-- Nearest neighbours by cosine distance.
SELECT id, content, 1 - (embedding <=> $1) AS cosine_similarity
FROM documents
ORDER BY embedding <=> $1
LIMIT 10;

-- L2 distance and inner product operators: <-> and <#>.
SELECT id FROM documents ORDER BY embedding <-> $1 LIMIT 5;
