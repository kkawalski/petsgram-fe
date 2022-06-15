from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ProfileForm(FlaskForm):
    avatar = FileField("Avatar")
    first_name = StringField("First Name", validators=[DataRequired(), ])
    last_name = StringField("Last Name", validators=[DataRequired(), ])
    description = TextAreaField("Description")
    submit = SubmitField("Create")
