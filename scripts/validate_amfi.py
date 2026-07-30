import pandas as pd

# Read both CSV files
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get unique AMFI codes from each file
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find codes present in NAV history but missing in fund master
missing_codes = nav_codes - fund_codes

# Display the result
if len(missing_codes) == 0:
    print("All AMFI codes are valid.")
else:
    print("Invalid AMFI Codes Found:")
    print(missing_codes)