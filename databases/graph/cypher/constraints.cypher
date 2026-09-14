// Uniqueness constraints and indexes.
CREATE CONSTRAINT person_email IF NOT EXISTS
FOR (p:Person) REQUIRE p.email IS UNIQUE;

CREATE INDEX person_name IF NOT EXISTS FOR (p:Person) ON (p.name);
CREATE FULLTEXT INDEX person_search IF NOT EXISTS
FOR (p:Person) ON EACH [p.name, p.bio];
