from pipeline.extract.scraper import parse_html

SAMPLE_HTML = """
<table class="gia-vang-search-data-table">
  <tr>
    <td><h2>SJC</h2></td>
    <td><span class="fixW">148.000.000</span></td>
    <td><span class="fixW">150.000.000</span></td>
  </tr>
  <tr>
    <td><h2>DOJI HN</h2></td>
    <td><span class="fixW">147.500.000</span></td>
    <td><span class="fixW">149.500.000</span></td>
  </tr>
</table>
"""


def test_parse_html_extracts_brands():
    quotes = parse_html(SAMPLE_HTML)
    assert len(quotes) == 2
    assert quotes[0].brand == "SJC"
    assert quotes[0].buy == 148_000_000
    assert quotes[0].sell == 150_000_000
    assert quotes[0].spread == 2_000_000


def test_parse_abbreviated_thousands_format():
    html = """
    <table class="gia-vang-search-data-table">
      <tr>
        <td><h2>SJC</h2></td>
        <td><span class="fixW">153,500</span></td>
        <td><span class="fixW">156,500</span></td>
      </tr>
    </table>
    """
    quotes = parse_html(html)
    assert quotes[0].buy == 153_500_000
    assert quotes[0].sell == 156_500_000


def test_parse_html_empty_table():
    assert parse_html("<html></html>") == []
