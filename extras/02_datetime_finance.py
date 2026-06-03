# DateTime - Dates handle karna Python me

from datetime import datetime, timedelta

today = datetime.today()
print(f"Today: {today.strftime("%d %B %Y")}")

# Days since investment
investment_date = datetime(2023, 1, 15)
days_held = (today - investment_date).days
years_held = days_held / 365
print(f"Investment held for: {days_held} days ({years_held:.1f} years)")

# Age calculation
dob = datetime(2002, 8, 14)
age = (today - dob).days // 365
print(f"Age: {age} years")

# Next payment date
last_payment = datetime(2026, 5, 5)
next_payment = last_payment + timedelta(days=30)
days_left = (next_payment - today).days
print(f"Next EMI: {next_payment.strftime("%d %B %Y")}")
print(f"Days left: {days_left}")

# Financial year
month = today.month
if month >= 4:
    fy = f"FY{today.year}-{str(today.year+1)[2:]}"
else:
    fy = f"FY{today.year-1}-{str(today.year)[2:]}"
print(f"Current FY: {fy}")
