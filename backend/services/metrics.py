# backend/services/metrics.py

def format_large_numbers(value):
    if value < 1_000:
        return f"${value:.2f}"
    elif value < 1_000_000:
        return f"${value / 1_000:.1f}K"
    elif value < 1_000_000_000:
        return f"${value / 1_000_000:.1f}M"
    return f"${value / 1_000_000_000:.1f}B"

def extract_key_metrics(company_data):
    income_statements = company_data["income_statement"]
    balance_sheet = company_data["balance_sheet"]
    cash_flow = company_data["cash_flow"]
    previous_income_statement = (income_statements[1] if len(income_statements) > 1 else None)
    latest_income_statement = income_statements[0]
    revenue_growth_percent = None
    if previous_income_statement:
        previous_revenue = (previous_income_statement["revenue"])
        latest_revenue = (latest_income_statement["revenue"])
        revenue_growth_percent = round(((latest_revenue - previous_revenue) / previous_revenue) * 100, 2)
    return {
        "latest_revenue": format_large_numbers(latest_income_statement["revenue"]),
        "previous_revenue": format_large_numbers(previous_income_statement["revenue"]) if previous_income_statement else None,
        "revenue_growth_percent": revenue_growth_percent,
        "free_cash_flow": format_large_numbers(cash_flow["freeCashFlow"]),
        "cash_and_short_term_investments": format_large_numbers(balance_sheet["cashAndShortTermInvestments"]),
        "debt": format_large_numbers(balance_sheet["totalDebt"]),
        "net_debt": format_large_numbers(balance_sheet["netDebt"])
    }