# JSON - Web APIs se data aata hai JSON format me

import json, os

portfolio = {
    "owner": "Bhumi Sharma",
    "stocks": [
        {"symbol": "RELIANCE", "qty": 10, "buy_price": 2400},
        {"symbol": "TCS",      "qty": 5,  "buy_price": 3200},
    ],
    "total_invested": 56000
}

# Save to file
with open("portfolio.json", "w") as f:
    json.dump(portfolio, f, indent=2)
print("Saved!")

# Load from file
with open("portfolio.json", "r") as f:
    loaded = json.load(f)

print(f"Owner: {loaded["owner"]}")
print(f"Stocks: {len(loaded["stocks"])}")
for s in loaded["stocks"]:
    print(f"  {s["symbol"]}: {s["qty"]} @ Rs {s["buy_price"]}")

# From API string
api = "{\"price\": 2650.45, \"change\": \"+0.89%\"}"
data = json.loads(api)
print(f"Live Price: Rs {data["price"]}")

os.remove("portfolio.json")
