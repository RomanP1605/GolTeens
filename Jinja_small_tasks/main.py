import flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search')
def formsearch():
    return render_template('search.html')


@app.route('/getsearch')
def get_search():
    mail = flask.request.args.get('mail')
    return f'Get searching {mail}'


@app.route('/postsearch', methods=['POST'])
def post_search():
    mail = flask.request.args.get('mail')
    return f'Post searching {mail}'


@app.route('/galaxies')
def galaxies():
    nearby_galaxies = {
        1: {'galaxy': 'Canis Major Dwarf Galaxy',
            'distance_trillionkm': 2360000.3874623787,
            'distance_ly': 25000,
            'description': 'satellite of Milky Way'},
        2: {'galaxy': 'Milky Way',
            'distance_trillionkm': 2230000.008768,
            'distance_ly': 20000,
            'description': 'home galaxy of Earth'},
        3: {'galaxy': 'Large Magellanic Cloud',
            'distance_trillionkm': 2500000.67565002,
            'distance_ly': 160000,
            'description': 'satellite of Milky Way'}
    }
    return render_template('galaxies.html', nearby_galaxies=nearby_galaxies)


if __name__ == '__main__':
    app.run(debug=True)
