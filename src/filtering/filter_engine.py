def filter_influencers(influencers: list, min_subs: int = 5000, max_subs: int = 100000) -> list:
    filtered = []
    for creator in influencers:
        subs = creator.get("subscribers", 0)
        if min_subs <= subs <= max_subs:
            filtered.append(creator)
    return filtered