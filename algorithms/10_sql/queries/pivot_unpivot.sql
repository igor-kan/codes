-- Dynamic Matrix Cross Tabulation / Pivoting using CASE Expressions
SELECT 
    product_category,
    SUM(CASE WHEN fiscal_quarter = 'Q1' THEN sales_amount ELSE 0 END) AS q1_sales,
    SUM(CASE WHEN fiscal_quarter = 'Q2' THEN sales_amount ELSE 0 END) AS q2_sales,
    SUM(CASE WHEN fiscal_quarter = 'Q3' THEN sales_amount ELSE 0 END) AS q3_sales,
    SUM(CASE WHEN fiscal_quarter = 'Q4' THEN sales_amount ELSE 0 END) AS q4_sales,
    SUM(sales_amount) AS total_annual_sales
FROM quarterly_sales_log
GROUP BY product_category;
