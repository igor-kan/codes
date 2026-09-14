-- Interval and Temporal Overlap Resolution Pattern
SELECT 
    a.booking_id AS booking_a,
    b.booking_id AS booking_b,
    a.room_id,
    GREATEST(a.check_in, b.check_in) AS overlap_start,
    LEAST(a.check_out, b.check_out) AS overlap_end
FROM hotel_bookings a
INNER JOIN hotel_bookings b 
    ON a.room_id = b.room_id 
   AND a.booking_id < b.booking_id
   AND a.check_in < b.check_out 
   AND a.check_out > b.check_in;
