# Setting Up Apollo.io

Apollo.io is the lead enrichment engine behind agent-sales-kit. Free plan gives 50 email credits/month.

---

## Step 1 — Create Account

1. Go to **https://app.apollo.io**
2. Sign up with your work email (higher deliverability than Gmail)
3. Complete onboarding (skip the paid upgrade prompts)

## Step 2 — Get Your API Key

1. Click your avatar (top right) → **Settings**
2. Go to **Integrations** → **API**
3. Click **Create new key**
4. Name it: `agent-sales-kit`
5. Copy the key — you won't see it again

## Step 3 — Configure

```bash
# Option A: Environment variable (recommended)
export APOLLO_API_KEY=your_key_here

# Option B: .env file
echo "APOLLO_API_KEY=your_key_here" >> .env
```

## Step 4 — Test

```bash
python scripts/find-leads.py --industry "test" --location "Mumbai" --limit 1
```

Expected output: `✅ Found X companies`

---

## Credits Explained

| Action | Credits Used |
|--------|-------------|
| Find email address | 1 credit |
| Find phone number | 2 credits |
| Company search | 0 credits |
| People search (no reveal) | 0 credits |

**Free plan:** 50 email reveals/month  
**Basic ($49/mo):** 1,000 credits/month  
**Professional ($99/mo):** 2,000 credits/month + sequences

## Tips

- Use `--limit 25` to stay within free tier during testing
- Apollo's free emails are usually work emails (high deliverability)
- Always verify before sending: check for `email_verified: true` in leads.json
