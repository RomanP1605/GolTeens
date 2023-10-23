import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Connected to SQLite")
    sqlite_insert_query = """INSERT INTO sqlitedb_developers
    (id, name, email, joining_date, salary)
    VALUES
    (2, 'Roman', 'pautov.roman1605@gmail.com', '2023-01-29', 8100);"""
    count = cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    print("Data already printed in table sqlitedb_developers", cursor.rowcount)
    cursor.close()
except sqlite3.Error as error:
    print('Error with SQLite', error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('Connection closed')