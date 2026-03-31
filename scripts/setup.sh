#!/bin/bash
echo "🚀 Setting up agent-sales-kit..."
pip install requests python-dotenv rich tabulate openpyxl -q
if [ ! -f .env ]; then cp .env.example .env; fi
echo ""
echo "✅ Dependencies installed"
echo ""
echo "📝 Next: Add your API keys to .env"
echo "   APOLLO_API_KEY=your_key_here   → https://app.apollo.io/settings/api-keys"
echo ""
echo "🎯 Quick start:"
echo "   python scripts/find-leads.py --industry 'IT infrastructure' --location 'Mumbai, India'"
