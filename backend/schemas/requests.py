# schema/requests.py

from pydantic import BaseModel

class ResearchRequest(BaseModel):
    company: str