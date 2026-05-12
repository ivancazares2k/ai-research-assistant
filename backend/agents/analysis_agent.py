import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

async def run_analysis_agent(topic: str, search_findings: str) -> dict:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""You are a research analysis agent. You receive raw research findings 
and your job is to analyze them critically and extract deeper insights.

Topic: {topic}

Raw Research Findings:
{search_findings}

Provide your analysis in this exact structure:
- Core Insight: The single most important thing to understand about this topic
- Patterns & Connections: 2-3 patterns or connections you notice in the findings
- Gaps & Limitations: What important aspects are missing or unclear from the research
- Confidence Assessment: How well-established is the knowledge in this area (emerging/developing/established)
- Key Takeaway: One sentence summary of what someone should remember about this topic

Be analytical and critical. Your job is to add insight, not just restate the findings."""

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "agent": "analysis",
        "topic": topic,
        "analysis": message.content[0].text
    }