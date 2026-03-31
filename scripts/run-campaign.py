#!/usr/bin/env python3
"""
agent-sales-kit: Campaign Runner
Generate personalized email campaigns from leads.json

Usage:
  python scripts/run-campaign.py --leads leads.json --template it-infrastructure
  python scripts/run-campaign.py --leads leads.json --output my-campaign.csv
"""
import argparse, json, csv, os
from datetime import datetime

TEMPLATES = {
    "it-infrastructure": {
        "subject_1": "{{company}} network infrastructure — quick question",
        "body_1": """Hi {{first_name}},

Noticed {{company}} has been growing. As teams scale, most IT managers hit the same wall: cabling that wasn't built to handle it, Wi-Fi dead zones, or SD-WAN that's underdelivering.

We help enterprise IT teams solve exactly this — without ripping and replacing everything.

Worth a 15-min call this week?

Best,
{{sender_name}}""",
        "subject_2": "How [Similar Company] cut network downtime by 60%",
        "body_2": """Hi {{first_name}},

Quick follow-up — we recently helped a similar company cut network downtime by 60% in 6 weeks with a structured cabling + SD-WAN upgrade.

Is {{company}} facing similar challenges? Happy to share the case study.

{{sender_name}}""",
        "subject_3": "Free IT infrastructure audit for {{company}}",
        "body_3": """Hi {{first_name}},

Offering a complimentary 2-hour IT infrastructure audit for {{company}} — we map your setup, identify gaps, give you a prioritised action plan. No pitch, just value.

Interested?

{{sender_name}}""",
    },
    "generic": {
        "subject_1": "Quick question about {{company}}",
        "body_1": """Hi {{first_name}},

I came across {{company}} and noticed [relevant observation].

We help [target companies] with [problem]. Would it make sense to connect this week?

{{sender_name}}""",
        "subject_2": "Following up — {{company}}",
        "body_2": """Hi {{first_name}},

Just following up on my last message. Happy to share a relevant case study if helpful.

{{sender_name}}""",
        "subject_3": "Last note — {{company}}",
        "body_3": """Hi {{first_name}},

Last follow-up from my end. If timing isn't right, no worries — feel free to reach out when it makes sense.

{{sender_name}}""",
    }
}

def personalize(text, lead, sender_name="[Your Name]"):
    return (text
        .replace("{{first_name}}", lead.get("contact_name", "").split()[0] if lead.get("contact_name") else "there")
        .replace("{{company}}", lead.get("company_name", "your company"))
        .replace("{{title}}", lead.get("contact_title", ""))
        .replace("{{sender_name}}", sender_name)
    )

def main():
    parser = argparse.ArgumentParser(description="🚀 Generate personalized email campaign")
    parser.add_argument("--leads", default="leads.json", help="Input leads file")
    parser.add_argument("--template", default="generic", choices=list(TEMPLATES.keys()))
    parser.add_argument("--sender", default="[Your Name]", help="Your name")
    parser.add_argument("--output", default="campaign.csv", help="Output CSV file")
    args = parser.parse_args()

    with open(args.leads) as f:
        leads = json.load(f)

    template = TEMPLATES[args.template]
    rows = []

    for lead in leads:
        if not lead.get("contact_email"):
            continue
        rows.append({
            "Name": lead.get("contact_name", ""),
            "Title": lead.get("contact_title", ""),
            "Company": lead.get("company_name", ""),
            "Email": lead.get("contact_email", ""),
            "LinkedIn": lead.get("contact_linkedin", ""),
            "Phone": lead.get("contact_phone", ""),
            "Subject_1": personalize(template["subject_1"], lead, args.sender),
            "Body_1": personalize(template["body_1"], lead, args.sender),
            "Subject_2": personalize(template["subject_2"], lead, args.sender),
            "Body_2": personalize(template["body_2"], lead, args.sender),
            "Subject_3": personalize(template["subject_3"], lead, args.sender),
            "Body_3": personalize(template["body_3"], lead, args.sender),
            "Status": "ready",
            "Generated_at": datetime.now().isoformat()
        })

    with open(args.output, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys() if rows else [])
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n🎯 Campaign Ready")
    print(f"{'─'*40}")
    print(f"   Total leads:    {len(leads)}")
    print(f"   With emails:    {len(rows)}")
    print(f"   Template:       {args.template}")
    print(f"   Output:         {args.output}")
    print(f"   Est. reply rate: 5-12% (industry avg: 3-5%)")
    print(f"{'─'*40}")
    print(f"\n✅ Import {args.output} into Instantly, Lemlist, or Gmail\n")

if __name__ == "__main__":
    main()
