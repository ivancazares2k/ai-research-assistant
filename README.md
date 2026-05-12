# AI Research Assistant

**Live Demo:** https://ai-research-assistant-snowy-pi.vercel.app  
**Access Code:** demo2024

A full-stack web application where multiple AI agents research any topic in parallel and return a structured report.

## What It Does

Type any topic or question. Three specialized AI agents go to work:

- **Search Agent** — finds key facts, concepts, and angles worth investigating
- **Analysis Agent** — critically analyzes the findings, identifies patterns and gaps
- **Report Agent** — synthesizes everything into a clean, readable report

Results appear as a formatted report with three layers: the raw research, the analysis, and the final synthesis.

## Tech Stack

**Backend**
- FastAPI — Python web framework
- Anthropic Claude API — powers all three agents
- Python asyncio — handles agent orchestration
- SlowAPI — rate limiting
- Railway — backend hosting

**Frontend**
- React — UI framework
- Vite — build tool
- react-markdown — renders formatted reports
- Vercel — frontend hosting

## Security

- Access code authentication — only authorized users can make requests
- Rate limiting — 10 requests per hour per IP address
- API keys stored as environment variables, never in code

## Project Structure
ai-research-assistant/
├── backend/
│   ├── main.py              # FastAPI app and /research endpoint
│   ├── agents/
│   │   ├── search_agent.py  # Finds key facts and angles
│   │   ├── analysis_agent.py# Analyzes and critiques findings
│   │   └── report_agent.py  # Writes the final report
│   ├── Procfile             # Railway deployment config
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── App.jsx          # Main React component
│       └── App.css          # Styles
└── README.md
## Running Locally

### Prerequisites
- Python 3.9+
- Node.js 18+
- Anthropic API key

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` folder:
ANTHROPIC_API_KEY=your_key_here
Start the server:
```bash
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` and enter access code `demo2024`.

## How the Multi-Agent Pipeline Works

Most AI apps send one prompt and get one response. This project chains three specialized agents where each one builds on the previous:

1. The **Search Agent** receives your topic and returns structured research
2. The **Analysis Agent** receives the search output and adds a critical layer
3. The **Report Agent** receives both and writes the final synthesis

Each agent has a specific job description baked into its prompt. Specialization produces better output than asking one prompt to do everything.

## What I Learned

- FastAPI and async Python
- Multi-agent architecture in pure Python code
- Access code authentication and rate limiting
- Deploying a full-stack app to Railway and Vercel
- Connecting a React frontend to a Python backend

## Author

Built by Ivan Cazares as a portfolio project while transitioning into AI engineering.