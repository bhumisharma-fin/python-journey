# Budget Visualizer - Text based chart
def budget_bar_chart(income, expenses):
    total_expense = sum(expenses.values())
    savings = income - total_expense
    all_items = dict(expenses)
    all_items["Savings"] = savings
    print(f"\nBUDGET BREAKDOWN (Income: Rs {income:,})")
    print("=" * 55)
    for item, amount in sorted(all_items.items(), key=lambda x: -x[1]):
        pct = amount / income * 100
        bar = "█" * int(pct / 2)
        label = "💰" if item == "Savings" else "💸"
        print(f"  {label} {item:<18} {bar:<25} {pct:>5.1f}%  Rs {amount:,}")
    print("=" * 55)
    if savings > 0:
        print(f"  ✅ Saving {savings/income*100:.1f}% of income!")
    else:
        print(f"  ⚠️  Overspending by Rs {abs(savings):,}!")

budget_bar_chart(80000, {
    "Rent": 22000, "Food": 9000, "Transport": 4000,
    "Shopping": 6000, "Entertainment": 3000, "Utilities": 3000,
    "Investment": 10000
})
