import psycopg2

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

conn.autocommit = True
cur = conn.cursor()

print("Connected to database")