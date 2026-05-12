import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

async def run_report_agent(topic: str, search_findings: str, analysis: str) -> dict:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""You are a research report agent. You receive raw findings and analysis 
and your job is to write a clean, well-structured report that a human would enjoy reading.

Topic: {topic}

Research Findings:
{search_findings}

Analysis:
{analysis}

Write a comprehensive research report with these sections:
1. Executive Summary (2-3 sentences overview)
2. Key Facts (the most important things to know)
3. Deep Insights (the analytical layer - what it all means)
4. Open Questions (what remains uncertain or worth exploring)
5. Bottom Line (one clear takeaway for a busy reader)

Write in clear, engaging prose. Make it informative but accessible."""

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "agent": "report",
        "topic": topic,
        "report": message.content[0].text
    }