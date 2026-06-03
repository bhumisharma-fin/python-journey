# String Methods - Text data clean karna
# Finance me: names, descriptions clean karna

text = "  Hello Finance Professional!  "
print(text.strip())   # Remove spaces
print(text.lower())   # lowercase
print(text.upper())   # UPPERCASE
print(text.title())   # Title Case

# Clean transaction names
transactions = ["ZOMATO ORDER", "amazon.in", "  UPI-PHONEPE  "]
cleaned = [t.strip().title() for t in transactions]
print(cleaned)

# Split CSV line
csv_line = "Bhumi,28,Mumbai,Finance"
parts = csv_line.split(",")
print(parts)

# Remove Rs and convert to number
amount_str = "Rs 1,500.50"
clean = amount_str.replace("Rs ", "").replace(",", "")
amount = float(clean)
print(f"Amount: {amount}")

# f-strings - very useful!
name = "Bhumi"
salary = 75000
print(f"Name: {name}")
print(f"Salary: Rs {salary:,}/month")
print(f"Annual: Rs {salary*12:,}/year")
