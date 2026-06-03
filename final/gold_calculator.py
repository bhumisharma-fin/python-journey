# Gold Investment Calculator
def gold_returns(grams, buy_price, current_price):
    invested = grams * buy_price
    current_value = grams * current_price
    profit = current_value - invested
    returns = profit / invested * 100
    print(f"Gold Investment Summary")
    print(f"Quantity:       {grams}g")
    print(f"Buy Price:      Rs {buy_price:,}/g")
    print(f"Current Price:  Rs {current_price:,}/g")
    print(f"Invested:       Rs {invested:,}")
    print(f"Current Value:  Rs {current_value:,}")
    print(f"Profit/Loss:    Rs {profit:,} ({returns:+.2f}%)")

# Gold vs FD comparison
def gold_vs_fd(amount, gold_return, fd_rate, years):
    gold_value = amount * (1 + gold_return/100) ** years
    fd_value   = amount * (1 + fd_rate/100) ** years
    print(f"\nGold vs FD - Rs {amount:,} for {years} years")
    print(f"Gold ({gold_return}%/yr): Rs {gold_value:,.0f}")
    print(f"FD   ({fd_rate}%/yr):  Rs {fd_value:,.0f}")
    winner = "Gold" if gold_value > fd_value else "FD"
    print(f"Winner: {winner}!")

gold_returns(50, 5500, 7200)
gold_vs_fd(500000, 12, 7.5, 10)
