import sqlite3

conn = sqlite3.connect("lines.db")
cursor = conn.cursor()


def create_tables():
    create_flights_table()
    create_seats_table()
    create_runways_table()
    create_extras_table()
    create_promo_codes_table()


def create_promo_codes_table():
    query = """CREATE TABLE IF NOT EXISTS
        promo_codes(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            code INTEGER NOT NULL,
            percents_discount INTEGER NOT NULL)"""

    cursor.execute(query)


def create_runways_table():
    query = """CREATE TABLE IF NOT EXISTS
        runway(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            is_free INTEGER NOT NULL,
            free_until TEXT NOT NULL)"""

    cursor.execute(query)


def create_flights_table():
    query = """CREATE TABLE IF NOT EXISTS
        flights(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            destination TEXT NOT NULL,
            time TEXT NOT NULL)"""
    cursor.execute(query)


def create_seats_table():
    query = """CREATE TABLE IF NOT EXISTS
        seats(id INTEGER PRIMARY KEY AUTOINCREMENT,
            num INTEGER NOT NULL,
            flight_id INTEGER NOT NULL,
            headphones INTEGER NOT NULL,
            champagne INTEGER NOT NULL,
            food INTEGER NOT NULL,
            price REAL NOT NULL,
            sold INTEGER NOT NULL,
            FOREIGN KEY(flight_id) REFERENCES flights(id))"""
    cursor.execute(query)


def create_extras_table():
    query = """CREATE TABLE IF NOT EXISTS
        extras(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            seat_num INTEGER NOT NULL,
            flight_id INTEGER NOT NULL,
            headphones_price INTEGER NOT NULL,
            champagne_price INTEGER NOT NULL,
            food_price INTEGER NOT NULL,
            FOREIGN KEY(seat_num) REFERENCES seats(num))"""
    cursor.execute(query)


def add_runway(is_free,  free_until):
    query = """INSERT into runway
    (is_free, free_until)
    values (?, ?)"""

    cursor.execute(query, (is_free, free_until))
    conn.commit()


def add_seat(flight_id, num, price, headphones_price, champagne_price,
             food_price):
    query = """INSERT into seats
    (flight_id, num, headphones, champagne, food, price, sold)
    values (?, ?, ?, ?, ?, ?, ?)"""

    cursor.execute(
        query, (flight_id, num, 0, 0, 0, price, 0))
    conn.commit()
    add_extras(num, flight_id, headphones_price, champagne_price, food_price)


def add_extras(seat_num, flight_id, headphones_price, champagne_price,
               food_price):
    query = """INSERT into extras
    (seat_num, flight_id, headphones_price, champagne_price, food_price)
    values (?, ?, ?, ?, ?)"""

    cursor.execute(
        query, (seat_num, flight_id, headphones_price, champagne_price,
                food_price))
    conn.commit()


def add_flight(destination, time):
    query = """INSERT into flights
    (destination, time)
    values (?, ?)"""

    cursor.execute(query, (destination, time))
    conn.commit()


def add_promo_code(code, percent):
    query = """INSERT into promo_codes
    (code, percents_discount)
    values (?, ?)"""

    cursor.execute(query, (code, percent))
    conn.commit()


def get_promo_code_percent(promo_code):
    query = "SELECT percents_discount FROM promo_codes WHERE code = ?"
    cursor.execute(query, (promo_code,))
    percent = cursor.fetchone()
    return percent[0]


def get_seat_price(flight_id, seat):
    query = "SELECT price FROM seats WHERE flight_id = ? and num = ?"
    cursor.execute(query, (flight_id, seat))
    price = cursor.fetchone()
    return price[0]


def get_free_runways():
    query = "SELECT id, free_until FROM runway WHERE is_free = ?"
    cursor.execute(query, (1,))
    runways = cursor.fetchall()
    return runways


def get_flights(destination):
    query = "SELECT id, destination, time FROM flights WHERE destination = ?"
    cursor.execute(query, (destination,))
    flights = cursor.fetchall()
    return flights


def get_seats(flight_id):
    query = "SELECT num, sold FROM seats WHERE flight_id = ?"
    cursor.execute(query, (flight_id,))
    seats = cursor.fetchall()
    return seats


def get_extras_prices(flight_id, seat):
    query = """SELECT headphones_price, champagne_price, food_price
    FROM extras WHERE flight_id = ? and seat_num = ?"""
    cursor.execute(query, (flight_id, seat))
    extras_prices = cursor.fetchone()
    return extras_prices


def get_ticket_id(flight_id, seat):
    query = "SELECT id FROM seats WHERE flight_id = ? and num = ?"
    cursor.execute(query, (flight_id, seat))
    ticket_id = cursor.fetchone()
    return ticket_id[0]


def get_destination(flight):
    query = """SELECT destination FROM flights
    WHERE id = ?"""
    cursor.execute(query, (flight,))
    destination = cursor.fetchone()
    return destination[0]


def get_runway(runway_id):
    query = """SELECT is_free, free_until FROM runway
    WHERE id = ?"""
    cursor.execute(query, (runway_id,))
    runway = cursor.fetchone()
    return runway


def set_seat_sold(flight_id, seat_number):
    query = """UPDATE seats SET sold = ?
    WHERE flight_id = ? and num = ?"""
    cursor.execute(query, (1, flight_id, seat_number))

    conn.commit()

    return get_ticket_id(flight_id, seat_number)


def set_extras_to_seat(flight_id, seat, headphones, champagne, food):
    query = """UPDATE seats SET headphones = ?, champagne = ?, food = ?
    WHERE flight_id == ? and num = ?"""
    cursor.execute(query, (headphones, champagne, food, flight_id, seat))

    conn.commit()


def set_permission_given_at_time(runway_number, time):
    query = """UPDATE runway SET free_until = ? WHERE id == ?"""
    cursor.execute(query, (time, runway_number))

    conn.commit()


def is_ticket_taken(flight, seat):
    query = """SELECT sold FROM seats
    WHERE flight_id = ? and num = ?"""
    cursor.execute(query, (flight, seat))
    ticket_sold = cursor.fetchone()
    if ticket_sold[0] == 0:
        return False
    return True


def make_runway_free(runway):
    query = """UPDATE runway SET is_free = ?, free_until = ? WHERE id = ?"""
    cursor.execute(query, (1, "31-12-2050 23:59", runway))

    conn.commit()


def is_promo_code_correct(promo_code):
    query = "SELECT Count(*) FROM promo_codes WHERE code = ?"
    cursor.execute(query, (promo_code,))
    count = cursor.fetchone()
    if count[0] == 0:
        return False
    return True
