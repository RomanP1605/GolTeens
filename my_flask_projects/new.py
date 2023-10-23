from flask import Flask
app = Flask(__name__)
@app.route('/path1')
def path1():
    return 'Path1'
@app.route('/path2')
def path2():
    return 'Path2'
if __name__ == '__main__':
    app.run(debug=True)