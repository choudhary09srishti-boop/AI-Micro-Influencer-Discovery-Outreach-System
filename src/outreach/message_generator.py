import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def enforce_word_count(email: str, creator: dict, brand: dict) -> str:
    words = len(email.split())
    if 60 <= words <= 90:
        return email

    if words > 90:
        return " ".join(email.split()[:90])

    # Too short — expand with specific closing lines
    additions = [
        f"We believe your audience of skincare enthusiasts would genuinely connect with {brand.get('name', 'our brand')}'s approach to clean, effective formulations.",
        f"Your content on {', '.join(creator.get('top_topics', ['skincare'])[:2])} resonates deeply with what {brand.get('name', 'our brand')} stands for.",
        f"We'd love to explore a collaboration that brings real value to your audience and aligns with your content style.",
        f"Looking forward to discussing how we can create something meaningful together for your community."
    ]

    i = 0
    while len(email.split()) < 60 and i < len(additions):
        email = email.strip() + " " + additions[i]
        i += 1

    return " ".join(email.split()[:90])
    
    prompt = f"""
Rewrite this email to be STRICTLY between 60-90 words.
Keep the same tone and personalization but expand or trim as needed.
Reference the creator's content topics and brand values specifically.
Return ONLY the email text, nothing else.

Creator: {creator.get('name')}
Topics: {creator.get('top_topics')}
Brand: {brand.get('name')}
Brand Values: {brand.get('values')}

Original email:
{email}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    rewritten = response.choices[0].message.content.strip()
    return rewritten

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
- Recent Video Titles: {creator.get('video_titles_analyzed', [])}
- Match Score: {creator.get('match_score', '')}
- Match Reason: {creator.get('match_reason', '')}

Generate two personalized outreach messages:
1. Email: STRICTLY between 60-90 words. Must mention creator's specific video topics, brand values, and collaboration opportunity. Be warm and specific, not generic.
2. Instagram DM: STRICTLY between 15-30 words, casual and direct.

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

    text = response.choices[0].message.content.strip()
    result = json.loads(text)
    result["email"] = enforce_word_count(result["email"], creator, brand)
    return result