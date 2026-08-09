# backend/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

from schemas.requests import ResearchRequest
from schemas.responses import ResearchResponse

from agents.coordinator import run_research

import os
import traceback


# ----------------------------------
# Environment Variables
# ----------------------------------

load_dotenv()

app = FastAPI(
    title="Investment Research Platform"
)

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")


# ----------------------------------
# CORS
# ----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------------------------
# Health Check
# ----------------------------------

@app.get("/")
async def root():
    return {
        "message": "Investment Research Platform API Running"
    }


# ----------------------------------
# Research Endpoint
# ----------------------------------

@app.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest):
    try:
        result = await run_research(request.company)
        return result
    except ValueError as e:
        print("\n==== VALUE ERROR ====")
        traceback.print_exc()
        print("=====================\n")
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        print("\n==== RUNTIME ERROR ====")
        traceback.print_exc()
        print("=======================\n")
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        print("\n==== UNHANDLED EXCEPTION ====")
        traceback.print_exc()
        print("=============================\n")
        raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")