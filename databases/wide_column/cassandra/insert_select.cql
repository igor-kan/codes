-- Inserts are upserts; reads are by partition key.
INSERT INTO users (user_id, email, name, created_at)
VALUES (uuid(), 'ada@example.com', 'Ada', toTimestamp(now()));

SELECT user_id, email, name FROM users WHERE user_id = 550e8400-e29b-41d4-a716-446655440000;

SELECT * FROM users LIMIT 50 ALLOW FILTERING;
