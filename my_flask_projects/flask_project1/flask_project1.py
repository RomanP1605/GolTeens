from flask import Flask,render_template
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/CrossZero')
def CrossZero():
    return render_template('CrossGame.html')

@app.route('/projects/telebot')
def telebot():
    return render_template('telebot.html')

if __name__ == '__main__':
    app.run(debug=True)