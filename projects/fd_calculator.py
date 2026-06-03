# Fixed Deposit Calculator
def fd_calculator(principal, rate, years, compounding="quarterly"):
    n = {"monthly": 12, "quarterly": 4, "yearly": 1}[compounding]
    r = rate / 100
    amount = principal * (1 + r/n) ** (n * years)
    interest = amount - principal
    print(f"\nFixed Deposit Summary")
    print(f"Principal:    Rs {principal:,}")
    print(f"Rate:         {rate}% per year")
    print(f"Duration:     {years} years")
    print(f"Compounding:  {compounding}")
    print(f"Maturity:     Rs {amount:,.2f}")
    print(f"Interest:     Rs {interest:,.2f}")
    print(f"Effective Rate: {(amount/principal-1)*100:.2f}%")

fd_calculator(100000, 7.5, 3)
fd_calculator(500000, 7.1, 5, "monthly")
