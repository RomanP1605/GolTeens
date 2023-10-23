import sqlite3

def insert_multiple_records(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Connected")
        sqlite_insert_query = """INSERT INTO sqlitedb_developers
        (id, name, email, joining_date, salary)
        VALUES (?,?,?,?,?);"""
        cursor.executemany(sqlite_insert_query, records)
        sqlite_connection.commit()
        print("Record succesfully added to table", cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error when working with SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Connection closed")
records_to_insert = [(6, 'Jaroslav', 'idebylos@gmail.com', '2020-11-14', 8500),
                    (7, 'Tom', 'ullegyddomm@gmail.com', '2020-11-15',6600),
                    (8, 'Nik', 'aqillysso@gmail.com', '2020-11-27', 7400)]
insert_multiple_records(records_to_insert)