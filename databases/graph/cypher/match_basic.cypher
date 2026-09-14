// Pattern matching with labels, relationships and predicates.
MATCH (p:Person) RETURN p.name AS name, p.born AS born;

MATCH (p:Person)-[:WORKS_AT]->(c:Company {name: "Example Corp"})
WHERE p.born > 1900
RETURN p.name, c.name
ORDER BY p.name
LIMIT 10;
