# Expense Splitter - Trip ya dinner expenses split karo
class ExpenseSplitter:
    def __init__(self, members):
        self.members = members
        self.expenses = []

    def add_expense(self, paid_by, description, amount, split_among=None):
        if split_among is None:
            split_among = self.members
        self.expenses.append({
            "paid_by": paid_by, "desc": description,
            "amount": amount, "split": split_among
        })

    def calculate(self):
        balance = {m: 0 for m in self.members}
        for exp in self.expenses:
            share = exp["amount"] / len(exp["split"])
            balance[exp["paid_by"]] += exp["amount"]
            for member in exp["split"]:
                balance[member] -= share

        print("\nEXPENSE SUMMARY:")
        for exp in self.expenses:
            print(f"  {exp[paid_by]} paid Rs {exp[amount]:,} for {exp[desc]}")

        print("\nFINAL SETTLEMENT:")
        for member, bal in balance.items():
            if bal > 0:
                print(f"  {member} gets back Rs {bal:,.0f}")
            elif bal < 0:
                print(f"  {member} owes Rs {abs(bal):,.0f}")

trip = ExpenseSplitter(["Nick", "Bhumi", "Rahul", "Priya"])
trip.add_expense("Nick",  "Hotel",      8000)
trip.add_expense("Bhumi", "Food",       3600)
trip.add_expense("Rahul", "Petrol",     2400)
trip.add_expense("Priya", "Activities", 4000)
trip.calculate()
