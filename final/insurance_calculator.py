# Life Insurance Need Calculator
def insurance_need(annual_income, years_to_retire, existing_cover=0, liabilities=0, savings=0):
    """
    Human Life Value (HLV) method
    How much life insurance do you actually need?
    """
    future_income = annual_income * years_to_retire
    net_need = future_income + liabilities - savings - existing_cover
    recommended = max(net_need, 0)
    print(f"LIFE INSURANCE CALCULATOR")
    print(f"=" * 45)
    print(f"Annual Income:      Rs {annual_income:,}")
    print(f"Years to Retire:    {years_to_retire}")
    print(f"Future Income Loss: Rs {future_income:,}")
    print(f"Existing Liabilities: Rs {liabilities:,}")
    print(f"Existing Savings:   Rs {savings:,}")
    print(f"Existing Cover:     Rs {existing_cover:,}")
    print(f"=" * 45)
    print(f"Recommended Cover:  Rs {recommended:,}")
    times = recommended / annual_income
    print(f"Thats {times:.0f}x your annual income")
    if times < 10:
        print("⚠️  Consider increasing your life cover!")
    else:
        print("✅ Good coverage!")

insurance_need(
    annual_income=900000,
    years_to_retire=30,
    existing_cover=5000000,
    liabilities=2000000,
    savings=1500000
)
