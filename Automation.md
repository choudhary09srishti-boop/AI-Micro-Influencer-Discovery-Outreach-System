# Outreach Automation Layer

## Email Automation

### Option 1 — Gmail SMTP (Free)
Connect via Python's smtplib:
- Enable 2FA on Gmail
- Generate App Password
- Use SMTP server: smtp.gmail.com, port 587
- Loop through output.json, extract email field, send via SMTP

### Option 2 — SendGrid Free Tier
- Sign up at sendgrid.com (100 emails/day free)
- Use sendgrid Python SDK
- Plug in creator email from output.json
- Personalized email body already generated in pipeline

### Option 3 — Brevo Free Tier
- Sign up at brevo.com (300 emails/day free)
- Use Brevo API or SMTP relay
- Same logic as SendGrid

---

## Instagram DM Automation

### Option 1 — Instagrapi (Python Library)
- Open source Instagram private API wrapper
- Login with Instagram credentials
- Extract creator username from profile_link
- Send DM using client.direct_send()

### Option 2 — Meta Graph API
- Official Meta API for business accounts
- Requires Facebook Business Manager
- Use /me/messages endpoint
- Send pre-generated DM from output.json

### Option 3 — Apify Workflows
- No-code automation platform
- Use Instagram DM Actor on Apify
- Feed creator handles + DM text from output.json
- Schedule runs daily/weekly

---

## Automation Flow
output.json
↓
extract creator email + DM
↓
email sender (Gmail SMTP / SendGrid / Brevo)
↓
Instagram DM sender (Instagrapi / Meta Graph API / Apify)
↓
outreach delivered

## Scheduling
- Use Python `schedule` library for daily runs
- Or GitHub Actions cron job to trigger pipeline automatically

## Rate Limiting
- Add time.sleep(2) between each message
- Respect platform API quotas
- SendGrid: 100/day, Brevo: 300/day, Instagrapi: 20 DMs/hour
