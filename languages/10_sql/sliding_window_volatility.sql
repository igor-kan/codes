-- =============================================================================
-- File: languages/10_sql/sliding_window_volatility.sql
-- Language: ANSI SQL (PostgreSQL 14+, DuckDB, BigQuery, Snowflake Compatible)
-- Domain: Quantitative Finance & Market Microstructure
-- Algorithm: Analytical Sliding Windows for 20/50 SMA & 20-Day Annualized Volatility
--
-- Rationale & Language Fit:
--   SQL is the undisputed standard declarative language for relational database
--   querying and financial data engineering. Window functions (`OVER (PARTITION BY ...
--   ORDER BY ... ROWS BETWEEN ...)`) enable declarative, cache-friendly vector
--   computations directly inside the database engine without loading gigabytes of
--   tick data into application memory.
-- =============================================================================

-- Schema Definition: Daily equity price series
CREATE TABLE IF NOT EXISTS daily_market_quotes (
    symbol          VARCHAR(12) NOT NULL,
    trade_date      DATE NOT NULL,
    adj_close       NUMERIC(14, 4) NOT NULL,
    volume          BIGINT NOT NULL,
    PRIMARY KEY (symbol, trade_date)
);

-- Analytical Query: Computes Daily Log Returns, 20/50 SMA, and Annualized Volatility
WITH price_returns AS (
    SELECT
        symbol,
        trade_date,
        adj_close,
        volume,
        -- Prior day close using LAG window function
        LAG(adj_close, 1) OVER (
            PARTITION BY symbol
            ORDER BY trade_date
        ) AS prev_close,
        -- Daily logarithmic return: ln(P_t / P_{t-1})
        LN(adj_close / NULLIF(LAG(adj_close, 1) OVER (
            PARTITION BY symbol
            ORDER BY trade_date
        ), 0)) AS log_return
    FROM daily_market_quotes
),
rolling_metrics AS (
    SELECT
        symbol,
        trade_date,
        adj_close,
        log_return,
        -- 20-Day Simple Moving Average (SMA_20)
        AVG(adj_close) OVER (
            PARTITION BY symbol
            ORDER BY trade_date
            ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
        ) AS sma_20,
        
        -- 50-Day Simple Moving Average (SMA_50)
        AVG(adj_close) OVER (
            PARTITION BY symbol
            ORDER BY trade_date
            ROWS BETWEEN 49 PRECEDING AND CURRENT ROW
        ) AS sma_50,
        
        -- Count of records in the 20-day window (to filter out incomplete warmups)
        COUNT(log_return) OVER (
            PARTITION BY symbol
            ORDER BY trade_date
            ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
        ) AS return_count_20,
        
        -- Sample Standard Deviation of 20-day daily log returns
        STDDEV_SAMP(log_return) OVER (
            PARTITION BY symbol
            ORDER BY trade_date
            ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
        ) AS daily_volatility_20d
    FROM price_returns
)
SELECT
    symbol,
    trade_date,
    ROUND(adj_close, 2) AS close_price,
    ROUND(sma_20, 2) AS sma_20,
    ROUND(sma_50, 2) AS sma_50,
    -- Golden Cross / Death Cross indicator signal
    CASE 
        WHEN sma_20 > sma_50 THEN 'BULLISH_TREND'
        WHEN sma_20 < sma_50 THEN 'BEARISH_TREND'
        ELSE 'NEUTRAL'
    END AS ma_trend_signal,
    
    -- 20-Day Annualized Historical Volatility: sigma_daily * sqrt(252 trading days)
    CASE
        WHEN return_count_20 >= 20 THEN
            ROUND(daily_volatility_20d * SQRT(252.0) * 100.0, 2)
        ELSE NULL
    END AS annualized_volatility_pct
FROM rolling_metrics
ORDER BY symbol, trade_date;
