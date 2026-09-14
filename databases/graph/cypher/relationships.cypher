// Create and traverse relationships.
MATCH (a:Person {name: "Ada Lovelace"})
MATCH (b:Person {name: "Alan Turing"})
CREATE (a)-[:INFLUENCED {year: 1936}]->(b);

MATCH (a:Person)-[r:INFLUENCED]->(b:Person)
RETURN a.name AS from, type(r) AS rel, b.name AS to;
