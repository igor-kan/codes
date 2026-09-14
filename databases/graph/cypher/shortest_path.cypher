// Shortest path and variable-length patterns.
MATCH (a:Person {name: "Ada"}), (b:Person {name: "Grace"})
MATCH path = shortestPath((a)-[:KNOWS*..10]-(b))
RETURN [n IN nodes(path) | n.name] AS route, length(path) AS hops;

MATCH p = (a:Airport {code: "LHR"})-[:FLIGHT*1..3]->(b:Airport {code: "JFK"})
RETURN p
ORDER BY length(p)
LIMIT 5;
