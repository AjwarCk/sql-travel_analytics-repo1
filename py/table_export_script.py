import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

# -------------------------
# Hotels (Dimension)
# -------------------------
hotels = pd.DataFrame([
    [1, "Grand Central Hotel", "Bangkok", "Thailand", 5],
    [2, "City Comfort Inn", "Bangkok", "Thailand", 3],
    [3, "Seaside Resort", "Phuket", "Thailand", 4],
    [4, "Urban Stay", "Singapore", "Singapore", 4],
    [5, "Skyline Suites", "Kuala Lumpur", "Malaysia", 5],
    [6, "Harbor View", "Penang", "Malaysia", 4],
    [7, "Metro Lodge", "Jakarta", "Indonesia", 3],
    [8, "Palm Residency", "Bali", "Indonesia", 5],
    [9, "Business Hub", "Ho Chi Minh City", "Vietnam", 4],
    [10, "Riverside Hotel", "Hanoi", "Vietnam", 4]
], columns=["hotel_id", "hotel_name", "city", "country", "star_rating"])

# -------------------------
# Rooms (Dimension)
# -------------------------
rooms = pd.DataFrame([
    [101, 1, "Deluxe", 2],
    [102, 1, "Suite", 4],
    [201, 2, "Standard", 2],
    [301, 3, "Sea View", 2],
    [302, 3, "Family", 4],
    [401, 4, "Business", 2],
    [501, 5, "Executive", 2],
    [601, 6, "Harbor View", 2],
    [701, 7, "Standard", 2],
    [801, 8, "Villa", 4],
    [901, 9, "Corporate", 2],
    [1001, 10, "River View", 2]
], columns=["room_id", "hotel_id", "room_type", "max_guests"])

# -------------------------
# Room Inventory (60 days → ~7,200 rows)
# -------------------------
inventory_rows = []
start_date = datetime(2024, 7, 1)

for day in range(60):
    current_date = start_date + timedelta(days=day)
    for _, room in rooms.iterrows():
        inventory_rows.append([
            room["hotel_id"],
            room["room_id"],
            current_date.date(),
            random.randint(0, 15),
            round(random.uniform(55, 350), 2)
        ])

room_inventory = pd.DataFrame(
    inventory_rows,
    columns=[
        "hotel_id",
        "room_id",
        "date",
        "available_rooms",
        "price_per_night"
    ]
)

# -------------------------
# Bookings (3,000 rows)
# -------------------------
statuses = ["confirmed", "cancelled"]
booking_rows = []

booking_id = 10001

for _ in range(3000):
    room = rooms.sample(1).iloc[0]

    booking_date = start_date - timedelta(days=random.randint(1, 60))
    check_in = start_date + timedelta(days=random.randint(0, 50))
    nights = random.randint(1, 7)

    booking_rows.append([
        booking_id,
        room["hotel_id"],
        room["room_id"],
        booking_date.date(),
        check_in.date(),
        (check_in + timedelta(days=nights)).date(),
        random.choices(statuses, weights=[0.72, 0.28])[0],
        round(random.uniform(90, 1800), 2)
    ])

    booking_id += 1

bookings = pd.DataFrame(
    booking_rows,
    columns=[
        "booking_id",
        "hotel_id",
        "room_id",
        "booking_date",
        "check_in",
        "check_out",
        "status",
        "total_amount"
    ]
)

# -------------------------
# Export CSVs
# -------------------------
hotels.to_csv("/Users/ajwarck/Desktop/vs_code/sql/practice_dir/travel_analytics/data/hotels.csv", index=False)
rooms.to_csv("/Users/ajwarck/Desktop/vs_code/sql/practice_dir/travel_analytics/data/rooms.csv", index=False)
room_inventory.to_csv("/Users/ajwarck/Desktop/vs_code/sql/practice_dir/travel_analytics/data/room_inventory.csv", index=False)
bookings.to_csv("/Users/ajwarck/Desktop/vs_code/sql/practice_dir/travel_analytics/data/bookings.csv", index=False)

print("✅ CSVs created with >2,500 fact records (portfolio-safe)")
