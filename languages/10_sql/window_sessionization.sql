-- Advanced Analytical SQL: Sessionization and Sliding Inactivity Windows
-- Groups stream event logs into distinct user sessions based on a 30-minute inactivity boundary.

WITH event_deltas AS (
    SELECT
        user_id,
        event_time,
        event_type,
        EXTRACT(EPOCH FROM (event_time - LAG(event_time) OVER (
            PARTITION BY user_id 
            ORDER BY event_time
        ))) AS seconds_since_last_event
    FROM user_activity_log
),
session_flags AS (
    SELECT
        user_id,
        event_time,
        event_type,
        CASE
            WHEN seconds_since_last_event IS NULL OR seconds_since_last_event > 1800 THEN 1
            ELSE 0
        END AS is_new_session
    FROM event_deltas
),
session_grouped AS (
    SELECT
        user_id,
        event_time,
        event_type,
        SUM(is_new_session) OVER (
            PARTITION BY user_id 
            ORDER BY event_time 
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS session_id
    FROM session_flags
)
SELECT
    user_id,
    session_id,
    MIN(event_time) AS session_start,
    MAX(event_time) AS session_end,
    COUNT(*) AS total_events,
    EXTRACT(EPOCH FROM (MAX(event_time) - MIN(event_time))) AS session_duration_seconds
FROM session_grouped
GROUP BY user_id, session_id
ORDER BY user_id, session_start;
