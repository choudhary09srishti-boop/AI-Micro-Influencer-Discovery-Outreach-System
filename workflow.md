# Step-by-Step Workflow

## Step 1 — Keyword Input
User provides brand keyword and brand details at runtime via terminal prompts.

## Step 2 — Discovery
YouTube Data API v3 searches for Indian channels using the keyword.
Region filter: IN. Returns channel IDs.

## Step 3 — Filtering
Channels are filtered by subscriber count (5K–100K).
Only active Indian micro-influencers are kept.

## Step 4 — Content Analysis
Groq LLM (Llama 3.3-70b) analyzes channel description to extract:
- Niche
- Content type
- Tone
- Top topics
- Audience type
- Engagement quality

## Step 5 — Brand Matching
Groq LLM compares creator profile against brand details.
Returns a relevance score (0–100) and reason.

## Step 6 — Outreach Generation
Groq LLM generates:
- Personalized email (60–90 words)
- Instagram DM (15–30 words)
Both reference creator niche, topics, and brand values.

## Step 7 — Collaboration Strategy
Rule-based engine assigns strategy:
- Sponsorship → high engagement + 50K+ subs
- Product Trial → review creators
- Affiliate → educational creators
- UGC → lifestyle creators

## Step 8 — Segmentation
Creators are grouped into 3 clusters:
- Educators
- Tutorial Creators
- Product Reviewers

## Step 9 — Output
Full enriched data saved to data/output.json.
Architecture diagram saved to data/architecture_diagram.png.