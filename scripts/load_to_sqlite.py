import pandas as pd
from sqlalchemy import create_engine, text

# Connect to SQLite
engine = create_engine("sqlite:///bluestock_mf.db")

# -----------------------------
# Load Dimension Table: dim_fund
# -----------------------------
fund_df = pd.read_csv("data/raw/01_fund_master.csv")

fund_df = fund_df[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "sub_category",
        "plan",
        "launch_date",
        "benchmark",
        "expense_ratio_pct",
        "exit_load_pct",
        "min_sip_amount",
        "min_lumpsum_amount",
        "fund_manager",
        "risk_category",
        "sebi_category_code",
    ]
]

fund_df.to_sql("dim_fund", engine, if_exists="append", index=False)

# -----------------------------
# Load Fact Table: fact_nav
# -----------------------------
nav_df = pd.read_csv("data/processed/nav_history_cleaned.csv")

nav_df = nav_df[
    [
        "amfi_code",
        "date",
        "nav",
    ]
]

nav_df.to_sql("fact_nav", engine, if_exists="append", index=False)

# -----------------------------
# Load Fact Table: fact_transactions
# -----------------------------
txn_df = pd.read_csv("data/processed/investor_transactions_cleaned.csv")

txn_df = txn_df[
    [
        "investor_id",
        "transaction_date",
        "amfi_code",
        "transaction_type",
        "amount_inr",
        "state",
        "city",
        "city_tier",
        "age_group",
        "gender",
        "annual_income_lakh",
        "payment_mode",
        "kyc_status",
    ]
]

txn_df.to_sql("fact_transactions", engine, if_exists="append", index=False)

# -----------------------------
# Load Fact Table: fact_performance
# -----------------------------
perf_df = pd.read_csv("data/processed/scheme_performance_cleaned.csv")

perf_df = perf_df[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "aum_crore",
        "expense_ratio_pct",
        "morningstar_rating",
    ]
]

perf_df.to_sql("fact_performance", engine, if_exists="append", index=False)

# -----------------------------
# Verify Row Counts
# -----------------------------
with engine.connect() as conn:
    print("\n========== DATABASE SUMMARY ==========")

    tables = [
        "dim_fund",
        "fact_nav",
        "fact_transactions",
        "fact_performance",
    ]

    for table in tables:
        count = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        ).scalar()

        print(f"{table:<20}: {count} rows")

print("\nData loaded successfully!")