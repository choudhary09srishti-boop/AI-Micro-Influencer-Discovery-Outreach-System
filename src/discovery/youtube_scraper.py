import os
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
            influencers.append({
                "channel_id": item["id"],
                "name": snippet.get("title"),
                "description": snippet.get("description", "")[:300],
                "subscribers": sub_count,
                "video_count": int(stats.get("videoCount", 0)),
                "view_count": int(stats.get("viewCount", 0)),
                "country": snippet.get("country", "Unknown"),
                "profile_link": f"https://youtube.com/channel/{item['id']}"
            })

    return influencers