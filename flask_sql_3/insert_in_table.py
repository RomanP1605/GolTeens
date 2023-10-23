import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База даних подключена до SQLite")
    sqlite_insert_query = """INSERT INTO sqlitedb_developers
                            (id, name, email, joining_date, salary)
                            VALUES
                            (3, 'Roman', 'pautov.roman1605@gmail.com', '2023-01-29', 8100);"""
    count = cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    print("Записано в таблицю", cursor.rowcount)

    cursor.close()

except sqlite3.Error as error:
    print("Помилка при роботі", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("З’єднання з SQLite закрите")
