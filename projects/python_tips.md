# Python Tips for Finance Professionals 💡

## Quick Reference

### Reading CSV (Bank Statement)
```python
import pandas as pd
df = pd.read_csv("statement.csv")
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
print(df.groupby("Category")["Amount"].sum())
```

### Date Handling
```python
from datetime import datetime
date = datetime.strptime("01-06-2026", "%d-%m-%Y")
print(date.strftime("%B %Y"))  # June 2026
```

### Quick EMI
```python
p, r, n = 500000, 8.5/12/100, 60
emi = p * r * (1+r)**n / ((1+r)**n - 1)
print(f"EMI: Rs {emi:,.0f}")
```

### Percentage Change
```python
old, new = 100, 115
change = (new - old) / old * 100
print(f"Change: {change:+.1f}%")
```

## Common Finance Formulas

| Formula | Python Code |
|---------|------------|
| Simple Interest | `si = p * r * t / 100` |
| Compound Interest | `ci = p * (1 + r/n)**(n*t) - p` |
| CAGR | `cagr = (end/start)**(1/years) - 1` |
| ROI | `roi = (gain - cost) / cost * 100` |

## Recommended Libraries
- `pandas` - Data analysis
- `numpy` - Math operations  
- `matplotlib` - Charts
- `yfinance` - Stock data
- `openpyxl` - Excel files
