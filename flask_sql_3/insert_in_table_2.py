import sqlite3

def insert_variable_into_table(dev_id, name, email, join_date, salary):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("База даних подключена до SQLite")
        sqlite_insert_with_param = """INSERT INTO sqlitedb_developers
                                (id, name, email, joining_date, salary)
                                VALUES
                                (?,?,?,?,?);"""
        data_tuple = (dev_id, name, email, join_date, salary)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Змінні успішно вставлені в таблицю sqlitedb_developers", cursor.rowcount)

        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("З’єднання з SQLite закрите")

insert_variable_into_table(4, 'Nelly', 'nel@gmail.com', '2023-07-16', 6000)
insert_variable_into_table(5, 'Grig', 'gr@gmail.com', '2023-07-16', 6500)
