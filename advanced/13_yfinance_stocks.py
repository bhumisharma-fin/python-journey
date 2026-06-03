# yfinance - Real stock market data Python me
# pip install yfinance pandas

# Note: Run karne ke liye internet chahiye
# yf.download() real NSE/BSE data fetch karta hai

import yfinance as yf
from datetime import datetime, timedelta

# Indian stocks - NSE suffix ".NS" lagta hai
stocks = {
    "Reliance": "RELIANCE.NS",
    "TCS":      "TCS.NS",
    "Infosys":  "INFY.NS",
}

print("Indian Stock Prices (Live)")
print("=" * 45)

for name, ticker in stocks.items():
    stock = yf.Ticker(ticker)
    info  = stock.info
    price = info.get("currentPrice", "N/A")
    pe    = info.get("trailingPE", "N/A")
    mktcap = info.get("marketCap", 0)
    mktcap_cr = mktcap / 1e7 if mktcap else "N/A"

    print(f"\n{name} ({ticker})")
    print(f"  Price:     Rs {price}")
    print(f"  P/E Ratio: {pe:.1f}" if isinstance(pe, float) else f"  P/E Ratio: {pe}")
    print(f"  Mkt Cap:   Rs {mktcap_cr:,.0f} Cr" if mktcap else f"  Mkt Cap:   {mktcap_cr}")

# Historical data - last 30 days
print("\nFetching 30-day history for TCS...")
data = yf.download("TCS.NS", period="1mo", progress=False)
print(data[["Open","High","Low","Close","Volume"]].tail(5))
