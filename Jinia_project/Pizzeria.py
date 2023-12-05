import flask
from flask import Flask, render_template, request
import sqlite3
import flask_wtf
import wtforms

class BestPizza(flask_wtf.FlaskForm):
    best_pizza = wtforms.RadioField('Which pizza did you like the most?')
    rating = wtforms.IntegerField('Rate our pizzeria on a 10-point scale')
    feedback = wtforms.StringField('Your feedback')
    submit = wtforms.SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'


@app.route('/')
def main():
    return render_template('main_pizza.html', title='Veterano Pizza')


connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS PARTICIPANTS (pizza TEXT, count TEXT)')
connect.execute('CREATE TABLE IF NOT EXISTS MENU (pizza_name TEXT, about TEXT, price INTEGER)')
connect.execute('CREATE TABLE IF NOT EXISTS NEWS (main TEXT, about TEXT, time TEXT)')


@app.route('/menu', methods=['POST', 'GET'])
def menu():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM MENU')
    data = sorted(cursor.fetchall())
    if request.method == 'POST':
        pizza = request.form['pizza']
        count = request.form['count']
        with sqlite3.connect('database.db') as users:
            cursor = users.cursor()
            cursor.execute('INSERT INTO PARTICIPANTS (pizza, count) VALUES (?,?)', (pizza, count))
            users.commit()
            return render_template('menu.html')
    else:
        return render_template('menu.html', data=data)


@app.route('/admin', methods=['POST','GET'])
def admin():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM PARTICIPANTS')
    data = cursor.fetchall()
    if request.method == 'POST':
        # Add new pizza
        pizza_name = request.form['pizza_name']
        about = request.form['about']
        price = request.form['price']
        with sqlite3.connect('database.db') as users:
            cursor = users.cursor()
            cursor.execute('INSERT INTO MENU (pizza_name, about, price) VALUES (?,?,?)', (pizza_name, about, price))
            users.commit()
            return render_template('participants.html')
    else:
        return render_template('participants.html', data=data)

@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    data = cursor.fetchall()
    if request.method == 'POST':
        main = request.form['main']
        about_post = request.form['about_post']
        time = request.form['time']
        with sqlite3.connect('database.db') as users:
            cursor = users.cursor()
            cursor.execute('INSERT INTO NEWS (main, about_post, time) VALUES (?,?,?)', (main, about_post, time))
            users.commit()
            return render_template('new_post.html')
    else:
        return render_template('new_post.html', data=data)



@app.route('/vote', methods=['POST', 'GET'])
def vote():
    form = BestPizza()
    form.best_pizza.choices = [('Пеппероні', 'Пеппероні'), ('Маргарита', 'Маргарита')]
    if flask.request.method == 'GET':
        return render_template('poll.html', form=form)
    return form.best_pizza.data


@app.route('/poll', methods=['POST', 'GET'])
def thank():
    return render_template("thankyou.html")


@app.route('/news')
def news():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM NEWS')
    data = cursor.fetchall()
    return render_template('news.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
