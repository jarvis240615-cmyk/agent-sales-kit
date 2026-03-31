#!/usr/bin/env python3
"""
agent-sales-kit: Lead Finder
Find companies + decision-maker contacts using Apollo.io API

Usage:
  python scripts/find-leads.py --industry "IT infrastructure" --location "Mumbai, India"
  python scripts/find-leads.py --industry "manufacturing" --location "Pune, India" --size "51,200"
  python scripts/find-leads.py --industry "banking" --location "India" --titles "CTO,Head of IT"
"""
import argparse, json, os, sys, requests, time
from datetime import datetime

APOLLO_KEY = os.getenv("APOLLO_API_KEY")
BASE_URL = "https://api.apollo.io"

def check_api_key():
    if not APOLLO_KEY:
        print("❌ APOLLO_API_KEY not set.")
        print("   Get your free key at: https://app.apollo.io/settings/api-keys")
        print("   Then: export APOLLO_API_KEY=your_key")
        sys.exit(1)

def find_companies(industry, location, size_range, limit=25):
    headers = {"x-api-key": APOLLO_KEY, "Content-Type": "application/json"}
    payload = {
        "q_organization_keyword_tags": [industry],
        "organization_locations": [location],
        "organization_num_employees_ranges": [size_range],
        "page": 1, "per_page": min(limit, 25)
    }
    try:
        r = requests.post(f"{BASE_URL}/v1/mixed_companies/search", json=payload, headers=headers, timeout=15)
        r.raise_for_status()
        return r.json().get("organizations", [])
    except requests.exceptions.HTTPError as e:
        print(f"⚠️  API error: {e.response.status_code} — {e.response.text[:200]}")
        return []
    except Exception as e:
        print(f"⚠️  Error: {e}")
        return []

def find_contacts(domain, titles, limit=3):
    headers = {"x-api-key": APOLLO_KEY, "Content-Type": "application/json"}
    payload = {
        "q_organization_domains": domain,
        "person_titles": titles,
        "page": 1, "per_page": limit,
        "reveal_personal_emails": True
    }
    try:
        r = requests.post(f"{BASE_URL}/v1/mixed_people/search", json=payload, headers=headers, timeout=15)
        r.raise_for_status()
        return r.json().get("people", [])
    except:
        return []

def main():
    parser = argparse.ArgumentParser(
        description="🎯 agent-sales-kit: Find B2B leads with Apollo.io",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/find-leads.py --industry "IT infrastructure" --location "Mumbai, India"
  python scripts/find-leads.py --industry "manufacturing" --location "Pune" --size "51,200" --limit 50
  python scripts/find-leads.py --industry "banking" --location "India" --titles "CTO,Head of IT,VP Technology"
        """
    )
    parser.add_argument("--industry", required=True, help="Target industry")
    parser.add_argument("--location", default="India", help="Target location")
    parser.add_argument("--size", default="11,200", help="Employee range (e.g. '11,50' or '51,200')")
    parser.add_argument("--titles", default="IT Manager,CTO,Head of IT,Purchase Manager,VP Technology,Director IT")
    parser.add_argument("--limit", type=int, default=25, help="Max companies to search")
    parser.add_argument("--output", default="leads.json", help="Output file")
    args = parser.parse_args()

    check_api_key()
    titles = [t.strip() for t in args.titles.split(",")]

    print(f"\n🚀 agent-sales-kit Lead Finder")
    print(f"   Industry: {args.industry}")
    print(f"   Location: {args.location}")
    print(f"   Titles:   {', '.join(titles[:3])}{'...' if len(titles)>3 else ''}")
    print(f"   Limit:    {args.limit} companies\n")

    companies = find_companies(args.industry, args.location, args.size, args.limit)
    print(f"✅ Found {len(companies)} companies\n")

    leads = []
    for i, company in enumerate(companies):
        domain = company.get("primary_domain", "")
        name = company.get("name", domain)
        if not domain:
            continue
        print(f"  [{i+1}/{len(companies)}] {name} ({domain})")
        contacts = find_contacts(domain, titles)
        time.sleep(0.5)  # Rate limiting
        for c in contacts:
            email = c.get("email", "")
            leads.append({
                "company_name": name,
                "company_domain": domain,
                "company_size": company.get("estimated_num_employees"),
                "company_industry": company.get("industry"),
                "company_city": company.get("city", ""),
                "company_linkedin": company.get("linkedin_url", ""),
                "contact_name": f"{c.get('first_name','')} {c.get('last_name','')}".strip(),
                "contact_title": c.get("title", ""),
                "contact_email": email,
                "contact_phone": (c.get("phone_numbers") or [{}])[0].get("raw_number", ""),
                "contact_linkedin": c.get("linkedin_url", ""),
                "email_verified": bool(email and "@" in email),
                "found_at": datetime.now().isoformat()
            })
        if contacts:
            print(f"     → {len(contacts)} contacts found")

    with open(args.output, "w") as f:
        json.dump(leads, f, indent=2, ensure_ascii=False)

    verified = sum(1 for l in leads if l["email_verified"])
    print(f"\n{'─'*50}")
    print(f"✅ Total leads:          {len(leads)}")
    print(f"📧 With verified emails: {verified}")
    print(f"📁 Saved to:             {args.output}")
    print(f"{'─'*50}")
    print(f"\nNext: python scripts/run-campaign.py --leads {args.output}\n")

if __name__ == "__main__":
    main()
