-- =====================================================
-- MUTUAL FUND ANALYTICS - SQL QUERIES
-- =====================================================

-- =====================================================
-- Query 1: Total Number of Mutual Funds
-- =====================================================

SELECT COUNT(*) AS total_funds
FROM dim_fund;

-- =====================================================
-- Query 2: Count of Funds by Category
-- =====================================================

SELECT
    category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;

-- =====================================================
-- Query 3: Top 10 Funds by 1-Year Return
-- =====================================================

SELECT
    amfi_code,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- =====================================================
-- Query 4: Total Investment by State
-- =====================================================

SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;

-- =====================================================
-- Query 5: Transaction Type Distribution
-- =====================================================

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- =====================================================
-- Query 6: Average Expense Ratio
-- =====================================================

SELECT
    ROUND(AVG(expense_ratio_pct), 2) AS average_expense_ratio
FROM fact_performance;

-- =====================================================
-- Query 7: Top 5 Funds by Sharpe Ratio
-- =====================================================

SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- =====================================================
-- Query 8: Total Investment by Payment Mode
-- =====================================================

SELECT
    payment_mode,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_amount DESC;

-- =====================================================
-- Query 9: Transactions by Gender
-- =====================================================

SELECT
    gender,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY gender;

-- =====================================================
-- Query 10: Top 5 Cities by Investment
-- =====================================================

SELECT
    city,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY city
ORDER BY total_investment DESC
LIMIT 5;