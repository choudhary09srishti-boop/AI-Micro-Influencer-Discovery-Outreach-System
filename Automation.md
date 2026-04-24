# 📤 Outreach Automation Logic

## Email Automation
- Tool: **Gmail API** or **SendGrid (free tier)**
- Logic: Loop through `output.json`, extract `email` field, send via API
- Trigger: Run `main.py` → auto-send to all matched creators

## Instagram DM Automation
- Tool: **Instagram Graph API** (for business accounts)
- Logic: Extract `dm` field from `output.json`, send via API to creator handles
- Limitation: Requires creator's Instagram handle (not available via YouTube API)

## Scheduling
- Tool: **Python `schedule` library** or **GitHub Actions cron**
- Run pipeline daily/weekly for fresh discovery

## Rate Limiting
- Add `time.sleep(1)` between API calls to avoid quota exhaustion

## Flow
input keyword → main.py → output.json → email/DM sender script → messages delivered