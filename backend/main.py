from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from agents.search_agent import run_search_agent
from agents.analysis_agent import run_analysis_agent
from agents.report_agent import run_report_agent
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import os

load_dotenv()

VALID_ACCESS_CODES = {"demo2024", "portfolio", "hiring"}

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="AI Research Assistant")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "https://ai-research-assistant-production-093d.up.railway.app",
        "https://ai-research-assistant-snowy-pi.vercel.app",
        "https://*.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def verify_access_code(request: Request):
    code = request.headers.get("X-Access-Code")
    if not code or code not in VALID_ACCESS_CODES:
        raise HTTPException(status_code=401, detail="Invalid or missing access code")
    return code

@app.get("/")
async def root():
    return {"message": "AI Research Assistant is running"}

@app.post("/validate")
async def validate(request: Request):
    body = await request.json()
    code = body.get("code", "")
    if code in VALID_ACCESS_CODES:
        return {"valid": True}
    raise HTTPException(status_code=401, detail="Invalid access code")

@app.post("/research")
@limiter.limit("10/hour")
async def research(request: Request, code: str = Depends(verify_access_code)):
    body = await request.json()
    topic = body.get("topic", "")

    search_result = await run_search_agent(topic)
    analysis_result = await run_analysis_agent(topic, search_result["findings"])
    report_result = await run_report_agent(
        topic,
        search_result["findings"],
        analysis_result["analysis"]
    )

    return {
        "topic": topic,
        "search": search_result["findings"],
        "analysis": analysis_result["analysis"],
        "report": report_result["report"]
    }