def tip_calculator(bill, tip_pct, people):
    tip = bill * tip_pct / 100
    total = bill + tip
    per_person = total / people
    print(f"Bill: Rs {bill:.2f}")
    print(f"Tip ({tip_pct}%): Rs {tip:.2f}")
    print(f"Total: Rs {total:.2f}")
    print(f"Per person: Rs {per_person:.2f}")

tip_calculator(1500, 10, 3)
