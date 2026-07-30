import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["amfi_code", "date"])

# Forward-fill missing NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
df = df.drop_duplicates()

# Validate NAV values
invalid_nav = df[df["nav"] <= 0]

if invalid_nav.empty:
    print("All NAV values are valid.")
else:
    print("Invalid NAV values found:")
    print(invalid_nav)

# Save cleaned file
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("Cleaned file saved successfully.")