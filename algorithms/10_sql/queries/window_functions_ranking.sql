-- Analytical Window Functions: Dense Rank, Row Number, and Quantiles
SELECT 
    department_id,
    employee_id,
    salary,
    ROW_NUMBER() OVER(PARTITION BY department_id ORDER BY salary DESC) as rank_exact,
    DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) as rank_dense,
    NTILE(4) OVER(PARTITION BY department_id ORDER BY salary DESC) as salary_quartile,
    ROUND(PERCENT_RANK() OVER(PARTITION BY department_id ORDER BY salary), 4) as percentile_rank
FROM employees;
