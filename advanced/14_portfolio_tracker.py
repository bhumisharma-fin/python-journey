# Portfolio Tracker - Apna investment track karo

portfolio = [
    # (Stock, Buy Price, Quantity, Current Price)
    ("Reliance",  2400, 10, 2650),
    ("TCS",       3200, 5,  3450),
    ("Infosys",   1400, 15, 1520),
    ("HDFC Bank", 1600, 8,  1580),
    ("Wipro",      450, 20,  480),
]

def portfolio_summary(portfolio):
    print(f"\n{=*70}")
    print(f"  PORTFOLIO TRACKER")
    print(f"{=*70}")
    print(f"  {Stock:<12} {Buy:>8} {Qty:>5} {Curr:>8} {Invested:>12} {Value:>12} {P