# Data Cleaning - Messy data ko clean karna
# Finance me: bank statements, CSV exports often messy hote hain

import pandas as pd
import numpy as np

# Messy data simulate karo
raw_data = {
    "Date":        ["01-01-2026", "2026-02-01", "March 1 2026", "2026/04/01", None],
    "Description": ["  ZOMATO  ", "amazon.in", None, "NETFLIX INDIA", "UPI-PHONEPE"],
    "Amount":      ["Rs 350.00", "-1299", "599.50", "  -649  ", None],
    "Category":    ["Food", "Shopping", "Entertainment", None, "Transfer"],
}
df = pd.DataFrame(raw_data)

print("BEFORE CLEANING:")
print(df)
print(f"\nMissing values:\n{df.isnull().sum()}")

# 1. Remove rows with missing Amount
df = df.dropna(subset=["Amount"])

# 2. Clean Amount column
df["Amount"] = df["Amount"].astype(str).str.replace("Rs", "").str.strip().astype(float)

# 3. Clean Description
df["Description"] = df["Description"].fillna("Unknown").str.strip().str.title()

# 4. Fill missing Category
df["Category"] = df["Category"].fillna("Uncategorized")

# 5. Drop rows with no Date
df = df.dropna(subset=["Date"])

print("\nAFTER CLEANING:")
print(df)
print(f"\nData types:\n{df.dtypes}")
