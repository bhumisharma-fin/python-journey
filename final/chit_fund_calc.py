# Chit Fund Calculator
def chit_fund_analysis(amount, members, months, commission_pct=5):
    monthly_contribution = amount / months
    commission = amount * commission_pct / 100
    net_prize  = amount - commission
    dividend   = commission / members
    print(f"CHIT FUND ANALYSIS")
    print(f"Chit Value:          Rs {amount:,}")
    print(f"Members:             {members}")
    print(f"Duration:            {months} months")
    print(f"Monthly Contribution: Rs {monthly_contribution:,}")
    print(f"Commission ({commission_pct}%):    Rs {commission:,}")
    print(f"Net Prize Money:     Rs {net_prize:,}")
    print(f"Monthly Dividend:    Rs {dividend:,}/member")
    total_paid = monthly_contribution * months
    print(f"\nIf you win in month 1:")
    print(f"  Get Rs {net_prize:,}, Pay Rs {total_paid:,} total")
    print(f"  Effective cost: Rs {total_paid - net_prize:,}")
    print(f"If you win in last month:")
    print(f"  Effective saving: Rs {net_prize - total_paid:,}")

chit_fund_analysis(100000, 10, 10)
