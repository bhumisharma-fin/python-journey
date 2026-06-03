# Regex - Text se patterns dhundhna
import re

# PAN validation
def validate_pan(pan):
    return bool(re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$", pan.upper()))

print(validate_pan("ABCDE1234F"))  # True
print(validate_pan("ABC12345F"))   # False

# Extract amount from SMS
sms = "Rs 1,299 debited from your account. Ref: TXN20260603"
amount = re.search(r"Rs ([\d,]+)", sms)
ref = re.search(r"TXN\w+", sms)
if amount: print(f"Amount: {amount.group(1)}")
if ref:    print(f"Ref: {ref.group()}")

# All amounts in statement
statement = """
Debit Rs 1500 Zomato
Credit Rs 50000 Salary
Debit Rs 299 Netflix
"""
amounts = re.findall(r"Rs (\d+)", statement)
print(f"Amounts: {amounts}")
print(f"Total: Rs {sum(int(a) for a in amounts)}")
