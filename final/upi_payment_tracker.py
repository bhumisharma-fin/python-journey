# UPI Payment Tracker
from collections import defaultdict

payments = [
    ("2026-06-01", "Zomato",     349,  "Food"),
    ("2026-06-01", "Uber",       180,  "Transport"),
    ("2026-06-02", "Amazon",    1299,  "Shopping"),
    ("2026-06-03", "Swiggy",     250,  "Food"),
    ("2026-06-04", "BookMyShow", 450,  "Entertainment"),
    ("2026-06-05", "BigBasket", 2100,  "Groceries"),
    ("2026-06-06", "Ola",        220,  "Transport"),
    ("2026-06-07", "Myntra",    1800,  "Shopping"),
    ("2026-06-08", "Zomato",     420,  "Food"),
    ("2026-06-09", "Netflix",    649,  "Entertainment"),
]

total = sum(p[2] for p in payments)
by_category = defaultdict(int)
by_app      = defaultdict(int)

for date, app, amount, cat in payments:
    by_category[cat] += amount
    by_app[app]      += amount

print(f"UPI SPENDING TRACKER")
print(f"Total Spent: Rs {total:,}\n")

print("BY CATEGORY:")
for cat, amt in sorted(by_category.items(), key=lambda x: -x[1]):
    print(f"  {cat:<15} Rs {amt:,}")

print("\nBY APP:")
for app, amt in sorted(by_app.items(), key=lambda x: -x[1]):
    print(f"  {app:<15} Rs {amt:,}")
