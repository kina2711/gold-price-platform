{{ config(materialized='table') }}

WITH raw_prices AS (
    SELECT
        brand,
        buy_price,
        sell_price,
        sell_price - buy_price AS spread,
        DATE(snapshot_time) AS report_date,
        snapshot_time
    FROM {{ source('gold_prices_db', 'silver_prices') }}
),

daily_latest AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY brand, report_date 
            ORDER BY snapshot_time DESC
        ) as rn
    FROM raw_prices
)

SELECT
    brand,
    buy_price,
    sell_price,
    spread,
    report_date,
    snapshot_time as last_updated
FROM daily_latest
WHERE rn = 1
ORDER BY brand ASC
