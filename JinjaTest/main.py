from flask import Flask, render_template
import random

app = Flask(__name__)
shoppings = ['apples', 'oranges', 'milk', 'butter']
restaurant = {
    'pizza':['margarita', 'tonna', 'suprema'],
    'coffee':['Capuccino', 'Espresso', 'Americano']
}

@app.route('/')
def main():
    rand = random.random()
    return render_template("ain.html", rand=rand)

@app.route('/shop')
def shop():
    return render_template("shop.html", shoppings=shoppings)

@app.route('/rest')
def rest():
    return render_template("restaurant.html", restaurant=restaurant)

if __name__ == '__main__':
    app.run(debug=True)

