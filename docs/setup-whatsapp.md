# WhatsApp Business API Setup (via Maton.ai)

No Meta approval required. Maton.ai manages the OAuth flow.

## Step 1 — Create Maton Account
1. Go to https://maton.ai
2. Sign up (free tier available)
3. Dashboard → API Keys → Create new key
4. Copy your `MATON_API_KEY`

## Step 2 — Connect WhatsApp Business
1. Maton Dashboard → Integrations → WhatsApp Business
2. Click "Connect" → Follow OAuth flow
3. Authorize your WhatsApp Business account
4. Note your `PHONE_NUMBER_ID` from the dashboard

## Step 3 — Configure
```bash
export MATON_API_KEY=your_maton_key_here
export WHATSAPP_PHONE_ID=your_phone_number_id
```

## Step 4 — Send a Test Message
```python
import urllib.request, os, json

data = json.dumps({
    'messaging_product': 'whatsapp',
    'to': '919876543210',  # include country code, no +
    'type': 'text',
    'text': {'body': 'Hello from agent-sales-kit!'}
}).encode()

req = urllib.request.Request(
    f'https://gateway.maton.ai/whatsapp-business/v21.0/{os.environ["WHATSAPP_PHONE_ID"]}/messages',
    data=data, method='POST'
)
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.load(urllib.request.urlopen(req)))
```

## WhatsApp vs Email for Outreach
- WhatsApp open rates: 85-95% (vs email: 25-40%)
- Response rates: 30-45% (vs email: 5-12%)
- Best for: Follow-ups after email, meeting confirmations, quick questions
- Not for: First cold contact (can feel intrusive)

## Recommended Flow
1. Email sequence (5 touches)
2. If no reply after Email 3 → WhatsApp follow-up
3. Keep WhatsApp messages short (under 100 words)
4. Always identify yourself: "Hi [Name], this is [Your Name] from [Company]..."
