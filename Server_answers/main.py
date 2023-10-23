from flask import Flask, render_template, make_response, url_for, request

app = Flask(__name__)

menu = [{'title':'Main','url':'/'},
        {'title':'Add post','url':'/add_post'}]

@app.route('/')
def index():
    # res=make_response('<h1>Error Server<h1>', 500)
    # img = None
    # with app.open_resource(app.root_path + '/static/images/ava.png', mode='rb') as f:
    #     img = f.read()
    #     if img is None:
    #         return 'No image'
    #     res = make_response(img)
    #     res.headers['Content-Type'] = 'text/plain'
    return '<h1> Main page </h1>'

@app.route('/login')
def login():
    log=''
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')
    res=make_response(f'<h1>Form autorization</h1><p>logged:{log}')
    res.set_cookie('logged','yes')
    return res


if __name__ == '__main__':
    app.run(debug=True)
