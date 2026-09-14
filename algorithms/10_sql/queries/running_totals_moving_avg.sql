-- Time-Series Analytics: Cumulative Sum and 7-Day Centered Moving Average
SELECT 
    transaction_date,
    daily_revenue,
    SUM(daily_revenue) OVER (
        ORDER BY transaction_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue,
    AVG(daily_revenue) OVER (
        ORDER BY transaction_date 
        ROWS BETWEEN 3 PRECEDING AND 3 FOLLOWING
    ) AS centered_7day_moving_avg
FROM daily_financial_summary;
