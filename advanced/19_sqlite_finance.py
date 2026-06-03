# SQLite - Local database for finance data
# No server needed - file based database

import sqlite3
from datetime import datetime

# Database connect/create
conn = sqlite3.connect(":memory:")  # In-memory for demo
cursor = conn.cursor()

# Tables create karo
cursor.executescript("""
    CREATE TABLE IF NOT EXISTS transactions (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        date        TEXT NOT NULL,
        description TEXT NOT NULL,
        amount      REAL NOT NULL,
        category    TEXT NOT NULL,
        type        TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS categories (
        id   INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        budget REAL
    );
""")

# Sample data insert
transactions = [
    ("2026-06-01", "Salary",      60000,  "Income",    "credit"),
    ("2026-06-02", "Rent",       -15000,  "Housing",   "debit"),
    ("2026-06-05", "Groceries",   -4500,  "Food",      "debit"),
    ("2026-06-10", "Freelance",   10000,  "Income",    "credit"),
    ("2026-06-15", "Netflix",      -649,  "Entertain", "debit"),
    ("2026-06-20", "Zomato",      -1200,  "Food",      "debit"),
    ("2026-06-25", "SIP",         -5000,  "Investment","debit"),
]
cursor.executemany(
    "INSERT INTO transactions (date, description, amount, category, type) VALUES (?,?,?,?,?)",
    transactions
)
conn.commit()

# Query: Category wise spending
print("CATEGORY WISE SUMMARY:")
cursor.execute("""
    SELECT category, SUM(amount) as total, COUNT(*) as count
    FROM transactions
    GROUP BY category
    ORDER BY total
""")
for row in cursor.fetchall():
    print(f"  {row[0]:<15} Rs {row[1]:>10,.0f}  ({row[2]} txns)")

# Total balance
cursor.execute("SELECT SUM(amount) FROM transactions")
balance = cursor.fetchone()[0]
print(f"\nNet Balance: Rs {balance:,.0f}")

conn.close()
