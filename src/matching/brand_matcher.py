import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def match_brand(creator: dict, brand: dict) -> dict:
    prompt = f"""
You are a brand-influencer matching expert.

Brand:
- Name: {brand['name']}
- Industry: {brand['industry']}
- Target Audience: {brand['target_audience']}
- Values: {brand['values']}

Creator:
- Name: {creator['name']}
- Niche: {creator.get('niche', '')}
- Content Type: {creator.get('content_type', '')}
- Tone: {creator.get('tone', '')}
- Top Topics: {creator.get('top_topics', [])}
- Audience Type: {creator.get('audience_type', '')}
- Engagement Quality: {creator.get('engagement_quality', '')}

Give a match score from 0-100 and a one line reason.
Respond in this exact JSON format only:
{{"score": 85, "reason": "your reason here"}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    import json
    text = response.choices[0].message.content.strip()
    return json.loads(text)