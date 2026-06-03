# Pandas Advanced - Real data analysis techniques

import pandas as pd

# Sample transaction data
data = {
    "Date":     ["2026-01","2026-01","2026-02","2026-02","2026-03","2026-03","2026-03"],
    "Category": ["Food","Transport","Food","Shopping","Food","Utilities","Transport"],
    "Amount":   [3500, 1200, 4200, 8000, 2800, 2200, 1500],
    "Mode":     ["UPI","Cash","UPI","Card","UPI","NetBanking","UPI"],
}
df = pd.DataFrame(data)

print("RAW DATA:")
print(df.to_string(index=False))

# GroupBy - Category wise total
print("\nCATEGORY WISE SPENDING:")
category_summary = df.groupby("Category")["Amount"].agg(["sum","mean","count"])
category_summary.columns = ["Total", "Average", "Transactions"]
print(category_summary.sort_values("Total", ascending=False))

# Month wise spending
print("\nMONTH WISE TOTAL:")
print(df.groupby("Date")["Amount"].sum())

# Payment mode analysis
print("\nPAYMENT MODE USAGE:")
print(df.groupby("Mode")["Amount"].sum().sort_values(ascending=False))

# Pivot table
print("\nPIVOT TABLE (Month x Category):")
pivot = df.pivot_table(values="Amount", index="Date", columns="Category", aggfunc="sum", fill_value=0)
print(pivot)
