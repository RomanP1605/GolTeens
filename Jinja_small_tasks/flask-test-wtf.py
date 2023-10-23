import flask
import flask_wtf
import wtforms
class SubscriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('Name')
    email = wtforms.StringField('Email')
    test = wtforms.PasswordField('Password')
    submit = wtforms.SubmitField('Submit')

class IceCreamForm(flask_wtf.FlaskForm):
    tastes = wtforms.SelectField('Taste')
    topping = wtforms.SelectMultipleField('Topping')
    cup_size = wtforms.RadioField('Cup')
    submit = wtforms.SubmitField('Submit')

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route('/subscribe/', methods=['GET', 'POST'])
def subscribe():
    form = SubscriptionForm()
    if flask.request.method == "GET":
        return flask.render_template('subscription.html', form=form)
    return form.name.data

@app.route('/ice', methods=['GET', 'POST'])
def ice():
    form = IceCreamForm()
    form.tastes.choices = [('vanilla', 'vanilla'), ('choko', 'choko'), ('mango', 'mango')]
    form.topping.choices = [('coffee', 'coffee'), ('coffee', 'coffee'), ('strawbery', 'strawbery')]
    form.cup_size.choices = [('cornet', 'cornet'), ('paper', 'paper'), ('chokolate', 'chokolate')]
    if flask.request.method == 'GET':
        return flask.render_template('ice.html', form=form)
    return form.tastes.data

if __name__ == '__main__':
    app.run(debug=True)