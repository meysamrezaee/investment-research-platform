# backend/services/news_service.py

import os
import requests

from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_stock_news(symbol: str):

    url = "https://newsapi.org/v2/everything"

    response = requests.get(
        url,
        params={
            "q": symbol,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 10
        },
        headers={
            "X-Api-Key": NEWS_API_KEY
        },
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    return data.get("articles", [])