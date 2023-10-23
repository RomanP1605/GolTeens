from flask import Flask, render_template, request

app = Flask(__name__)

filename = 'data.txt'

poll_data = {
    'question': 'Which web framework do you use?',
    'fields': ['Flask', 'Django']
}

@app.route('/')
def root():
    return render_template("poll.html", data=poll_data)

@app.route('/poll')
def poll():
    vote = request.args.get('field')
    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()
    return render_template("thankyou.html", data=poll_data)

if __name__ == '__main__':
    app.run(debug=True)