-- Recursive CTE for Hierarchical Tree Traversal
WITH RECURSIVE OrgHierarchy AS (
    -- Anchor member: find top-level managers
    SELECT 
        employee_id, 
        manager_id, 
        first_name, 
        last_name, 
        1 AS depth, 
        CAST(employee_id AS VARCHAR(255)) AS lineage
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive member: traverse down the reporting chain
    SELECT 
        e.employee_id, 
        e.manager_id, 
        e.first_name, 
        e.last_name, 
        h.depth + 1, 
        CONCAT(h.lineage, ' -> ', e.employee_id)
    FROM employees e
    INNER JOIN OrgHierarchy h ON e.manager_id = h.employee_id
)
SELECT depth, employee_id, first_name, last_name, lineage
FROM OrgHierarchy
ORDER BY depth, employee_id;
