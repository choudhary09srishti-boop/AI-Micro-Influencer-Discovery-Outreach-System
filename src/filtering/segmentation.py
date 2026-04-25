import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_segments(keyword: str) -> list:
    prompt = f"""
For the content category "{keyword}", suggest exactly 3 logical creator segment names.
These should be specific to the category, not generic.

Example for skincare: ["Skincare Educators", "Makeup Tutorial Creators", "Product Review Creators"]
Example for education: ["Olympiad Preparation", "Reasoning & Aptitude", "Student Competition Awareness"]
Example for finance: ["Investment Educators", "Budgeting Advisors", "Stock Market Creators"]

Return ONLY a JSON array of 3 strings. No extra text.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)

def segment_creators(creators: list, keyword: str = "general") -> dict:
    segment_names = generate_segments(keyword)
    segments = {name: [] for name in segment_names}
    keys = list(segments.keys())

    for creator in creators:
        content_type = creator.get("content_type", "").lower()
        topics = " ".join(creator.get("top_topics", [])).lower()
        niche = creator.get("niche", "").lower()
        combined = content_type + " " + topics + " " + niche

        if "educat" in combined or "health" in combined or "tips" in combined or "dermat" in combined:
            creator["segment"] = keys[0]
            segments[keys[0]].append(creator)
        elif "tutorial" in combined or "routine" in combined or "makeup" in combined or "how" in combined:
            creator["segment"] = keys[1]
            segments[keys[1]].append(creator)
        else:
            creator["segment"] = keys[2]
            segments[keys[2]].append(creator)

    return segments