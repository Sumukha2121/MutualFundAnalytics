# Mutual Fund Analytics - Data Dictionary

## Overview

This document describes the database schema, column definitions, data types, business meaning, and source datasets used in the Mutual Fund Analytics project.

---

# Table: dim_fund

**Source:** fund_master.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI code of the mutual fund (Primary Key) |
| scheme_name | TEXT | Name of the mutual fund scheme |
| fund_house | TEXT | Asset Management Company (AMC) |
| category | TEXT | Fund category (Equity, Debt, Hybrid, etc.) |
| sub_category | TEXT | Sub-category of the fund |
| plan | TEXT | Direct or Regular plan |
| launch_date | TEXT | Scheme launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Expense ratio (%) |
| exit_load_pct | REAL | Exit load (%) |
| min_sip_amount | REAL | Minimum SIP investment |
| min_lumpsum_amount | REAL | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk category |
| sebi_category_code | TEXT | SEBI classification code |

---

# Table: dim_date

**Source:** Generated from NAV and transaction dates

| Column | Data Type | Description |
|--------|-----------|-------------|
| date | TEXT | Calendar date (Primary Key) |
| year | INTEGER | Year |
| quarter | INTEGER | Quarter (1–4) |
| month | INTEGER | Month |
| day | INTEGER | Day of month |

---

# Table: fact_nav

**Source:** nav_history.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| nav_id | INTEGER | Primary Key |
| amfi_code | INTEGER | Fund identifier |
| date | TEXT | NAV date |
| nav | REAL | Net Asset Value |

---

# Table: fact_transactions

**Source:** investor_transactions.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| transaction_id | INTEGER | Primary Key |
| investor_id | TEXT | Investor identifier |
| transaction_date | TEXT | Transaction date |
| amfi_code | INTEGER | Fund identifier |
| transaction_type | TEXT | SIP, Lumpsum or Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | City tier |
| age_group | TEXT | Age group |
| gender | TEXT | Gender |
| annual_income_lakh | REAL | Annual income (Lakhs) |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

---

# Table: fact_performance

**Source:** scheme_performance.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| performance_id | INTEGER | Primary Key |
| amfi_code | INTEGER | Fund identifier |
| return_1yr_pct | REAL | 1-year return (%) |
| return_3yr_pct | REAL | 3-year return (%) |
| return_5yr_pct | REAL | 5-year return (%) |
| benchmark_3yr_pct | REAL | Benchmark return (%) |
| alpha | REAL | Alpha ratio |
| beta | REAL | Beta ratio |
| sharpe_ratio | REAL | Sharpe ratio |
| sortino_ratio | REAL | Sortino ratio |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown |
| aum_crore | REAL | Assets Under Management (Crores) |
| expense_ratio_pct | REAL | Expense ratio (%) |
| morningstar_rating | INTEGER | Morningstar rating |

---

# Table: fact_aum

**Source:** scheme_performance.csv

| Column | Data Type | Description |
|--------|-----------|-------------|
| aum_id | INTEGER | Primary Key |
| amfi_code | INTEGER | Fund identifier |
| aum_crore | REAL | Assets Under Management (Crores) |

---

## Relationships

- dim_fund → fact_nav
- dim_fund → fact_transactions
- dim_fund → fact_performance
- dim_fund → fact_aum
- dim_date → fact_nav
- dim_date → fact_transactions