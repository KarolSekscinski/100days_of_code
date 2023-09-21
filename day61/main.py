from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_bootstrap import Bootstrap5

def is_email(form, field):
    if "@" not in field.data and "." not in field.data:
        raise ValidationError('Email must contain . and @')


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), is_email])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "anystringtokeepsecret"



@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        email = login_form.data['email']
        password = login_form.data['password']
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
