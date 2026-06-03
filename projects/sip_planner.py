# SIP Retirement Planner
def sip_future_value(monthly, rate, years):
    r = rate / 100 / 12
    n = years * 12
    return monthly * ((1 + r)**n - 1) / r * (1 + r)

def retirement_planner(current_age, retire_age, monthly_expense, inflation=6, sip_return=12):
    invest_years = retire_age - current_age
    retire_years = 85 - retire_age
    inflated_expense = monthly_expense * (1 + inflation/100) ** invest_years
    corpus_needed = inflated_expense * 12 * retire_years
    monthly_sip = corpus_needed / (((1 + sip_return/100/12)**( invest_years*12) - 1) / (sip_return/100/12) * (1 + sip_return/100/12))

    print(f"\nRETIREMENT PLANNER")
    print(f"Current Age:      {current_age}")
    print(f"Retirement Age:   {retire_age}")
    print(f"Years to invest:  {invest_years}")
    print(f"Monthly Expense:  Rs {monthly_expense:,}")
    print(f"Future Expense:   Rs {inflated_expense:,.0f}/month")
    print(f"Corpus Needed:    Rs {corpus_needed:,.0f}")
    print(f"Monthly SIP:      Rs {monthly_sip:,.0f}")

retirement_planner(25, 60, 50000)
