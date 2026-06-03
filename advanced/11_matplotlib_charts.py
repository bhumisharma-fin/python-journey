# Matplotlib - Python me charts banana
# pip install matplotlib

import matplotlib
matplotlib.use("Agg")  # No display needed
import matplotlib.pyplot as plt

# Monthly expense data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
income  = [50000, 52000, 50000, 55000, 53000, 58000]
expense = [35000, 38000, 33000, 40000, 36000, 39000]
savings = [i - e for i, e in zip(income, expense)]

# Line chart - Income vs Expense
plt.figure(figsize=(10, 5))
plt.plot(months, income,  marker="o", label="Income",  color="green")
plt.plot(months, expense, marker="o", label="Expense", color="red")
plt.plot(months, savings, marker="o", label="Savings", color="blue",  linestyle="--")
plt.title("Monthly Income vs Expense")
plt.xlabel("Month")
plt.ylabel("Amount (Rs)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("income_expense.png")
print("Chart saved: income_expense.png")

# Pie chart - Expense breakdown
categories = ["Rent", "Food", "Transport", "Shopping", "Utilities", "Other"]
amounts    = [15000, 8000, 3000, 5000, 2000, 2000]

plt.figure(figsize=(8, 8))
plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=90)
plt.title("Expense Breakdown")
plt.savefig("expense_pie.png")
print("Chart saved: expense_pie.png")
