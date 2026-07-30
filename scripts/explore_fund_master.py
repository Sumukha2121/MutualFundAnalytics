import pandas as pd

# Read the CSV file
df = pd.read_csv("data/raw/01_fund_master.csv")

# Display all column names
print("Columns:")
print(df.columns)

# Display unique categories
print("\nUnique Categories:")
print(df["category"].unique())

# Display unique sub-categories
print("\nUnique Sub-Categories:")
print(df["sub_category"].unique())

# Display unique risk categories
print("\nUnique Risk Categories:")
print(df["risk_category"].unique())