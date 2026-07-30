import os
import pandas as pd

folder = "data/raw"

files = os.listdir(folder)

for file in files:

    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("="*60)
        print("File:", file)

        print("\nShape")
        print(df.shape)

        print("\nColumns")
        print(df.columns)

        print("\nData Types")
        print(df.dtypes)

        print("\nFirst Five Rows")
        print(df.head())

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nDuplicate Rows")
        print(df.duplicated().sum())

        print("="*60)