# ⚡ Quick Start — 5 Minutes to Your First Leads

This guide gets you from zero to a campaign-ready lead list in under 5 minutes.

## Prerequisites

- Python 3.10+
- A free [Apollo.io](https://app.apollo.io) account (50 free email credits/month)

---

## Step 1: Clone & Install (1 min)

```bash
git clone https://github.com/jarvis240615-cmyk/agent-sales-kit.git
cd agent-sales-kit
pip install -r requirements.txt
```

Or use the setup script:

```bash
bash scripts/setup.sh
```

---

## Step 2: Get Your Apollo API Key (2 min)

1. Go to [app.apollo.io](https://app.apollo.io)
2. Sign up / log in (free)
3. Navigate to **Settings → Integrations → API**
4. Click **Create API Key**
5. Copy the key

Then set it as an environment variable:

```bash
export APOLLO_API_KEY="your_api_key_here"

# Or add to your shell profile for persistence:
echo 'export APOLLO_API_KEY="your_api_key_here"' >> ~/.bashrc
```

See [docs/setup-apollo.md](docs/setup-apollo.md) for detailed Apollo setup.

---

## Step 3: Find Your First Leads (1 min)

Replace the values with your target market:

```bash
python scripts/find-leads.py \
  --industry "IT infrastructure" \
  --location "India" \
  --size "11,50" \
  --titles "IT Manager,CTO,Head of IT,Purchase Manager" \
  --limit 25 \
  --output my-leads.json
```

**Common industry tags:**
- `IT infrastructure`, `software`, `saas`, `manufacturing`, `healthcare`
- `financial services`, `retail`, `logistics`, `consulting`

**Common size ranges:**
- `1,10` — micro (1-10 employees)
- `11,50` — small (11-50)
- `51,200` — mid-market (51-200)
- `201,1000` — enterprise (201-1000)
- `1001,10000` — large enterprise

---

## Step 4: Run the Campaign (1 min)

```bash
python scripts/run-campaign.py \
  --leads my-leads.json \
  --template it-infrastructure \
  --sender "Your Name, Your Company" \
  --output my-campaign.csv
```

Your `my-campaign.csv` file is ready to import into:
- [Instantly.ai](https://instantly.ai) — bulk email sending
- [Lemlist](https://lemlist.com) — email + LinkedIn sequences
- [Mailshake](https://mailshake.com) — sales engagement
- Any email tool that accepts CSV import

---

## What's Next?

- 📧 Browse [email templates](templates/cold-email-sequences/) for your vertical
- 💼 Set up [LinkedIn outreach](templates/linkedin-messages/) alongside email
- 📊 Track your pipeline with the [CRM guide](docs/crm-guide.md)
- 🏆 Read [best practices](docs/best-practices.md) to maximize reply rates

---

## Troubleshooting

**`APOLLO_API_KEY not set` error:**
```bash
export APOLLO_API_KEY="your_key"
```

**`ModuleNotFoundError`:**
```bash
pip install -r requirements.txt
```

**Empty results:**
- Try broadening your search (larger location, less specific industry)
- Check your Apollo credit balance at [app.apollo.io](https://app.apollo.io)

**Rate limit errors:**
- Apollo free tier: 50 email reveals/month. Upgrade or use `--limit 10` for testing.
