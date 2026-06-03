# Python Finance Cheat Sheet

## Data Types
```python
x = 10          # int
y = 10.5        # float  
name = "Bhumi"  # str
lst = [1,2,3]   # list
d = {"a": 1}    # dict
```

## String Formatting
```python
salary = 75000
print(f"Rs {salary:,}")       # Rs 75,000
print(f"{8.567:.2f}%")        # 8.57%
print(f"{5000:+,}")           # +5,000
```

## List Quick Ops
```python
total   = sum(amounts)
highest = max(amounts)
lowest  = min(amounts)
avg     = sum(amounts) / len(amounts)
top3    = sorted(amounts, reverse=True)[:3]
big     = [x for x in amounts if x > 1000]
```

## Dict Quick Ops
```python
value = d.get("key", "default")
pairs = list(d.items())
filtered = {k:v for k,v in d.items() if v > 0}
```

## Pandas Quick Ref
```python
df = pd.read_csv("file.csv")
df.head()                       # First 5 rows
df.describe()                   # Stats
df[df["amount"] > 1000]         # Filter
df.groupby("category").sum()    # Group
df.sort_values("amount")        # Sort
df["new"] = df["a"] + df["b"]  # New column
df.to_excel("output.xlsx")      # Save Excel
```

## Finance Formulas
```python
# Simple Interest
si = P * R * T / 100

# Compound Interest  
ci = P * (1 + R/100/n)**(n*T) - P

# EMI
r = annual_rate / 12 / 100
emi = P * r * (1+r)**n / ((1+r)**n - 1)

# SIP Future Value
fv = monthly * ((1+r)**n - 1) / r * (1+r)

# CAGR
cagr = (end/start)**(1/years) - 1

# % Change
pct = (new - old) / old * 100
```

## Install Libraries
```bash
pip install numpy pandas matplotlib openpyxl yfinance
```
