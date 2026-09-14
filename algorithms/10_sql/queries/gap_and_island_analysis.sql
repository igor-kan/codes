-- Gaps and Islands Analysis: Grouping contiguous log events
WITH NumberedEvents AS (
    SELECT 
        user_id,
        event_date,
        ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY event_date) as rn,
        event_date - INTERVAL '1 day' * ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY event_date) as island_grp
    FROM user_activity_log
)
SELECT 
    user_id,
    MIN(event_date) as streak_start,
    MAX(event_date) as streak_end,
    COUNT(*) as streak_length
FROM NumberedEvents
GROUP BY user_id, island_grp
ORDER BY streak_length DESC;
