# Python for Finance Interviews
# Common questions asked in finance/data roles

# 1. Find top 3 expenses
expenses = {"Rent": 20000, "Food": 8000, "Shopping": 5000,
            "Transport": 3000, "Entertainment": 2000, "Utilities": 2000}
top3 = sorted(expenses.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 expenses:", top3)

# 2. Calculate portfolio return
portfolio = [
    ("RELIANCE", 2400, 2650, 10),
    ("TCS",      3200, 3450, 5),
    ("INFY",     1400, 1380, 15),  # loss
]
total_invested = sum(buy * qty for _, buy, _, qty in portfolio)
total_value    = sum(curr * qty for _, _, curr, qty in portfolio)
overall_return = (total_value - total_invested) / total_invested * 100
print(f"\nPortfolio Return: {overall_return:.2f}%")

# 3. Running total (cumulative sum)
monthly_savings = [5000, 8000, 6000, 10000, 7000, 9000]
running_total = []
total = 0
for s in monthly_savings:
    total += s
    running_total.append(total)
print(f"\nRunning savings: {running_total}")

# 4. Find months where spending exceeded budget
budget = 40000
actual = [38000, 42000, 35000, 45000, 39000, 41000]
months = ["Jan","Feb","Mar","Apr","May","Jun"]
over = [(m, a) for m, a in zip(months, actual) if a > budget]
print(f"\nOver budget: {over}")

# 5. Compound Annual Growth Rate
start, end, years = 100000, 185000, 6
cagr = (end/start)**(1/years) - 1
print(f"\nCAGR: {cagr*100:.2f}%")
