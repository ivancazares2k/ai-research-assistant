from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from agents.search_agent import run_search_agent

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

@app.post("/search")
async def search(request: dict):
    topic = request.get("topic", "")
    result = await run_search_agent(topic)
    return result