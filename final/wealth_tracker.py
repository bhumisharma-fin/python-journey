# Monthly Wealth Tracker - Net worth over time
import json

def add_monthly_data(month, assets, liabilities):
    net_worth = sum(assets.values()) - sum(liabilities.values())
    return {
        "month": month,
        "assets": sum(assets.values()),
        "liabilities": sum(liabilities.values()),
        "net_worth": net_worth
    }

history = [
    add_monthly_data("Jan 2026", {"savings": 120000, "mf": 200000, "stocks": 150000}, {"loan": 800000}),
    add_monthly_data("Feb 2026", {"savings": 130000, "mf": 215000, "stocks": 165000}, {"loan": 790000}),
    add_monthly_data("Mar 2026", {"savings": 145000, "mf": 225000, "stocks": 172000}, {"loan": 780000}),
    add_monthly_data("Apr 2026", {"savings": 158000, "mf": 240000, "stocks": 185000}, {"loan": 770000}),
    add_monthly_data("May 2026", {"savings": 170000, "mf": 260000, "stocks": 195000}, {"loan": 760000}),
    add_monthly_data("Jun 2026", {"savings": 185000, "mf": 275000, "stocks": 210000}, {"loan": 750000}),
]
print(f"{Month:<12} {Assets:>12} {Liabilities:>14} {Net