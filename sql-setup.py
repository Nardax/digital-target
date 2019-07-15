import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)

        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS PinValue (Id integer PRIMARY KEY, [Value] integer NOT NULL);")

        pinValue = (5, 255)
        c.execute("INSERT INTO PinValue VALUES(?,?);", pinValue)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
if __name__ == '__main__':
    create_connection("/home/pi/repos/digital-target/data.db")