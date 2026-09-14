-- Approximate nearest neighbour indexes.
CREATE INDEX ON documents
  USING hnsw (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);

CREATE INDEX ON documents
  USING ivfflat (embedding vector_l2_ops)
  WITH (lists = 100);

SET hnsw.ef_search = 40;
