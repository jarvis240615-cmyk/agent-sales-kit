# CRM Manager Agent

## Pipeline Stages

```
Prospect → Contacted → Engaged → Meeting → Proposal → Negotiation → Won ✅
                                                                  → Lost ❌
```

## Lead JSON Schema

```json
{
  "id": "unique-id",
  "company": "Company Name",
  "domain": "company.com",
  "contact_name": "First Last",
  "contact_title": "IT Manager",
  "contact_email": "email@company.com",
  "contact_phone": "+91-XXXXXXXXXX",
  "contact_linkedin": "https://linkedin.com/in/...",
  "status": "contacted",
  "priority": "high",
  "deal_value": 1800000,
  "next_action": "Follow up on proposal",
  "next_action_date": "2026-04-05",
  "last_contact_date": "2026-03-31",
  "notes": "Interested in structured cabling. Decision in Q2.",
  "source": "Apollo / LinkedIn / Referral / Inbound",
  "created_at": "2026-03-31T00:00:00"
}
```

## Weekly Review Checklist
- [ ] Any overdue follow-ups?
- [ ] Any proposals pending >7 days?
- [ ] Any leads in "Engaged" for >14 days without a meeting booked?
- [ ] Pipeline value this week vs last week
- [ ] Win/loss ratio this month

## KPIs to Track

| Metric | Target | How to measure |
|--------|--------|----------------|
| Email reply rate | >8% | Replies / Sent |
| LinkedIn acceptance | >35% | Accepts / Sent |
| Meeting rate | >15% of replies | Meetings / Replies |
| Proposal-to-close | >25% | Won / Proposals |
| Avg deal size | Track monthly | Total revenue / Deals |
| Sales cycle | <45 days | Date contact → Date won |

## CRM File Location
`~/.agent-sales-kit/crm.json` — auto-created on first run
