def suggest_collaboration(creator: dict) -> dict:
    content_type = creator.get("content_type", "").lower()
    engagement = creator.get("engagement_quality", "").lower()
    subscribers = creator.get("subscribers", 0)

    if engagement == "high" and subscribers > 50000:
        strategy = "Sponsorship"
        reason = "High engagement and large reach make paid sponsorship worthwhile."
    elif "review" in content_type:
        strategy = "Product Trial"
        reason = "Review-focused creators convert well with free product trials."
    elif "tutorial" in content_type or "educational" in content_type:
        strategy = "Affiliate"
        reason = "Educational creators drive purchase intent — affiliate links work best."
    else:
        strategy = "UGC (User Generated Content)"
        reason = "Lifestyle creators produce authentic content ideal for brand repurposing."

    return {
        "strategy": strategy,
        "reason": reason
    }