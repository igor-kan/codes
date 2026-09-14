-- Enable pgvector and create a table with an embedding column.
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (
  id        bigserial PRIMARY KEY,
  content   text NOT NULL,
  embedding vector(1536) NOT NULL,
  created_at timestamptz DEFAULT now()
);
