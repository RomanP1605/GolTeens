from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    country = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    pr = db.relationship('Profiles', backref='users', uselist=False)

    def __repr__(self):
        return f'<users {self.id}>'


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<users {self.id}>'


with app.app_context():
    db.create_all()

with app.app_context():
    print(Users.query.all())
    res = Users.query.all()
    f = Users.query.first()
    print(res)
    print(res[0].email)
    print(f)
    print(f.id)
    print(Users.query.filter_by(id=1).all())
    print(Users.query.filter(Users.id == 1).all())
    print(Users.query.filter(Users.id > 1).all())
    Users.query.limit(2).all()
    Users.query.order_by(Users.email).all()
    Users.query.order_by(Users.email.desc()).all()
    Users.query.get(2)
    res = db.session.query(Users, Profiles).join(Profiles, Users.id == Profiles.user_id).all()
    print(res)
    print(res[0].Users.email)
    print(res[0].Profiles.name)


@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == 'POST':
        try:
            hash = generate_password_hash(request.form['psw'])
            u = Users(email=request.form['email'], psw=hash)
            db.session.add(u)
            db.session.flush()
            p = Profiles(name=request.form['name'], old=request.form['old'], city=request.form['city'], user_id=u.id)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print('Error')
    return render_template("register.html", title="REGISTRATION")


@app.route("/")
def index():
    info = []
    try:
        info = Users.query.all()
    except:
        print('Error reading DB')
    return render_template('index.html', title='MAIN', list=info)


if __name__ == '__main__':
    app.run(debug=True)
