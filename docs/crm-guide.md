# CRM Guide — Track Your Pipeline

## Option 1: Built-in JSON CRM (Zero Setup)

The simplest option — a JSON file that tracks all leads.

```bash
# Initialize CRM
python scripts/crm.py init

# Add a lead
python scripts/crm.py add --company "Tata Steel" --contact "Ramesh Kumar" \
  --email ramesh@tatasteel.com --status contacted --priority high

# View pipeline
python scripts/crm.py pipeline

# Update status
python scripts/crm.py update --id 1 --status meeting --notes "Call scheduled for Apr 5"
```

CRM file stored at: `~/.agent-sales-kit/crm.json`

## Option 2: Google Sheets Sync

1. Create a Google Sheet with columns:
   `ID | Company | Contact | Email | Phone | LinkedIn | Status | Priority | Deal Value | Next Action | Notes | Last Updated`

2. Install: `pip install gspread google-auth`

3. Export leads to Sheets:
```python
import gspread
from google.oauth2.service_account import Credentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("Sales Pipeline").sheet1
# Write your leads.json data to the sheet
```

## Pipeline Stages

| Stage | Meaning | Avg time |
|-------|---------|----------|
| `prospect` | Identified, not contacted | — |
| `contacted` | Email/LinkedIn sent | Day 0 |
| `engaged` | Replied, showing interest | Day 3-7 |
| `meeting` | Call/demo scheduled | Day 7-14 |
| `proposal` | Quotation sent | Day 14-21 |
| `negotiation` | Price/scope discussion | Day 21-35 |
| `won` | PO received | Day 30-60 |
| `lost` | Dead deal | — |

## Weekly Review (15 mins every Monday)
1. Any overdue follow-ups? → Act today
2. Any proposals pending >7 days? → Follow up
3. Any meetings not confirmed? → Confirm
4. Pipeline value vs last week → Track trend
5. New leads to add this week → Plan outreach
