-- Secondary index for low-cardinality lookups.
CREATE INDEX IF NOT EXISTS idx_users_email ON users (email);

CREATE CUSTOM INDEX IF NOT EXISTS idx_users_attrs
ON users (ENTRIES(attrs)) USING 'StorageAttachedIndex';

SELECT * FROM users WHERE email = 'ada@example.com';
