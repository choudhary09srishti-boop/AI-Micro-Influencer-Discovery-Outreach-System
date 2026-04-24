import json
from src.discovery.youtube_scraper import search_influencers
from src.filtering.filter_engine import filter_influencers
from src.analysis.content_analyzer import analyze_creator
from src.matching.brand_matcher import match_brand
from src.outreach.message_generator import generate_outreach
from src.outreach.collaboration_strategy import suggest_collaboration

brand = {
    "name": "Mamaearth",
    "industry": "Skincare",
    "target_audience": "Young Indian women aged 18-35",
    "values": "Natural ingredients, toxin-free, sustainable"
}

if __name__ == "__main__":
    keyword = "skincare"

    print("🔍 Discovering influencers...")
    results = search_influencers(keyword)

    print(f"⚙️ Filtering {len(results)} creators...")
    filtered = filter_influencers(results)

    print(f"✅ {len(filtered)} micro-influencers found\n")

    output = []
    for r in filtered:
        analysis = analyze_creator(r)
        r.update(analysis)
        match = match_brand(r, brand)
        r["match_score"] = match["score"]
        r["match_reason"] = match["reason"]
        messages = generate_outreach(r, brand)
        r["email"] = messages["email"]
        r["dm"] = messages["dm"]
        collab = suggest_collaboration(r)
        r["collaboration_strategy"] = collab["strategy"]
        r["collaboration_reason"] = collab["reason"]

        print(f"Name: {r['name']} | Score: {r['match_score']}")
        print(f"EMAIL:\n{r['email']}")
        print(f"\nDM:\n{r['dm']}")
        print(f"Strategy: {collab['strategy']} — {collab['reason']}")
        print("=" * 60)

        output.append({
            "name": r["name"],
            "subscribers": r["subscribers"],
            "profile_link": r["profile_link"],
            "niche": r.get("niche"),
            "content_type": r.get("content_type"),
            "tone": r.get("tone"),
            "top_topics": r.get("top_topics"),
            "engagement_quality": r.get("engagement_quality"),
            "match_score": r.get("match_score"),
            "match_reason": r.get("match_reason"),
            "email": r.get("email"),
            "dm": r.get("dm"),
            "collaboration_strategy": r.get("collaboration_strategy"),
            "collaboration_reason": r.get("collaboration_reason"),
        })

    with open("data/output.json", "w") as f:
        json.dump(output, f, indent=2)

    print("\n✅ Saved to data/output.json")