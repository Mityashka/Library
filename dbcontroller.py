import psycopg2
from configs import host, user, password, db_name


def connect():
    try:
        connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        connection.autocommit = True
        cursor = connection.cursor()
        # print(f"[INFO] successfully connected to database") for developer
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS books (book_id SERIAL PRIMARY KEY, title VARCHAR(50), author VARCHAR(50), year INTEGER, status VARCHAR(20))")
        # print(f"[INFO] table successfully created") for developer
        return connection, cursor
    except Exception as ex:
        print(f"[INFO] error while connecting to database, {ex}")
