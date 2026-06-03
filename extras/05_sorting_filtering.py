# Sorting and Filtering - Data organize karna

transactions = [
    {"date": "2026-06-03", "amount": 350,  "desc": "Zomato",   "cat": "Food"},
    {"date": "2026-06-01", "amount": 1299, "desc": "Amazon",   "cat": "Shopping"},
    {"date": "2026-06-02", "amount": 180,  "desc": "Uber",     "cat": "Transport"},
    {"date": "2026-06-04", "amount": 649,  "desc": "Netflix",  "cat": "Entertainment"},
    {"date": "2026-06-05", "amount": 2500, "desc": "Groceries","cat": "Food"},
]

# Sort by amount highest first
by_amount = sorted(transactions, key=lambda x: x["amount"], reverse=True)
print("Top expenses:")
for t in by_amount[:3]:
    print(f"  {t["desc"]:<12} Rs {t["amount"]}")

# Filter food only
food = [t for t in transactions if t["cat"] == "Food"]
print(f"\nFood spending: Rs {sum(t["amount"] for t in food)}")

# Group by category
from collections import defaultdict
by_cat = defaultdict(int)
for t in transactions:
    by_cat[t["cat"]] += t["amount"]

print("\nBy Category:")
for cat, total in sorted(by_cat.items(), key=lambda x: -x[1]):
    print(f"  {cat:<15} Rs {total}")

total = sum(t["amount"] for t in transactions)
print(f"\nTotal: Rs {total}")
