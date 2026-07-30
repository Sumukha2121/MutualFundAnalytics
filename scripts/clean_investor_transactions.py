import os
import pandas as pd

# Read the dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# 1. Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# 2. Standardize transaction_type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)
# Replace common variations
df["transaction_type"] = df["transaction_type"].replace({
    "Sip": "SIP",
    "Lump Sum": "Lumpsum",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

# 3. Validate amount > 0
invalid_amount = df[df["amount_inr"] <= 0]

# 4. Validate KYC Status
allowed_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = df[~df["kyc_status"].isin(allowed_kyc)]

# 5. Remove duplicate rows
df = df.drop_duplicates()

# 6. Create processed folder
os.makedirs("data/processed", exist_ok=True)

# 7. Save cleaned dataset
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

# 8. Print summary
print("=" * 50)
print("Investor Transactions Cleaning Summary")
print("=" * 50)

print(f"Total Records : {len(df)}")

print(f"Duplicate Rows Removed : {df.duplicated().sum()}")

print(f"Invalid Amount Records : {len(invalid_amount)}")

print(f"Invalid KYC Records : {len(invalid_kyc)}")

print("\nTransaction Types:")
print(df["transaction_type"].value_counts())

print("\nKYC Status:")
print(df["kyc_status"].value_counts())

print("\nCleaned file saved successfully!")