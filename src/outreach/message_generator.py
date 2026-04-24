import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_outreach(creator: dict, brand: dict) -> dict:
    prompt = f"""
You are an influencer marketing specialist.

Brand:
- Name: {brand['name']}
- Industry: {brand['industry']}
- Target Audience: {brand['target_audience']}
- Values: {brand['values']}

Creator:
- Name: {creator['name']}
- Niche: {creator.get('niche', '')}
- Top Topics: {creator.get('top_topics', [])}
- Tone: {creator.get('tone', '')}
- Content Type: {creator.get('content_type', '')}
- Match Score: {creator.get('match_score', '')}
- Match Reason: {creator.get('match_reason', '')}

Generate two personalized outreach messages:
1. Email (60-90 words, professional yet warm)
2. Instagram DM (15-30 words, casual and direct)

Respond in this exact JSON format only:
{{
  "email": "your email here",
  "dm": "your dm here"
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    import json
    text = response.choices[0].message.content.strip()
    return json.loads(text)