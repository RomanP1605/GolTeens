import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('помилка читання бд')
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?,?,?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Помилка додавання публікації в БД" + str(e))
            return False
        return True

    def getPost(self, postID):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE id={postID} LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Error earning post from db')
        return (False, False)

    def getPostsAnonce(self):
        try:
            self.__cur.execute(f'SELECT id,title,text FROM posts ORDER BY time DESC')
            res=self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Error earning posts from db')
            return []

    def addUser(self, name, email, psw):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count']>0:
                print('Користувач вже існує')
                return False
            tm=math.floor(time.time())
            self.__cur.execute('INSERT INTO users VALUES(NULL, ?,?,?,?)',(name, email,psw,tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Помилка додавання користувача в БД'+str(e))
            return False
        return True

    def getUser(self, user_id):
        try:
            self.__cur.execute(f'SELECT * FROM users WHERE id={user_id} LIMIT 1')
            res = self.__cur.fetchone()
            if not res:
                print('Користувача не знайдено')
                return False
            return res
        except sqlite3.Error as e:
            print('Помилка отримання даних з БД'+str(e))
        return False

    def getUserByEmail(self,email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email='{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('Користувача не знайдено')
                return False
            return res
        except sqlite3.Error as e:
            print('Помилка отримання даних з БД'+ str(e))
        return False