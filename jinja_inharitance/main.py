from flask import Flask, render_template
app = Flask(__name__)

max_score = 175
test_name = "Python Challenge"
students = [
    {"name": "Яблуко", "score": 55},
    {"name": "Ананас", "score": 175},
    {"name": "Груша", "score": 89},
    {"name": "Вишня", "score": 67},
    {"name": "Клубніка", "score": 80},
]

@app.route('/')
def index():
    return render_template('base.html', title='jinjia2 and Flask')

@app.route('/results')
def results():
    context={
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    return render_template("results.html", **context)

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

if __name__ == '__main__':
    app.run(debug=True)