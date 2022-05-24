from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(),])
    password = PasswordField("Password", validators=[DataRequired(),])
    submit = SubmitField("Sign In")


class RegisterUserForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(),])
    password = PasswordField("Password", validators=[DataRequired(),])
    password_submit = PasswordField("Password", validators=[DataRequired(), EqualTo("password"),])
    submit = SubmitField("Sign Up")
