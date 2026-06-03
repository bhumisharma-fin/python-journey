# Credit Score Guide - India (CIBIL)
def credit_score_analysis(score):
    if score >= 750:
        rating = "EXCELLENT"
        advice = "Best loan rates available! Keep it up."
    elif score >= 700:
        rating = "GOOD"
        advice = "Good rates, can improve further."
    elif score >= 650:
        rating = "FAIR"
        advice = "Moderate rates. Work on improving."
    elif score >= 600:
        rating = "POOR"
        advice = "High interest rates. Focus on improvement."
    else:
        rating = "VERY POOR"
        advice = "Difficult to get loans. Urgent action needed."

    print(f"\nCIBIL Score: {score}")
    print(f"Rating:      {rating}")
    print(f"Advice:      {advice}")

# Factors that affect credit score
factors = {
    "Payment History":     "35% - Always pay EMI on time!",
    "Credit Utilization":  "30% - Use less than 30% of credit limit",
    "Credit Age":          "15% - Keep old cards active",
    "Credit Mix":          "10% - Mix of secured/unsecured loans",
    "New Credit":          "10% - Dont apply for too many loans",
}
print("CREDIT SCORE FACTORS:")
for factor, impact in factors.items():
    print(f"  {factor:<22}: {impact}")

credit_score_analysis(780)
credit_score_analysis(680)
