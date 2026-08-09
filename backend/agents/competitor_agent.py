# backend/agents/competitor_agent.py

import asyncio

from services.market_data import get_stock_peers
from services.openai_client import ask_llm


async def analyze_competitors(symbol: str):

    peers = await asyncio.to_thread(
        get_stock_peers,
        symbol
    )

    prompt = f"""
    Analyze these competitors:

    {peers}

    Discuss:
    - Main competitors
    - Relative positioning
    - Competitive advantages
    - Competitive threats
    """

    return await asyncio.to_thread(
        ask_llm,
        prompt
    )