"""Persist gold price snapshots as JSON history."""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from google.cloud import storage as gcs
from google.cloud import bigquery
from google.oauth2 import service_account

from pipeline.extract.scraper import GoldQuote

_ICT = ZoneInfo("Asia/Ho_Chi_Minh")
MAX_SNAPSHOTS = 730  # ~2 years of daily snapshots

# --- Cloud Config ---
GCP_PROJECT = os.getenv("GCP_PROJECT_ID", "gold-price-platform")
GCS_BUCKET = os.getenv("GCS_BUCKET_NAME", "gold-price-lake")
BQ_DATASET = os.getenv("BQ_DATASET_NAME", "gold_prices_db")
BQ_TABLE = "silver_prices"
GCP_KEY_PATH = Path("gcp-key.json")

def _get_gcp_credentials():
    if GCP_KEY_PATH.exists():
        return service_account.Credentials.from_service_account_file(str(GCP_KEY_PATH))
    return None

def upload_to_gcs(local_path: Path, gcs_blob_name: str) -> None:
    try:
        credentials = _get_gcp_credentials()
        client = gcs.Client(project=GCP_PROJECT, credentials=credentials)
        bucket = client.bucket(GCS_BUCKET)
        blob = bucket.blob(gcs_blob_name)
        blob.upload_from_filename(str(local_path))
        print(f"Uploaded {local_path} to gs://{GCS_BUCKET}/{gcs_blob_name}")
    except Exception as e:
        print(f"Warning: Failed to upload to GCS: {e}")

def load_to_bigquery(quotes: list[GoldQuote], snapshot_time: datetime) -> None:
    try:
        credentials = _get_gcp_credentials()
        client = bigquery.Client(project=GCP_PROJECT, credentials=credentials)
        table_id = f"{GCP_PROJECT}.{BQ_DATASET}.{BQ_TABLE}"
        
        # Prepare rows for BigQuery
        rows_to_insert = []
        for q in quotes:
            row = asdict(q)
            row["snapshot_time"] = snapshot_time.isoformat()
            # Map keys to match BQ schema
            row["buy_price"] = row.pop("buy")
            row["sell_price"] = row.pop("sell")
            rows_to_insert.append(row)
        
        # Define schema and partitioning
        schema = [
            bigquery.SchemaField("brand", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("buy_price", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("sell_price", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("snapshot_time", "TIMESTAMP", mode="REQUIRED"),
        ]
        table = bigquery.Table(table_id, schema=schema)
        table.time_partitioning = bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field="snapshot_time",
        )
        
        # Create table if not exists
        try:
            client.create_table(table, exists_ok=True)
        except Exception as e:
            print(f"Warning: Table creation might have failed or already exists: {e}")

        errors = client.insert_rows_json(table_id, rows_to_insert)
        if errors:
            print(f"Encountered errors while inserting rows to BigQuery: {errors}")
        else:
            print(f"Inserted {len(rows_to_insert)} rows to {table_id}")
    except Exception as e:
        print(f"Warning: Failed to load to BigQuery: {e}")


@dataclass
class Snapshot:
    timestamp: str
    date: str
    entries: list[dict]

    @classmethod
    def from_quotes(cls, quotes: list[GoldQuote], when: datetime | None = None) -> Snapshot:
        now = when or datetime.now(_ICT)
        return cls(
            timestamp=now.strftime("%Y-%m-%d %H:%M:%S"),
            date=now.strftime("%Y-%m-%d"),
            entries=[asdict(q) for q in quotes],
        )


def load_history(path: Path) -> list[Snapshot]:
    if not path.exists():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [Snapshot(**item) for item in raw]


def save_history(path: Path, history: list[Snapshot]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    trimmed = history[-MAX_SNAPSHOTS:]
    path.write_text(
        json.dumps([s.__dict__ for s in trimmed], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def append_snapshot(path: Path, quotes: list[GoldQuote], when: datetime | None = None) -> Snapshot:
    now = when or datetime.now(_ICT)
    history = load_history(path)
    snap = Snapshot.from_quotes(quotes, now)
    history.append(snap)
    save_history(path, history)
    
    # Medallion Architecture: Save to Bronze (Raw)
    bronze_dir = Path("data/bronze") / now.strftime("%Y/%m/%d")
    bronze_dir.mkdir(parents=True, exist_ok=True)
    bronze_filename = f"raw_{now.strftime('%H%M%S')}.json"
    bronze_file = bronze_dir / bronze_filename
    bronze_file.write_text(json.dumps(snap.__dict__, ensure_ascii=False, indent=2), encoding="utf-8")
    
    # Cloud Integration: GCS (Bronze)
    gcs_blob_name = f"bronze/{now.strftime('%Y/%m/%d')}/{bronze_filename}"
    upload_to_gcs(bronze_file, gcs_blob_name)
    
    # Cloud Integration: BigQuery (Silver)
    load_to_bigquery(quotes, now)
    
    return snap


def quotes_to_dicts(quotes: list[GoldQuote]) -> list[dict]:
    return [asdict(q) for q in quotes]


def parse_snapshot_date(snap: Snapshot) -> date:
    return datetime.strptime(snap.date, "%Y-%m-%d").date()
