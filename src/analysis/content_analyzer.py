import os
import json
from groq import Groq
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_recent_video_titles(channel_id: str, max_results: int = 5) -> list:
    try:
        youtube = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))
        response = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            order="date",
            maxResults=max_results,
            type="video"
        ).execute()
        titles = [item["snippet"]["title"] for item in response.get("items", [])]
        print(f"  📹 Fetched {len(titles)} video titles")
        return titles
    except Exception as e:
        print(f"  ⚠️ Could not fetch titles: {e}")
        return []

def analyze_creator(influencer: dict) -> dict:
    channel_id = influencer.get("channel_id", "")
    video_titles = get_recent_video_titles(channel_id)
    titles_text = "\n".join(video_titles) if video_titles else "No titles available"

    prompt = f"""
You are analyzing a YouTube micro-influencer profile for brand outreach.

Channel Name: {influencer['name']}
Subscribers: {influencer['subscribers']}
Total Views: {influencer['view_count']}
Videos: {influencer['video_count']}
Description: {influencer['description']}

Recent Video Titles:
{titles_text}

Return ONLY a JSON object with these fields:
{{
  "niche": "primary content niche in 2-3 words",
  "content_type": "educational/entertainment/reviews/tutorials/lifestyle",
  "audience_type": "who their audience is in one sentence",
  "tone": "professional/casual/humorous/inspirational",
  "top_topics": ["topic1", "topic2", "topic3"],
  "engagement_quality": "high/medium/low based on views vs subscribers ratio",
  analysis["video_titles_analyzed"] = video_titles
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    analysis = json.loads(raw)
    analysis["video_titles_analyzed"] = video_titles
    return {**influencer, **analysis}