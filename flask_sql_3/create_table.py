import sqlite3

try:
   sqlite_connection = sqlite3.connect('sqlite_python.db')
   sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                               id INTEGER PRIMARY KEY,
                               name TEXT NOT NULL,
                               email text NOT NULL UNIQUE,
                               joining_date datetime,
                               salary REAL NOT NULL);'''

   cursor = sqlite_connection.cursor()
   print("База даних подключена до SQLite")
   cursor.execute(sqlite_create_table_query)
   sqlite_connection.commit()
   print("Таблиця SQLite створена")

   cursor.close()

except sqlite3.Error as error:
   print("Помилка підключення до sqlite", error)
finally:
   if (sqlite_connection):
       sqlite_connection.close()
       print("З’єднання з SQLite закрите")