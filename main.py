import json
from src.discovery.youtube_scraper import search_influencers
from src.filtering.filter_engine import filter_influencers
from src.filtering.segmentation import segment_creators
from src.analysis.content_analyzer import analyze_creator
from src.matching.brand_matcher import match_brand
from src.outreach.message_generator import generate_outreach
from src.outreach.collaboration_strategy import suggest_collaboration

if __name__ == "__main__":
    print("=== Micro-Influencer Outreach System ===\n")
    keyword = input("Enter brand keyword (e.g. skincare, finance, education): ").strip()
    brand_name = input("Enter brand name: ").strip()
    brand_industry = input("Enter brand industry: ").strip()
    brand_audience = input("Enter target audience: ").strip()
    brand_values = input("Enter brand values: ").strip()

    brand = {
        "name": brand_name,
        "industry": brand_industry,
        "target_audience": brand_audience,
        "values": brand_values
    }

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
            "platform": "YouTube",
            "name": r["name"],
            "subscribers": r["subscribers"],
            "profile_link": r["profile_link"],
            "niche": r.get("niche"),
            "content_type": r.get("content_type"),
            "tone": r.get("tone"),
            "top_topics": r.get("top_topics"),
            "engagement_quality": r.get("engagement_quality"),
            "contact_email": "N/A",
            "match_score": r.get("match_score"),
            "match_reason": r.get("match_reason"),
            "email": r.get("email"),
            "dm": r.get("dm"),
            "collaboration_strategy": r.get("collaboration_strategy"),
            "video_titles_analyzed": r.get("video_titles_analyzed", []),
            "collaboration_reason": r.get("collaboration_reason"),
        })

    segments = segment_creators(output)
    print("\n📊 Final Creator Segments:")
    for seg, creators in segments.items():
        print(f"  {seg}: {len(creators)} creators")

    with open("data/output.json", "w") as f:
        json.dump(output, f, indent=2)

    print("\n✅ Saved to data/output.json")