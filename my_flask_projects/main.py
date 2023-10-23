from flask import Flask,url_for,request,send_file,redirect,abort
app = Flask(__name__)

@app.route('/url_for_test')
def url_for_test():
    return url_for('main_page')

@app.route('/goods')
def main_page():
    return send_file('goods.html')

@app.route('/index')
def atb():
    return send_file('index.html')

@app.route('/summer')
def summer():
    return send_file('image.html')

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s' % name

@app.route('/dir/<int:item_id>')
def dir_item(item_id):
    item_id = item_id*3
    return 'Number : %d' % item_id

@app.route('/versions/<float:version>')
def versions(version):
    version = version/100
    return 'Version: %f' % version

@app.route('/authorization')
def send_login():
    return send_file('login.html')

@app.route('/redirect-to-login-page')
def redirected():
    return redirect(url_for('send_login'))

@app.route('/aborted-page')
def aborted_page():
    abort(401)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.method == ['name']
        return 'Request method POST, sended number: %s' % user
    else:
        user = request.args.get('name')
        return 'Request method GET, sended number: %s' % user

@app.errorhandler(404)
def page_not_found(error):
    return 'Такої сторінки нема', 404

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('atb'))
        print(url_for('summer'))
        print(url_for('main_page'))
    app.run(debug=True)