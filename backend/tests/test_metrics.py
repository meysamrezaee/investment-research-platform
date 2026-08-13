import pytest

from backend.services import metrics


def test_format_large_numbers():
    assert metrics.format_large_numbers(2_500_000_000) == "$2.5B"
    assert metrics.format_large_numbers(950_000_000) == "$950.0M"
    assert metrics.format_large_numbers(1_500_000) == "$1.5M"
    assert metrics.format_large_numbers(2_500) == "$2.5K"
    assert metrics.format_large_numbers(750.98) == "$750.98"
    assert metrics.format_large_numbers(0) == "$0.00"


def test_extract_key_metrics_with_previous():
    company_data = {
        "income_statement": [
            {"revenue": 2_000_000_000},  # latest
            {"revenue": 1_500_000_000},  # previous
        ],
        "balance_sheet": {
            "cashAndShortTermInvestments": 500_000_000,
            "totalDebt": 300_000_000,
            "netDebt": 200_000_000,
        },
        "cash_flow": {
            "freeCashFlow": 250_000_000
        }
    }

    res = metrics.extract_key_metrics(company_data)

    assert res["latest_revenue"] == "$2.0B"
    assert res["previous_revenue"] == "$1.5B"
    assert res["revenue_growth_percent"] == round(((2_000_000_000 - 1_500_000_000) / 1_500_000_000) * 100, 2)
    assert res["free_cash_flow"] == "$250.0M"
    assert res["cash_and_short_term_investments"] == "$500.0M"
    assert res["debt"] == "$300.0M"
    assert res["net_debt"] == "$200.0M"
