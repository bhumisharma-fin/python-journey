# NumPy - Numbers ko fast process karne ke liye
# Finance me: returns calculate, average, std deviation

import numpy as np

# Array banana - list se better aur faster
prices = np.array([100, 105, 98, 110, 107])
print("Stock Prices:", prices)

# Basic calculations - ek line me!
print("Average Price:", np.mean(prices))       # 104.0
print("Highest Price:", np.max(prices))        # 110
print("Lowest Price:", np.min(prices))         # 98
print("Std Deviation:", np.std(prices))        # market volatility measure

# Daily returns calculate karo
returns = np.diff(prices) / prices[:-1] * 100
print("Daily Returns (%):", returns.round(2))

# Multiple stocks ek saath
portfolio = np.array([
    [100, 105, 98],   # Stock A
    [200, 195, 210],  # Stock B
    [50,  52,  49],   # Stock C
])
print("\nPortfolio Average per stock:", np.mean(portfolio, axis=1))
