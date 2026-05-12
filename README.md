# AI Research Assistant

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

**Frontend**
- React — UI framework
- Vite — build tool
- react-markdown — renders formatted reports

## Project Structure