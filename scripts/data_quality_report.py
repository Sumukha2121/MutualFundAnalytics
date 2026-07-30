import os
import pandas as pd

folder = "data/raw"

files = os.listdir(folder)

print("=" * 80)
print("DATA QUALITY REPORT")
print("=" * 80)

for file in files:
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        df = pd.read_csv(path)

        print(f"\nFile Name : {file}")
        print(f"Rows      : {df.shape[0]}")
        print(f"Columns   : {df.shape[1]}")

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:", df.duplicated().sum())

        if df.isnull().sum().sum() == 0 and df.duplicated().sum() == 0:
            print("\nRemarks : Dataset is clean.")
        else:
            print("\nRemarks : Dataset contains missing values or duplicate records.")

        print("-" * 80)