import flask
import flask_wtf
import wtforms


class RegistForm(flask_wtf.FlaskForm):
    email = wtforms.EmailField('Email')
    password = wtforms.PasswordField('Password')
    submit = wtforms.SubmitField('Submit')

def is_luggage_weight_valid(form,field):
    if field.data>30:
        raise wtforms.validators.ValidationError('Weight to big')


class LuggForm(flask_wtf.FlaskForm):
    surname = wtforms.StringField('Surname',validators = [wtforms.validators.InputRequired()])
    name = wtforms.StringField('Name', validators = [wtforms.validators.InputRequired()])
    pass_id = wtforms.IntegerField('Passport number', validators = [wtforms.validators.InputRequired()])
    luggage_weight = wtforms.IntegerField(
        'Weight baggage',
        validators=[
            wtforms.validators.InputRequired(),
            is_luggage_weight_valid
        ]
    )
    submit = wtforms.SubmitField('Send', validators = [wtforms.validators.InputRequired()])


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = '1234'



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistForm()
    if flask.request.method == "GET":
        return flask.render_template('registration.html', form=form)
    return form.email.data

@app.route('/luggage', methods=['GET', 'POST'])
def lugagge():
    form = LuggForm()
    if flask.request.method == 'GET':
        return flask.render_template('luggage.html', form=form)
    if form.validate_on_submit():
        return 'ok'
    else:
        return f'{form.errors}'


if __name__ == '__main__':
    app.run(debug=True)
