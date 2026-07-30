import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

nav = pd.read_sql("SELECT DISTINCT date FROM fact_nav", conn)

nav["date"] = pd.to_datetime(nav["date"])

date_dim = pd.DataFrame({
    "date": nav["date"].dt.strftime("%Y-%m-%d"),
    "year": nav["date"].dt.year,
    "quarter": nav["date"].dt.quarter,
    "month": nav["date"].dt.month,
    "day": nav["date"].dt.day
})

date_dim.to_sql(
    "dim_date",
    conn,
    if_exists="append",
    index=False
)

conn.close()

print("Date dimension loaded successfully.")