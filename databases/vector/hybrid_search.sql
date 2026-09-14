-- Hybrid full-text + vector search with reciprocal rank fusion.
WITH keyword AS (
  SELECT id, row_number() OVER (ORDER BY ts_rank_cd(tsv, query) DESC) AS rank
  FROM documents, websearch_to_tsquery('english', $2) query
  WHERE tsv @@ query
  LIMIT 50
),
semantic AS (
  SELECT id, row_number() OVER (ORDER BY embedding <=> $1) AS rank
  FROM documents
  LIMIT 50
)
SELECT d.id, d.content
FROM documents d
LEFT JOIN keyword k ON k.id = d.id
LEFT JOIN semantic s ON s.id = d.id
ORDER BY COALESCE(1.0 / (60 + k.rank), 0) + COALESCE(1.0 / (60 + s.rank), 0) DESC
LIMIT 10;
