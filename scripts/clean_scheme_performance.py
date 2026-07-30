import os
import pandas as pd

# Read the dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for column in return_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Check for missing return values
missing_returns = df[df[return_columns].isnull().any(axis=1)]

# Flag unusual return values
# (less than -100% or greater than 200%)
anomalies = df[
    (df["return_1yr_pct"] < -100) | (df["return_1yr_pct"] > 200) |
    (df["return_3yr_pct"] < -100) | (df["return_3yr_pct"] > 200) |
    (df["return_5yr_pct"] < -100) | (df["return_5yr_pct"] > 200)
]

# Validate expense ratio
# Expected range: 0.1% to 2.5%
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

# Remove duplicate rows
df = df.drop_duplicates()

# Create processed folder if needed
os.makedirs("data/processed", exist_ok=True)

# Save cleaned dataset
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

# Print summaryprint("=" * 50)
print("Scheme Performance Cleaning Summary")
print("=" * 50)

print(f"Total Records              : {len(df)}")
print(f"Duplicate Rows Removed     : {df.duplicated().sum()}")
print(f"Missing Return Records     : {len(missing_returns)}")
print(f"Return Value Anomalies     : {len(anomalies)}")
print(f"Invalid Expense Ratios     : {len(invalid_expense)}")

print("\nCleaned file saved successfully.")