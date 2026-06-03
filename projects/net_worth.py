# Net Worth = Assets - Liabilities
assets = {
    "Savings Account":  150000,
    "Fixed Deposits":   300000,
    "Mutual Funds":     250000,
    "Stocks":           180000,
    "Gold":              85000,
    "PPF":              120000,
}
liabilities = {
    "Home Loan":       1500000,
    "Car Loan":         350000,
    "Credit Card":       25000,
    "Personal Loan":    100000,
}
total_assets = sum(assets.values())
total_liab   = sum(liabilities.values())
net_worth    = total_assets - total_liab

print("ASSETS:")
for k, v in assets.items():
    print(f"  {k:<20} Rs {v:>10,}")
print(f"  {TOTAL:<20} Rs {total_assets:>10,}")

print("\nLIABILITIES:")
for k, v in liabilities.items():
    print(f"  {k:<20} Rs {v:>10,}")
print(f"  {TOTAL:<20} Rs {total_liab:>10,}")

print(f"\nNET WORTH: Rs {net_worth:,}")
print(f"Status: {Positive!