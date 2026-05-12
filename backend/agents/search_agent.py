import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

async def run_search_agent(topic: str) -> dict:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    prompt = f"""You are a research search agent. Your job is to identify the most 
important facts, key concepts, and angles worth investigating about a topic.

Topic: {topic}

Return your response in this exact structure:
- Key Facts: List 5 important facts about this topic
- Key Concepts: List 3-4 core concepts someone needs to understand this topic
- Angles to Investigate: List 3 interesting angles or questions worth exploring further

Be specific and informative. This will be used by other agents to do deeper analysis."""

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "agent": "search",
        "topic": topic,
        "findings": message.content[0].text
    }
