# Finance Dashboard - Sab kuch ek jagah
# Ye apka final project hai Bhumi!

from datetime import datetime

class FinanceDashboard:
    def __init__(self, name, monthly_income):
        self.name = name
        self.income = monthly_income
        self.expenses = {}
        self.investments = {}
        self.goals = []

    def add_expense(self, category, amount):
        self.expenses[category] = self.expenses.get(category, 0) + amount

    def add_investment(self, name, amount, expected_return):
        self.investments[name] = {"amount": amount, "return": expected_return}

    def add_goal(self, name, target, months):
        monthly_needed = target / months
        self.goals.append({"name": name, "target": target, "months": months, "monthly": monthly_needed})

    def show_dashboard(self):
        total_expense    = sum(self.expenses.values())
        total_investment = sum(v["amount"] for v in self.investments.values())
        savings          = self.income - total_expense - total_investment

        print(f"\n{**50}")
        print(f"  FINANCE DASHBOARD - {self.name.upper()}")
        print(f"  {datetime.now().strftime(%B