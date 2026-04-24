# 🤖 Automated Micro-Influencer Outreach System

An AI-powered pipeline that automatically discovers Indian micro-influencers,
analyzes their content, matches them with a brand, and generates personalized outreach messages.

---

## 🔧 Tech Stack
- **Python** — Core language
- **YouTube Data API v3** — Influencer discovery
- **Groq LLM (Llama 3.3-70b)** — Content analysis, brand matching, outreach generation
- **Matplotlib** — Architecture diagram

---

## ⚙️ Setup

1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Add API keys to `.env`:
YOUTUBE_API_KEY=your_key
GROQ_API_KEY=your_key

---

## 🚀 Run

```bash
python main.py
```

---

## 🔄 Pipeline

1. **Discovery** — YouTube API searches Indian creators by keyword
2. **Filtering** — Keeps only 5K–100K subscriber channels
3. **Enrichment** — Collects name, subs, views, profile link
4. **Content Analysis** — Groq LLM identifies niche, tone, topics
5. **Brand Matching** — Groq LLM scores creator-brand fit (0–100)
6. **Outreach Generation** — Groq LLM writes personalized Email + DM
7. **Collaboration Strategy** — Rule-based engine suggests sponsorship/affiliate/UGC/product trial

---

## 📦 Output

- `data/output.json` — Full enriched creator data with outreach messages
- `data/architecture_diagram.png` — Visual pipeline diagram

---

## 📁 Project Structure
├── src/
│   ├── discovery/       # YouTube scraper
│   ├── filtering/       # Subscriber filter
│   ├── analysis/        # Content analyzer
│   ├── matching/        # Brand matcher
│   └── outreach/        # Message generator + collaboration strategy
├── data/                # Output files
├── main.py              # Entry point
├── architecture_diagram.py
├── requirements.txt
└── .env


---

## 🤝 Collaboration Types
| Type | When Used |
|------|-----------|
| Sponsorship | High engagement + 50K+ subscribers |
| Product Trial | Review-focused creators |
| Affiliate | Educational creators |
| UGC | Lifestyle creators |