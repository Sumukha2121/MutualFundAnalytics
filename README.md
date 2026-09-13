# Bluestock Mutual Fund Analytics

## Project Overview

Bluestock Mutual Fund Analytics is an end-to-end data analytics project developed as part of the Bluestock Fintech internship.

The project analyzes mutual fund industry data including fund master information, historical NAV, AUM, SIP inflows, category-level inflows, investor transactions, scheme performance, portfolio holdings, and benchmark indices.

The project combines Python-based ETL and analytics, SQLite database design, SQL analysis, and interactive Tableau dashboards to generate meaningful business and investment insights.

---

## Objectives

- Analyze mutual fund industry AUM and growth trends.
- Study SIP inflows and investor participation.
- Evaluate mutual fund scheme performance and risk.
- Compare fund returns against benchmark indices.
- Analyze investor transaction behavior and demographics.
- Identify category-level investment trends.
- Perform advanced risk and portfolio analytics.
- Build interactive dashboards for decision-making.
- Develop a reusable data processing and analytics pipeline.

---

## Dataset

The project uses 10 primary mutual fund datasets containing **87,533 records** in total.

| Dataset | Records | Description |
|---|---:|---|
| Fund Master | 40 | Fund, category, plan and scheme information |
| NAV History | 46,000 | Historical daily NAV data |
| AUM by Fund House | 90 | Fund-house level AUM and scheme counts |
| Monthly SIP Inflows | 48 | Monthly SIP inflows and SIP account metrics |
| Category Inflows | 144 | Category-wise monthly net inflows |
| Industry Folio Count | 21 | Industry-level investor folio data |
| Scheme Performance | 40 | Returns, risk and performance metrics |
| Investor Transactions | 32,778 | Investor transaction-level data |
| Portfolio Holdings | 322 | Scheme portfolio and sector holdings |
| Benchmark Indices | 8,050 | Historical benchmark index values |

An additional `live_nav.csv` dataset is used for the latest available NAV data.

---

## Technology Stack

### Programming & Analytics
- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- Statsmodels

### Database
- SQLite
- SQLAlchemy
- SQL

### Visualization
- Tableau

### Development
- Jupyter Notebook
- Visual Studio Code
- Git / GitHub

---

## Project Architecture

```text
Raw CSV Data
     |
     v
Data Ingestion
     |
     v
Data Cleaning & Validation
     |
     v
Processed Datasets
     |
     v
SQLite Database
     |
     +----------------------+
     |                      |
     v                      v
SQL Analytics        Python Analytics
                           |
                           v
                  Performance & Risk Metrics
                           |
                           v
                    Tableau Dashboards
                           |
                           v
                 Reports & Presentations
## Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│
├── scripts/
│   ├── clean_investor_transactions.py
│   ├── clean_nav_history.py
│   ├── clean_scheme_performance.py
│   ├── create_database.py
│   ├── create_date_dimension.py
│   ├── data_quality_report.py
│   ├── explore_fund_master.py
│   ├── load_to_sqlite.py
│   ├── recommender.py
│   └── validate_amfi.py
│
├── data_ingestion.py
├── live_nav_fetch.py
├── run_pipeline.py
├── schema.sql
├── queries.sql
├── DATA_DICTIONARY.md
├── requirements.txt
└── README.md
