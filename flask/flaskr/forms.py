from flask_wtf import Flaskform
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    # Username field cannot be empty with DataRequired() and length limited with Length()
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validoators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
