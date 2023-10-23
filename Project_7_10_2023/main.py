import sqlite3
import os
from flask import Flask, render_template, request, g, flash, redirect, url_for
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = '/tmp/main_app.db'
DEBUG = True
SECRET_KEY = '5544'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'main_app.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
        return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


dbase = None


@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.route('/')
def index():
    # db = get_db()
    # dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.getMenu(), posts=dbase.getPostsAnonce())


@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    # db = get_db()
    # dbase=FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'])
            if not res:
                flash('Помилка додавання статті', category='error')
            else:
                flash('Статтю додано', category='success')
        else:
            flash('Помилка додавання статті', category='error')
    return render_template('add_post.html', menu=dbase.getMenu(), title='Додавання статті')


@app.route("/post/<int:id_post>")
def showPost(id_post):
    # db=get_db()
    # dbase=FDataBase(db)
    title, post = dbase.getPost(id_post)
    if not title:
        os.abort(404)
    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


@app.route('/login')
def login():
    return render_template('login.html', menu=dbase.getMenu(), title='Авторизація')


@app.route("/register", methods=['POST','GET'])
def register():
    if request.method == "POST":
        if len(request.form['name'])>4 and len(request.form['email'])>4 \
            and len(request.form['psw'])>4 and request.form['psw'] == request.form['psw2']:
            hash=generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'],hash)
            if res:
                flash('Ви успішно зареєстровані','success')
                return redirect(url_for("login"))
            else:
                flash('Помилка додавання в БД', 'error')
        else:
            flash('Неправильно заповнені поля', 'error')

    return render_template("register.html", menu=dbase.getMenu(), title="Реєстрація")


if __name__ == '__main__':
    app.run(debug=True)
