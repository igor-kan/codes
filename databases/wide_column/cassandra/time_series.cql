-- Time-series pattern with a clustering column and TTL.
CREATE TABLE sensor_readings (
  sensor_id  uuid,
  reading_at timestamp,
  value      double,
  PRIMARY KEY ((sensor_id), reading_at)
) WITH CLUSTERING ORDER BY (reading_at DESC)
  AND default_time_to_live = 2592000;

INSERT INTO sensor_readings (sensor_id, reading_at, value)
VALUES (uuid(), toTimestamp(now()), 21.5) USING TTL 86400;

SELECT * FROM sensor_readings
WHERE sensor_id = 550e8400-e29b-41d4-a716-446655440000
  AND reading_at > '2026-01-01';
