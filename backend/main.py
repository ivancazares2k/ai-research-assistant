from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from agents.search_agent import run_search_agent
from agents.analysis_agent import run_analysis_agent
from agents.report_agent import run_report_agent
import os

load_dotenv()

app = FastAPI(title="AI Research Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Research Assistant is running"}

@app.post("/research")
async def research(request: dict):
    topic = request.get("topic", "")

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