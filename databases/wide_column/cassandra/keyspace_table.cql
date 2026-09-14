-- Keyspace and table definitions.
CREATE KEYSPACE IF NOT EXISTS app
  WITH replication = { 'class': 'NetworkTopologyStrategy', 'replication_factor': 3 }
  AND durable_writes = true;

USE app;

CREATE TABLE IF NOT EXISTS users (
  user_id   uuid PRIMARY KEY,
  email     text,
  name      text,
  created_at timestamp
);
