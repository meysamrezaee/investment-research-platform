# backend/services/openai_client.py

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def ask_llm(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.responses.create(
        model="gpt-5-nano", # change to gpt-5.4-mini later
        input=prompt
    )
    return response.output_text