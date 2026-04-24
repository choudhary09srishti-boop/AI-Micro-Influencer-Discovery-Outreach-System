import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_creator(influencer: dict) -> dict:
    prompt = f"""
You are analyzing a YouTube micro-influencer profile for brand outreach.

Channel Name: {influencer['name']}
Subscribers: {influencer['subscribers']}
Total Views: {influencer['view_count']}
Videos: {influencer['video_count']}
Description: {influencer['description']}

Return ONLY a JSON object with these fields:
{{
  "niche": "primary content niche in 2-3 words",
  "content_type": "educational/entertainment/reviews/tutorials/lifestyle",
  "audience_type": "who their audience is in one sentence",
  "tone": "professional/casual/humorous/inspirational",
  "top_topics": ["topic1", "topic2", "topic3"],
  "engagement_quality": "high/medium/low based on views vs subscribers ratio"
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    import json
    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    analysis = json.loads(raw)
    return {**influencer, **analysis}