# Currency Converter
rates = {"USD": 83.5, "EUR": 90.2, "GBP": 105.3, "JPY": 0.56, "AED": 22.7}

def convert(amount, from_curr, to_curr):
    if from_curr == "INR":
        inr = amount
    else:
        inr = amount * rates[from_curr]
    if to_curr == "INR":
        result = inr
    else:
        result = inr / rates[to_curr]
    print(f"{amount} {from_curr} = {result:.2f} {to_curr}")

convert(100, "USD", "INR")
convert(50000, "INR", "USD")
convert(1000, "INR", "JPY")
