import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def match_brand(creator: dict, brand: dict) -> dict:
    prompt = f"""
You are a strict brand-influencer matching expert.

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
- Recent Video Titles: {creator.get('video_titles_analyzed', [])}

Scoring rules:
- 80-100: Strong niche, audience, and value alignment
- 50-79: Partial match, some overlap
- 20-49: Weak match, different niche but some relevance
- 0-19: No alignment at all

Be strict. Korean beauty and Ayurvedic herbal brands are NOT the same.
A finance creator and a skincare brand is 0.
Give a score and one line reason.

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