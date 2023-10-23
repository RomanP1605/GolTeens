import sqlite3

def read_sqlite_table(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Connected")
        sqlite_select_query = """SELECT * from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total: ", len(records))
        print("Print all")
        for row in records:
            print("ID:", row[0])
            print("Name:", row[1])
            print("Email:", row[2])
            print("Added:", row[3])
            print("Salary:", row[4], end="\n\n")
        cursor.close()
    except sqlite3.Error as error:
        print("Error when working with SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Connection with SQLite closed")
read_sqlite_table(2)