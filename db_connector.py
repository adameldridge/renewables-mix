import sqlite3


def create_connection():

    database = "energy.db"

    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

    return None