import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print('DataBase created and connected')
    sqlite_select_query = "select sqlite_version()"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print('Version DataBase SQLite:', record)
    cursor.close()
except sqlite3.Error as error:
    print("Error connecting to", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Connection with SQLite closed")