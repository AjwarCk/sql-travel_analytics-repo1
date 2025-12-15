SHOW DATABASES;

-- Hotels (Supply)
CREATE TABLE hotels (
    hotel_id INT PRIMARY KEY,
    hotel_name VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50),
    star_rating INT
);

-- Rooms
CREATE TABLE rooms (
    room_id INT PRIMARY KEY,
    hotel_id INT,
    room_type VARCHAR(50),
    max_guests INT,
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id)
);

-- Daily Availability & Pricing
CREATE TABLE room_inventory (
    hotel_id INT,
    room_id INT,
    date DATE,
    available_rooms INT,
    price_per_night DECIMAL(10,2),
    PRIMARY KEY (hotel_id, room_id, date)
);

-- Bookings
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY,
    hotel_id INT,
    room_id INT,
    booking_date DATE,
    check_in DATE,
    check_out DATE,
    status VARCHAR(20), -- confirmed, cancelled
    total_amount DECIMAL(10,2)
);


SELECT * FROM hotels LIMIT 5;
SELECT * FROM rooms LIMIT 5;
SELECT * FROM bookings LIMIT 5;
SELECT * FROM room_inventory LIMIT 5;

DESCRIBE hotels;
DESCRIBE rooms;
DESCRIBE bookings;
DESCRIBE room_inventory;