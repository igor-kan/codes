// MERGE performs match-or-create semantics (upsert).
MERGE (p:Person {email: "ada@example.com"})
  ON CREATE SET p.createdAt = timestamp(), p.name = "Ada"
  ON MATCH SET p.lastSeen = timestamp()
RETURN p;

UNWIND $rows AS row
MERGE (p:Person {email: row.email})
SET p.name = row.name;
