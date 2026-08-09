# backend/agents/news_agent.py

import asyncio

from services.news_service import get_stock_news
from services.openai_client import ask_llm


async def analyze_news(symbol: str):

    news = await asyncio.to_thread(
        get_stock_news,
        symbol
    )

    if not news:
        return "No recent news found."

    prompt = f"""
You are an investment research analyst.

Review the following news:

{news}

Provide:

1. Key developments
2. Positive catalysts
3. Negative catalysts
4. Management developments
5. Investor concerns

Keep the response under 300 words.
"""

    return await asyncio.to_thread(
        ask_llm,
        prompt
    )
