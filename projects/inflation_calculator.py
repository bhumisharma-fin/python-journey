# Inflation Calculator - Paison ki value time ke saath
def inflation_impact(amount, rate, years):
    future_value = amount * (1 + rate/100) ** years
    purchasing_power = amount / (1 + rate/100) ** years
    print(f"\nInflation Impact Analysis")
    print(f"Current Amount:     Rs {amount:,}")
    print(f"Inflation Rate:     {rate}% per year")
    print(f"Time Period:        {years} years")
    print(f"Future Cost:        Rs {future_value:,.0f}")
    print(f"Purchasing Power:   Rs {purchasing_power:,.0f}")
    loss = amount - purchasing_power
    print(f"Value Lost:         Rs {loss:,.0f} ({loss/amount*100:.1f}%)")

# Real examples
print("Rs 1 Lakh ki value:")
inflation_impact(100000, 6, 10)
inflation_impact(100000, 6, 20)

print("\nMonthly expense ka future cost:")
inflation_impact(50000, 6, 25)
