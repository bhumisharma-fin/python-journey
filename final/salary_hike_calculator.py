# Salary Hike & Offer Comparison
def salary_analysis(ctc):
    basic = ctc * 0.40
    hra   = basic * 0.50
    pf_employee = basic * 0.12
    pf_employer = basic * 0.12
    special_allowance = ctc - basic - hra - pf_employer
    gross_monthly = (basic + hra + special_allowance) / 12
    net_monthly = gross_monthly - pf_employee/12
    print(f"CTC: Rs {ctc:,}/year")
    print(f"  Basic:             Rs {basic/12:>10,.0f}/month")
    print(f"  HRA:               Rs {hra/12:>10,.0f}/month")
    print(f"  Special Allowance: Rs {special_allowance/12:>10,.0f}/month")
    print(f"  PF Deduction:      Rs {pf_employee/12:>10,.0f}/month")
    print(f"  In-hand (approx):  Rs {net_monthly:>10,.0f}/month")

def compare_offers(current_ctc, offer_ctc, offer_company):
    hike = (offer_ctc - current_ctc) / current_ctc * 100
    monthly_diff = (offer_ctc - current_ctc) / 12
    print(f"\nOFFER COMPARISON")
    print(f"Current CTC:  Rs {current_ctc:,}")
    print(f"{offer_company}: Rs {offer_ctc:,}")
    print(f"Hike:         {hike:.1f}%")
    print(f"Extra/month:  Rs {monthly_diff:,.0f}")

salary_analysis(1200000)
compare_offers(1200000, 1800000, "New Company")
