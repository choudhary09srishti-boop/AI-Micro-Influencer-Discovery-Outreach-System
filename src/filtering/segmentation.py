def segment_creators(creators: list) -> dict:
    segments = {
        "Educators": [],
        "Tutorial Creators": [],
        "Product Reviewers": []
    }

    for creator in creators:
        content_type = creator.get("content_type", "").lower()
        topics = " ".join(creator.get("top_topics", [])).lower()
        niche = creator.get("niche", "").lower()
        combined = content_type + " " + topics + " " + niche

        if "educat" in combined or "health" in combined or "tips" in combined or "dermat" in combined:
            creator["segment"] = "Educators"
            segments["Educators"].append(creator)
        elif "tutorial" in combined or "routine" in combined or "makeup" in combined or "how" in combined:
            creator["segment"] = "Tutorial Creators"
            segments["Tutorial Creators"].append(creator)
        else:
            creator["segment"] = "Product Reviewers"
            segments["Product Reviewers"].append(creator)

    return segments