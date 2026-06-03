# Generators - Memory efficient processing
# Finance me: large CSV, transaction streams

def emi_schedule(principal, annual_rate, months):
    """Generate EMI schedule month by month"""
    r = annual_rate / 12 / 100
    emi = principal * r * (1+r)**months / ((1+r)**months - 1)
    balance = principal
    for month in range(1, months + 1):
        interest = balance * r
        principal_paid = emi - interest
        balance -= principal_paid
        yield {
            "month": month,
            "emi": round(emi, 2),
            "interest": round(interest, 2),
            "principal": round(principal_paid, 2),
            "balance": round(max(balance, 0), 2)
        }

print(f"EMI Schedule - Rs 5 lakh loan @ 8.5% for 5 years")
print(f"{"Month":>6} {"EMI":>10} {"Interest":>10} {"Principal":>10} {"Balance":>12}")
print("-" * 50)

schedule = list(emi_schedule(500000, 8.5, 60))
# Show first 3 and last 3 months
for row in schedule[:3] + schedule[-3:]:
    if row["month"] == 4:
        print("  ...")
    print(f"  {row["month"]:>4} Rs {row["emi"]:>8,} Rs {row["interest"]:>8,.0f} Rs {row["principal"]:>8,.0f} Rs {row["balance"]:>10,}")

total_interest = sum(r["interest"] for r in schedule)
print(f"\nTotal Interest Paid: Rs {total_interest:,.0f}")
