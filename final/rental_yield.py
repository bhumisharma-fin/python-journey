# Rental Yield Calculator - Property investment
def rental_yield(property_value, monthly_rent, annual_expenses=0):
    annual_rent = monthly_rent * 12
    net_income = annual_rent - annual_expenses
    gross_yield = annual_rent / property_value * 100
    net_yield   = net_income / property_value * 100
    print(f"RENTAL YIELD ANALYSIS")
    print(f"Property Value:    Rs {property_value:,}")
    print(f"Monthly Rent:      Rs {monthly_rent:,}")
    print(f"Annual Rent:       Rs {annual_rent:,}")
    print(f"Annual Expenses:   Rs {annual_expenses:,}")
    print(f"Net Income:        Rs {net_income:,}")
    print(f"Gross Yield:       {gross_yield:.2f}%")
    print(f"Net Yield:         {net_yield:.2f}%")
    if net_yield >= 3:
        print("✅ Good rental yield!")
    else:
        print("⚠️  Low yield. Consider price negotiation.")

# Mumbai apartment example
rental_yield(
    property_value=8500000,
    monthly_rent=28000,
    annual_expenses=50000
)
