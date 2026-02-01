import os
import psycopg2
import random


DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS test_data (
    id SERIAL PRIMARY KEY,
    value INTEGER
);
""")


for _ in range(2):
    value = random.randint(1, 100)
    cur.execute("INSERT INTO test_data (value) VALUES (%s);", (value,))

conn.commit()


cur.execute("SELECT * FROM test_data;")
rows = cur.fetchall()
print("Current data in table:")
for row in rows:
    print(row)

cur.close()
conn.close()
