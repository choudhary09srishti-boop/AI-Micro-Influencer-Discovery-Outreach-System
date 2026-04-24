import os
from datetime import datetime, timezone
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

def search_influencers(keyword: str, max_results: int = 20) -> list:
    youtube = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))

    search_response = youtube.search().list(
        q=f"{keyword} India",
        part="snippet",
        type="channel",
        regionCode="IN",
        relevanceLanguage="en",
        maxResults=max_results
    ).execute()

    channels = []
    for item in search_response.get("items", []):
        channel_id = item["snippet"]["channelId"]
        channels.append(channel_id)

    return get_channel_details(youtube, channels)


def get_channel_details(youtube, channel_ids: list) -> list:
    response = youtube.channels().list(
        part="snippet,statistics",
        id=",".join(channel_ids)
    ).execute()

    influencers = []
    for item in response.get("items", []):
        stats = item.get("statistics", {})
        snippet = item.get("snippet", {})

        sub_count = int(stats.get("subscriberCount", 0))
        if 5000 <= sub_count <= 100000:
            channel_id = item["id"]
            last_active = get_last_upload_date(youtube, channel_id)
            if not last_active:
                continue
            days_inactive = (datetime.now(timezone.utc) - last_active).days
            if days_inactive > 180:
                print(f"⏭ Skipping {snippet.get('title')} — inactive for {days_inactive} days")
                continue

            description = snippet.get("description", "")
            email = extract_email(description)

            influencers.append({
                "channel_id": channel_id,
                "name": snippet.get("title"),
                "description": description[:300],
                "subscribers": sub_count,
                "video_count": int(stats.get("videoCount", 0)),
                "view_count": int(stats.get("viewCount", 0)),
                "country": snippet.get("country", "Unknown"),
                "profile_link": f"https://youtube.com/channel/{channel_id}",
                "last_active_days_ago": days_inactive,
                "contact_email": email if email else "N/A"
            })

    return influencers


def get_last_upload_date(youtube, channel_id: str):
    try:
        response = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            order="date",
            maxResults=1,
            type="video"
        ).execute()
        items = response.get("items", [])
        if not items:
            return None
        published = items[0]["snippet"]["publishedAt"]
        return datetime.fromisoformat(published.replace("Z", "+00:00"))
    except:
        return None


def extract_email(text: str) -> str:
    import re
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else None