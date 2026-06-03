# Multiple Income Streams Tracker
income_streams = [
    {"source": "Primary Job",    "type": "Active",  "monthly": 75000, "stability": "High"},
    {"source": "Freelancing",    "type": "Active",  "monthly": 15000, "stability": "Medium"},
    {"source": "YouTube",        "type": "Passive", "monthly":  3000, "stability": "Low"},
    {"source": "Dividend",       "type": "Passive", "monthly":  2500, "stability": "Medium"},
    {"source": "Rental Income",  "type": "Passive", "monthly": 12000, "stability": "High"},
    {"source": "SIP Returns",    "type": "Passive", "monthly":  5000, "stability": "Medium"},
]
total = sum(s["monthly"] for s in income_streams)
active = sum(s["monthly"] for s in income_streams if s["type"] == "Active")
passive = sum(s["monthly"] for s in income_streams if s["type"] == "Passive")

print("INCOME DIVERSIFICATION")
print("=" * 55)
for s in income_streams:
    pct = s["monthly"] / total * 100
    bar = "█" * int(pct / 3)
    print(f"  {s[source]:<20} {s[type]:<8} Rs {s[monthly]:>6,} ({pct:>4.1f}%) {bar}")

print("=" * 55)
print(f"  Total Monthly: Rs {total:,}")
print(f"  Active Income: Rs {active:,} ({active/total*100:.0f}%)")
print(f"  Passive Income: Rs {passive:,} ({passive/total*100:.0f}%)")
print(f"\n  Goal: Passive > Active income = Financial Freedom!")
