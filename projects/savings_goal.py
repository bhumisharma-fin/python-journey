def savings_goal(goal_name, target, current, monthly_saving):
    remaining = target - current
    months = remaining / monthly_saving if monthly_saving > 0 else float("inf")
    years = months / 12
    pct = current / target * 100
    bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
    print(f"\nGoal: {goal_name}")
    print(f"Progress: [{bar}] {pct:.1f}%")
    print(f"Target:   Rs {target:,}")
    print(f"Saved:    Rs {current:,}")
    print(f"Remaining: Rs {remaining:,}")
    print(f"ETA:      {months:.0f} months ({years:.1f} years)")

savings_goal("Emergency Fund", 300000, 85000, 10000)
savings_goal("Europe Trip",    200000, 45000, 8000)
savings_goal("New Phone",       60000, 20000, 5000)
