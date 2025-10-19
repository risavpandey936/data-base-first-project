import mysql.connector

# Database connection parameters
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "movie_ticket_db"

def connect_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def add_movie(name, genre, duration, language):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO movies (name, genre, duration, language) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, genre, duration, language))
    conn.commit()
    cursor.close()
    conn.close()

def add_theatre(name, location, capacity):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO theatres (name, location, capacity) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, location, capacity))
    conn.commit()
    cursor.close()
    conn.close()

def add_show(movie_id, theatre_id, show_time, price):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO shows (movie_id, theatre_id, show_time, price) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (movie_id, theatre_id, show_time, price))
    conn.commit()
    cursor.close()
    conn.close()

def add_customer(name, email, phone):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, email, phone))
    conn.commit()
    cursor.close()
    conn.close()

def book_ticket(customer_id, show_id, num_tickets, booking_date):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO tickets (customer_id, show_id, num_tickets, booking_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (customer_id, show_id, num_tickets, booking_date))
    conn.commit()
    cursor.close()
    conn.close()


