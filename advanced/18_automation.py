# Automation - Repetitive finance tasks automate karo

import os
import json
from datetime import datetime

# Auto-generate monthly report
def generate_monthly_report(month, income, expenses):
    total_expense = sum(expenses.values())
    savings = income - total_expense
    savings_rate = savings / income * 100

    report = {
        "month": month,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "income": income,
        "total_expense": total_expense,
        "savings": savings,
        "savings_rate": round(savings_rate, 2),
        "expense_breakdown": expenses,
        "status": "healthy" if savings_rate >= 20 else "needs_attention",
    }
    return report

def save_report(report):
    filename = f"report_{report[\"month\"]}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    print(f"Report saved: {filename}")
    return filename

def print_report(report):
    print(f"\n{=*45}")
    print(f"  MONTHLY REPORT - {report[month]}")
    print(f"  Generated: {report[generated_at]}")
    print(f"{=*45}")
    print(f"  Income:       Rs {report[income]:,}")
    print(f"  Expenses:     Rs {report[total_expense]:,}")
    print(f"  Savings:      Rs {report[savings]:,}")
    print(f"  Savings Rate: {report[savings_rate]}%")
    print(f"  Status:       {report[status].upper()}")
    print(f"{=*45}")

# Generate report
expenses = {"Rent": 15000, "Food": 7000, "Transport": 3000, "Other": 5000}
report = generate_monthly_report("2026-06", 60000, expenses)
print_report(report)
filename = save_report(report)

# Cleanup
if os.path.exists(filename):
    os.remove(filename)
