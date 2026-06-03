# API se data fetch karna - requests library
# pip install requests

import json

# Simulated API response (real me requests.get() use karo)
sample_api_response = {
    "symbol": "RELIANCE",
    "exchange": "NSE",
    "lastPrice": 2650.45,
    "change": 23.50,
    "pChange": 0.895,
    "totalTradedVolume": 4523621,
    "52weekHigh": 3217.90,
    "52weekLow": 2180.30,
    "marketCap": 17954200000000,
}

def parse_stock_data(data):
    price      = data["lastPrice"]
    change     = data["change"]
    pchange    = data["pChange"]
    high52     = data["52weekHigh"]
    low52      = data["52weekLow"]
    mktcap_cr  = data["marketCap"] / 1e7

    print(f"Stock: {data[symbol]} ({data[exchange]})")
    print(f"Price:      Rs {price:,.2f}")
    print(f"Change:     {change:+.2f} ({pchange:+.3f}%)")
    print(f"52W High:   Rs {high52:,.2f}")
    print(f"52W Low:    Rs {low52:,.2f}")
    print(f"Mkt Cap:    Rs {mktcap_cr:,.0f} Cr")

    # Price position in 52-week range
    position = (price - low52) / (high52 - low52) * 100
    print(f"52W Range:  {position:.1f}% from low")

parse_stock_data(sample_api_response)

# Real API example (uncomment to use):
# import requests
# url = "https://query1.finance.yahoo.com/v8/finance/chart/RELIANCE.NS"
# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# data = response.json()
