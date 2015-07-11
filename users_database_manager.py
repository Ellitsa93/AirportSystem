import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()


def create_tables():
    create_admins_table()
    create_passengers_table()
    create_rich_clients_table()
    create_user_destinations_table()
    create_master_codes_table()
    create_users_tickets_table()


def create_users_tickets_table():
    query = """CREATE TABLE IF NOT EXISTS
        users_tickets(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            ticket_num INTEGER NOT NULL)"""
    cursor.execute(query)


def create_master_codes_table():
    query = """CREATE TABLE IF NOT EXISTS
        master_codes(code INTEGER NOT NULL PRIMARY KEY)"""
    cursor.execute(query)


def create_user_destinations_table():
    query = """CREATE TABLE IF NOT EXISTS
        user_destinations(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            destination TEXT NOT NULL,
            times INTEGER NOT NULL)"""

    cursor.execute(query)


def create_rich_clients_table():
    query = """CREATE TABLE IF NOT EXISTS
        rich_client(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            plane_name TEXT NOT NULL)"""

    cursor.execute(query)


def create_admins_table():
    query = """CREATE TABLE IF NOT EXISTS
        admins(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL)"""

    cursor.execute(query)


def create_passengers_table():
    query = """CREATE TABLE IF NOT EXISTS
        passengers(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL)"""

    cursor.execute(query)


def add_master_code(code):
    query = "INSERT INTO master_codes(code) values (?)"
    cursor.execute(query, (code,))
    conn.commit


def add_passenger(name, password, email):
    query = """INSERT INTO passengers
    (username, password, email)
    values (?, ?, ?)"""

    cursor.execute(query, (name, password, email))
    conn.commit()


def add_administrator(name, password):
    query = """INSERT into admins
    (username, password)
    values (?, ?)"""

    cursor.execute(query, (name, password))
    conn.commit()


def add_rich_client(name, password, plane_name):
    query = """INSERT into rich_client
    (username, password, plane_name)
    values (?, ?, ?)"""

    cursor.execute(query, (name, password, plane_name))
    conn.commit()


def add_user_destination(name, destination):
    query = """INSERT into user_destinations
    (username, destination, times)
    values (?, ?, ?)"""

    cursor.execute(query, (name, destination, 1))
    conn.commit()


def add_user_ticket(username, ticket_id):
    query = """INSERT into users_tickets
    (username, ticket_num)
    values (?, ?)"""

    cursor.execute(query, (username, ticket_id))
    conn.commit()


def get_travels(name, destination):
    query = """SELECT times FROM user_destinations WHERE username = ? and
    destination = ?"""
    cursor.execute(query, (name, destination))
    times = cursor.fetchone()
    if times is None:
        return 0
    return times[0]


def get_best_destination(name):
    query = """SELECT destination FROM user_destinations WHERE username = ?
    ORDER BY times"""
    cursor.execute(query, (name, ))
    destinations = cursor.fetchone()
    if destinations is None:
        return ""
    return destinations[0]


def get_admin(username):
    query = "SELECT username FROM admins WHERE username = ?"
    cursor.execute(query, (username,))
    admin = cursor.fetchone()
    return admin


def get_passenger(username):
    query = "SELECT username FROM passengers WHERE username = ?"
    cursor.execute(query, (username,))
    passenger = cursor.fetchone()
    return passenger


def get_rich_client(username):
    query = "SELECT username FROM rich_client WHERE username = ?"
    cursor.execute(query, (username,))
    rich_client = cursor.fetchone()
    return rich_client

def get_email(username):
    query = "SELECT email FROM passengers WHERE username = ?"
    cursor.execute(query, (username,))
    email = cursor.fetchone()
    return email[0]


def increase_user_destination(name, destination):
    travels = get_travels(name, destination)
    if travels == 0:
        add_user_destination(name, destination)
    else:
        query = """UPDATE user_destinations SET times = ?
            WHERE username = ? and destination = ?"""

        cursor.execute(query, (travels + 1, name, destination))
        conn.commit()


def check_code(code):
    query = "SELECT code FROM master_codes WHERE code = ?"
    cursor.execute(query, (code,))
    code = cursor.fetchone()
    if code is None:
        return False
    return True


def check_ticket(ticket_id, user):
    query = """SELECT username FROM users_tickets
    WHERE ticket_num = ? and username = ?"""
    cursor.execute(query, (ticket_id, user))
    user_ticket = cursor.fetchone()
    if user_ticket is not None:
        return True
    return False
