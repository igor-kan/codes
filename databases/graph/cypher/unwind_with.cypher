// UNWIND, WITH chaining and list comprehension.
UNWIND [1, 2, 3, 4] AS n
WITH n, n * n AS squared
WHERE squared % 2 = 0
RETURN n, squared;

MATCH (p:Person)
WITH p.born AS year, count(*) AS born
ORDER BY year
RETURN collect({year: year, count: born}) AS timeline;
