def emi(p, r, n):
    r = r / 12 / 100
    return p * r * (1+r)**n / ((1+r)**n - 1)

banks = [
    ("SBI",        7.5,  240),
    ("HDFC",       8.0,  240),
    ("ICICI",      8.25, 240),
    ("Axis",       7.75, 180),
]
principal = 2000000
print(f"Loan: Rs {principal:,}")
print(f"{Bank:<10} {Rate:>6} {Months:>8} {EMI:>12} {Total:>14} {Interest:>12}")
for bank, rate, months in banks:
    e = emi(principal, rate, months)
    total = e * months
    interest = total - principal
    print(f"{bank:<10} {rate:>5.2f}% {months:>8} Rs {e:>9,.0f} Rs {total:>11,.0f} Rs {interest:>9,.0f}")
