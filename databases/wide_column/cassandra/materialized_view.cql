-- Materialized view for an alternate query path.
CREATE MATERIALIZED VIEW IF NOT EXISTS users_by_email AS
  SELECT user_id, email, name
  FROM users
  WHERE email IS NOT NULL AND user_id IS NOT NULL
  PRIMARY KEY (email, user_id);

SELECT * FROM users_by_email WHERE email = 'ada@example.com';
