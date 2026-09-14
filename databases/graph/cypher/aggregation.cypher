// Aggregation, grouping and collection.
MATCH (p:Person)-[:WORKS_AT]->(c:Company)
RETURN c.name AS company, count(p) AS employees, collect(p.name) AS names
ORDER BY employees DESC;

MATCH (p:Post)<-[:WROTE]-(u:User)
RETURN u.name, avg(size((p.body))) AS avgBody, max(p.createdAt) AS latest;
