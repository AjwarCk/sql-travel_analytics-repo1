SHOW DATABASES;

SELECT DATABASE();

-- 1. Volume & Emptiness (baseline)
SELECT 'hotels' AS tbl, COUNT(*) AS cnt FROM hotels
UNION ALL
SELECT 'rooms' AS tbl, COUNT(*) AS cnt FROM rooms
UNION ALL
SELECT 'room_inventory' AS tbl, COUNT(*) AS cnt FROM room_inventory
UNION ALL
SELECT 'bookings' AS tbl, COUNT(*) AS cnt FROM bookings;