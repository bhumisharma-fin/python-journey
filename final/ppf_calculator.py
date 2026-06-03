# PPF - Public Provident Fund Calculator
def ppf_calculator(yearly_deposit, rate, years=15):
    balance = 0
    total_deposited = 0
    print(f"PPF Calculator - Rs {yearly_deposit:,}/year @ {rate}%")
    print(f"{Year:<6} {Deposited:>12} {Balance:>14} {Interest:>12}")
    print("-" * 46)
    for year in range(1, years+1):
        interest = (balance + yearly_deposit) * rate / 100
        balance  = balance + yearly_deposit + interest
        total_deposited += yearly_deposit
        print(f"  {year:<4} Rs {yearly_deposit:>9,} Rs {balance:>11,.0f} Rs {interest:>9,.0f}")
    profit = balance - total_deposited
    print(f"\nTotal Deposited: Rs {total_deposited:,}")
    print(f"Maturity Value:  Rs {balance:,.0f}")
    print(f"Total Profit:    Rs {profit:,.0f}")

ppf_calculator(150000, 7.1)
