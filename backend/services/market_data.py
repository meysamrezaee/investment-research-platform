# backend/services/market_data.py

import os
import time

import requests

from dotenv import load_dotenv

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")

BASE_URL = "https://financialmodelingprep.com/stable"
CACHE_TTL_SECONDS = 24 * 60 * 60
_CACHE = {}


def _request_with_cache(url: str, params: dict):
    cache_key = (url, tuple(sorted({k: v for k, v in params.items() if k != "apikey"}.items())))
    now = time.time()
    cached_entry = _CACHE.get(cache_key)

    if cached_entry is not None and now - cached_entry["timestamp"] < CACHE_TTL_SECONDS:
        return cached_entry["value"]

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()
    _CACHE[cache_key] = {"value": data, "timestamp": now}
    return data


def get_company_profile(symbol: str):
    url = f"{BASE_URL}/profile"
    data = _request_with_cache(
        url,
        {
            "symbol": symbol,
            "apikey": FMP_API_KEY
        }
    )

    if not data:
        raise ValueError(f"No profile found for {symbol}")

    return data[0]


def get_income_statement(symbol: str):

    url = f"{BASE_URL}/income-statement"
    data = _request_with_cache(
        url,
        {
            "symbol": symbol,
            "apikey": FMP_API_KEY
        }
    )

    if not data:
        raise ValueError(f"No income statement found for {symbol}")

    return data[:5]


def get_balance_sheet(symbol: str):

    url = f"{BASE_URL}/balance-sheet-statement"
    data = _request_with_cache(
        url,
        {
            "symbol": symbol,
            "apikey": FMP_API_KEY
        }
    )

    if not data:
        raise ValueError(f"No balance sheet found for {symbol}")

    return data[0]


def get_cash_flow_statement(symbol: str):

    url = f"{BASE_URL}/cash-flow-statement"
    data = _request_with_cache(
        url,
        {
            "symbol": symbol,
            "apikey": FMP_API_KEY
        }
    )

    if not data:
        raise ValueError(f"No cash flow statement found for {symbol}")

    return data[0]
    
def get_company_data(symbol: str):

    profile = get_company_profile(symbol)

    income_statement = get_income_statement(symbol)

    balance_sheet = get_balance_sheet(symbol)

    cash_flow = get_cash_flow_statement(symbol)

    return {
        "profile": profile,
        "income_statement": income_statement,
        "balance_sheet": balance_sheet,
        "cash_flow": cash_flow
    }
    
   
def get_stock_peers(symbol: str):

    url = f"{BASE_URL}/stock-peers"
    params = {
        "symbol": symbol,
        "apikey": FMP_API_KEY
    }

    return _request_with_cache(url, params)