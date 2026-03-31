# 🚀 agent-sales-kit

<div align="center">

**The complete AI-powered B2B sales automation kit.**
*Give it a target market → it finds companies → enriches contacts → writes personalized emails → tracks your pipeline. Zero SaaS subscriptions required.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/jarvis240615-cmyk/agent-sales-kit?style=social)](https://github.com/jarvis240615-cmyk/agent-sales-kit/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/jarvis240615-cmyk/agent-sales-kit?style=social)](https://github.com/jarvis240615-cmyk/agent-sales-kit/network/members)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[Quick Start](#-quick-start) · [Use Cases](#-use-cases) · [Docs](docs/) · [Contributing](#-contributing)

</div>

---

## 🎬 See It In Action

```
$ python scripts/find-leads.py --industry "IT infrastructure" --location "India" --limit 25

🔍 Searching for IT infrastructure companies in India...
✅ Found 25 companies

  📧 Finding contacts at Tata Communications...
  📧 Finding contacts at HCL Infosystems...
  📧 Finding contacts at Wipro Infrastructure...
  📧 Finding contacts at Tech Mahindra...
  📧 Finding contacts at Hexaware Technologies...
  [... 20 more ...]

✅ Done! 73 leads found, 61 with verified emails
📁 Saved to leads.json

$ python scripts/run-campaign.py --leads leads.json --template it-infrastructure

📊 Campaign Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Total leads:        73
  Emails ready:       61
  Personalized:       61/61 (100%)
  Output:             campaign.csv
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ campaign.csv ready to import into any email tool!
```

---

## 🧠 What It Does

> Most B2B sales stacks cost $500–$2000/month. This does the same job for the cost of an Apollo free tier and a few API credits.

- **🔍 Lead Finding** — Search Apollo's 270M+ contact database by industry, location, company size, and job title
- **📧 Contact Enrichment** — Find verified work emails, LinkedIn profiles, and phone numbers for decision-makers
- **✍️ AI Email Writing** — Generate personalized 5-touch cold email sequences using proven copywriting frameworks
- **💼 LinkedIn Outreach** — Scripted connection requests and InMail follow-up sequences
- **📅 Follow-up Cadence** — Automated follow-up scheduling so no lead goes cold
- **📊 Pipeline Tracking** — CRM-lite tracking via Google Sheets, Airtable, or CSV
- **🔁 End-to-End Runner** — One command to go from ICP → campaign-ready CSV

---

## ⚡ Quick Start

**3 commands to your first campaign:**

```bash
# 1. Clone and install
git clone https://github.com/jarvis240615-cmyk/agent-sales-kit.git
cd agent-sales-kit && pip install -r requirements.txt

# 2. Set your Apollo API key (free tier works!)
export APOLLO_API_KEY="your_key_here"

# 3. Run your first lead search
python scripts/find-leads.py --industry "SaaS" --location "United States" --size "11,50" --limit 25
```

> 🔑 **No Apollo account?** [Get a free key here](https://app.apollo.io) — 50 free email credits/month on the free tier. See [docs/setup-apollo.md](docs/setup-apollo.md) for details.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     agent-sales-kit                          │
│                                                             │
│  INPUT: Target Market (industry + location + ICP)          │
│         ↓                                                   │
│  ┌──────────────┐    ┌──────────────────┐                  │
│  │ Lead Finder  │───▶│ Contact Enricher │                  │
│  │              │    │                  │                  │
│  │ Apollo API   │    │ Apollo People    │                  │
│  │ 270M+ orgs  │    │ Email verify     │                  │
│  └──────────────┘    └────────┬─────────┘                  │
│                               │                             │
│                               ▼                             │
│  ┌──────────────┐    ┌──────────────────┐                  │
│  │ Email Writer │◀───│   AI Personalizer│                  │
│  │              │    │                  │                  │
│  │ 5-touch seq  │    │ Company context  │                  │
│  │ Templates    │    │ Role-aware copy  │                  │
│  └──────┬───────┘    └──────────────────┘                  │
│         │                                                   │
│         ▼                                                   │
│  ┌──────────────┐    ┌──────────────────┐                  │
│  │  LinkedIn    │    │  Follow-up       │                  │
│  │  Outreach    │    │  Scheduler       │                  │
│  │              │    │                  │                  │
│  │ Connect reqs │    │ Day 1,3,7,14,21  │                  │
│  │ InMail seqs  │    │ Multi-channel    │                  │
│  └──────┬───────┘    └────────┬─────────┘                  │
│         │                     │                             │
│         └──────────┬──────────┘                             │
│                    ▼                                        │
│  ┌──────────────────────────────┐                           │
│  │         CRM Manager          │                           │
│  │  Google Sheets / Airtable /  │                           │
│  │  HubSpot / CSV Pipeline      │                           │
│  └──────────────────────────────┘                           │
│                    │                                        │
│                    ▼                                        │
│  OUTPUT: campaign.csv + pipeline dashboard                 │
└─────────────────────────────────────────────────────────────┘
```

---

## ✨ Features

### Lead Generation
- 🔍 Search 270M+ companies via Apollo.io API
- 🎯 Filter by industry, location, company size, technology stack
- 💡 ICP scoring to prioritize best-fit accounts
- 🏢 Company intelligence: funding, tech stack, recent news

### Contact Enrichment
- 📧 Verified work email addresses (95%+ deliverability)
- 🔗 LinkedIn profile URLs
- 📱 Phone numbers (where available)
- 👤 Decision-maker identification by job title
- 🛡️ GDPR-compliant data sourcing

### Email Sequences
- ✍️ 5-touch email sequences per vertical (IT, SaaS, Manufacturing, etc.)
- 🤖 AI personalization using company + role context
- 📐 Multiple proven frameworks: PAS, AIDA, Pattern Interrupt
- 📊 Subject line variants for A/B testing
- 📅 Timing recommendations per sequence step

### LinkedIn Outreach
- 🤝 Connection request templates (300 char, high acceptance rate)
- 💬 InMail sequences for premium accounts
- 📝 Profile view → connection → message → follow-up playbook

### Pipeline Management
- 📊 Google Sheets CRM template (no setup required)
- 🔄 Airtable integration
- 🏗️ HubSpot sync via API
- 📤 CSV export for any tool

### Developer-Friendly
- 🐍 Pure Python 3.10+ scripts
- 🔧 Modular agent architecture
- 📦 pip installable
- 🧪 Dry-run mode for testing
- 🔑 Environment variable config (no hardcoded credentials)

---

## 🎯 Use Cases

### 1. IT Infrastructure Startup (India Market)
> **Scenario:** You sell network switches and firewall solutions to mid-market companies in India.

```bash
python scripts/find-leads.py \
  --industry "IT infrastructure" \
  --location "India" \
  --size "51,200" \
  --titles "IT Manager,Head of IT,CTO,Purchase Manager" \
  --limit 50 \
  --output it-leads.json

python scripts/run-campaign.py \
  --leads it-leads.json \
  --template it-infrastructure \
  --sender "Rahul Sharma, Flair Networks"
```

**Result:** 50 companies → ~180 decision-maker contacts → 5-email sequence ready to send.
See full example in [examples/it-infrastructure-india/](examples/it-infrastructure-india/).

---

### 2. SaaS Company Targeting US Startups
> **Scenario:** You sell a project management tool to Series A/B startups.

```bash
python scripts/find-leads.py \
  --industry "software" \
  --location "San Francisco, CA" \
  --size "11,100" \
  --titles "VP Engineering,Head of Product,CTO,Engineering Manager" \
  --limit 100
```

**Result:** Hyper-targeted list of funded startups with verified engineering leader contacts.
See full example in [examples/saas-outbound/](examples/saas-outbound/).

---

### 3. Manufacturing Equipment Sales (Europe)
> **Scenario:** Industrial equipment dealer targeting factory operations managers in Germany.

```bash
python scripts/find-leads.py \
  --industry "manufacturing" \
  --location "Germany" \
  --size "201,1000" \
  --titles "Operations Manager,Plant Manager,Head of Procurement,COO" \
  --limit 75
```

Uses the [manufacturing email template](templates/cold-email-sequences/manufacturing.md) with localized copy.

---

### 4. Agency Selling to E-Commerce Brands
> **Scenario:** Digital marketing agency targeting DTC e-commerce brands $1M-$10M revenue.

The `saas-company.md` template adapts beautifully for agency outreach — focuses on ROI, quick wins, and social proof from similar brands.

---

### 5. Solopreneur / Freelancer Outreach
> **Scenario:** You're a freelance developer or consultant building your client pipeline.

Use the `generic-b2b.md` template with a personal tone. The kit works even at 10 leads/week — no SaaS subscription needed.

---

## 🔌 Integrations

| Integration | What For | Setup Guide |
|-------------|----------|-------------|
| **Apollo.io** | Lead finding + contact enrichment | [docs/setup-apollo.md](docs/setup-apollo.md) |
| **LinkedIn** | Connection requests + InMail sequences | [docs/setup-linkedin.md](docs/setup-linkedin.md) (planned) |
| **WhatsApp** | Follow-up via WhatsApp Business API | [docs/setup-whatsapp.md](docs/setup-whatsapp.md) |
| **Google Sheets** | CRM pipeline tracking | [docs/crm-guide.md](docs/crm-guide.md) |
| **HubSpot** | Push contacts + track deals | [docs/crm-guide.md](docs/crm-guide.md) |
| **Airtable** | Visual CRM alternative | [docs/crm-guide.md](docs/crm-guide.md) |
| **Instantly.ai** | Email sending at scale | Import campaign.csv directly |
| **Lemlist** | Email + LinkedIn sequences | Import campaign.csv directly |

---

## 🆚 Why agent-sales-kit vs. Alternatives

| Feature | **agent-sales-kit** | Clay | Apollo (built-in) | Lemlist | Instantly |
|---------|---------------------|------|-------------------|---------|-----------|
| Monthly cost | **Free / API credits** | $149–$800/mo | $49–$149/mo | $59–$159/mo | $37–$358/mo |
| Self-hosted | ✅ | ❌ | ❌ | ❌ | ❌ |
| Open source | ✅ | ❌ | ❌ | ❌ | ❌ |
| Customizable | ✅ Fully | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited |
| AI personalization | ✅ | ✅ | ❌ | ✅ | ❌ |
| Email sequences | ✅ 5-touch | ✅ | ✅ | ✅ | ✅ |
| LinkedIn outreach | ✅ Templates | ✅ | ❌ | ✅ | ❌ |
| API access | ✅ Full | ⚠️ Partial | ✅ | ⚠️ Partial | ✅ |
| Data ownership | ✅ Yours | ❌ Vendor | ❌ Vendor | ❌ Vendor | ❌ Vendor |
| Privacy / GDPR | ✅ Full control | ⚠️ | ⚠️ | ⚠️ | ⚠️ |

> **Bottom line:** Clay is incredible but $800/month is real money. agent-sales-kit gives you 80% of the value for the cost of API credits.

---

## 📂 Repository Structure

```
agent-sales-kit/
├── README.md                    ← You are here
├── QUICK-START.md               ← 5-minute setup guide
├── requirements.txt             ← Python dependencies
├── LICENSE                      ← MIT
├── .gitignore
│
├── agents/                      ← AI agent definitions
│   ├── lead-finder.md           ← Find target companies
│   ├── contact-enricher.md      ← Enrich with emails + LinkedIn
│   ├── email-writer.md          ← Write personalized sequences
│   ├── linkedin-outreach.md     ← LinkedIn connection + InMail
│   ├── follow-up-scheduler.md   ← Multi-touch follow-up cadence
│   └── crm-manager.md           ← Pipeline tracking
│
├── templates/                   ← Ready-to-use outreach templates
│   ├── cold-email-sequences/
│   │   ├── it-infrastructure.md ← 5-touch sequence for IT companies
│   │   ├── saas-company.md      ← For selling to SaaS companies
│   │   ├── manufacturing.md     ← For manufacturing sector
│   │   └── generic-b2b.md       ← Universal B2B template
│   ├── linkedin-messages/
│   │   ├── connection-request.md ← Connection request variants
│   │   └── inmail-sequence.md    ← InMail follow-up sequence
│   └── crm-template.xlsx        ← Pre-built pipeline tracker
│
├── scripts/                     ← Working Python scripts
│   ├── setup.sh                 ← One-command environment setup
│   ├── find-leads.py            ← Apollo lead search
│   ├── enrich-contacts.py       ← Contact enrichment
│   └── run-campaign.py          ← End-to-end campaign runner
│
├── examples/                    ← Real-world worked examples
│   ├── it-infrastructure-india/ ← IT sector, India market
│   └── saas-outbound/           ← SaaS company outbound
│
└── docs/                        ← Setup and strategy guides
    ├── setup-apollo.md          ← Apollo API setup
    ├── setup-whatsapp.md        ← WhatsApp Business setup
    ├── crm-guide.md             ← CRM integration guide
    └── best-practices.md        ← Cold outreach best practices
```

---

## 📖 Documentation

- [**5-Minute Quick Start**](QUICK-START.md) — Get your first leads in 5 minutes
- [**Apollo Setup**](docs/setup-apollo.md) — Configure your free Apollo account
- [**CRM Guide**](docs/crm-guide.md) — Set up your pipeline tracker
- [**Best Practices**](docs/best-practices.md) — Avoid spam, maximize replies
- [**WhatsApp Setup**](docs/setup-whatsapp.md) — Multi-channel follow-up

---

## 🗺️ Roadmap

### v1.0 (Current)
- [x] Apollo.io lead finding
- [x] Contact enrichment with emails + LinkedIn
- [x] 5-touch email sequence templates (4 verticals)
- [x] LinkedIn outreach playbooks
- [x] End-to-end campaign runner
- [x] Google Sheets CRM template

### v1.1 (Next — Q2 2025)
- [ ] 🤖 GPT-4o / Claude personalization per contact (uses company news, LinkedIn bio)
- [ ] 📬 Direct email sending via SendGrid / Mailgun / SMTP
- [ ] 📊 Reply rate tracking and analytics
- [ ] 🔄 HubSpot two-way sync
- [ ] 🐳 Docker container for zero-setup deployment

### v1.2 (Q3 2025)
- [ ] 🌐 Web UI (Streamlit) for non-technical users
- [ ] 📱 WhatsApp follow-up automation
- [ ] 🤖 AI objection handling suggestions
- [ ] 📈 A/B testing framework for subject lines
- [ ] 🔗 Zapier / Make.com webhook triggers

### v2.0 (Vision)
- [ ] 🧠 Fully autonomous sales agent (finds → enriches → emails → responds → books meetings)
- [ ] 🎙️ AI call prep briefs from LinkedIn + company news
- [ ] 🏆 Multi-agent orchestration with role specialization

---

## 🤝 Contributing

Contributions are what make open source amazing. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/new-template`)
3. **Commit** your changes (`git commit -m 'Add manufacturing template for DACH region'`)
4. **Push** (`git push origin feature/new-template`)
5. **Open a Pull Request**

### What We Need Most
- 🌍 **Regional templates** — email sequences for specific countries/markets
- 🏭 **Vertical templates** — new industry-specific sequences (healthcare, finance, legal)
- 🔌 **Integrations** — new CRM connectors, email senders, enrichment sources
- 🐛 **Bug fixes** — always welcome
- 📖 **Documentation** — setup guides, tutorials, examples

### Code Style
- Python: follow PEP 8, type hints encouraged
- Templates: use the existing format from `agents/lead-finder.md`
- Commit messages: conventional commits format

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## ⭐ Star History

If this project saved you money or time, please star it! It helps other sales teams and developers find it.

[![Star History Chart](https://api.star-history.com/svg?repos=jarvis240615-cmyk/agent-sales-kit&type=Date)](https://star-history.com/#jarvis240615-cmyk/agent-sales-kit&Date)

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## 💬 Community & Support

- 🐛 **Bug reports:** [Open an issue](https://github.com/jarvis240615-cmyk/agent-sales-kit/issues)
- 💡 **Feature requests:** [Start a discussion](https://github.com/jarvis240615-cmyk/agent-sales-kit/discussions)
- 🤝 **Show & tell:** Share your results in Discussions!

---

<div align="center">

**Built for sales teams who'd rather be closing deals than paying for SaaS.**

*If this kit helped you, consider starring ⭐ the repo — it keeps the project alive.*

</div>
