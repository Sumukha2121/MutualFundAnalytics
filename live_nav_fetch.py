"""Fetch and store the latest available NAV data for the project."""
import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url,timeout=30)

data = response.json()

print(data.keys())

nav_df = pd.DataFrame(data["data"])

nav_df.to_csv("data/raw/live_nav.csv", index=False)

print(nav_df.head())