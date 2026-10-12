import os
from pathlib import Path

import pymysql
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

connection = pymysql.connect(
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"],
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        print("Connected to:", cursor.fetchone()[0])
        cursor.execute("SHOW TABLES;")
        print("Tables:")
        for row in cursor.fetchall():
            print("-", row[0])
finally:
    connection.close()
