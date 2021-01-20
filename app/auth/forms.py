from app.models import User


from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import Regexp
from wtforms import StringField
from wtforms import SelectMultipleField
from wtforms import SelectField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import ValidationError
from wtforms import IntegerField
from wtforms import TextAreaField
from wtforms import RadioField
from wtforms.validators import EqualTo

class RegistrationForm(FlaskForm):
    gender_choices = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    first_name = StringField("First name", validators=[DataRequired()])
    middle_name = StringField("Middle name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    gender = RadioField("Gender", validators=[DataRequired()], choices=gender_choices)
    password = PasswordField("Password", validators=[DataRequired(), Length(6,12), Regexp('^[A-Za-z0-9][a-z0-9._]*$',message='Password must contain a nuber underscore or a dot')])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(6,12), EqualTo('password')])
    submit = SubmitField("Create Account")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already exists')

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(6,12), Regexp('^[A-Za-z0-9][a-z0-9._]*$',message='Password must contain a nuber underscore or a dot')])
    submit = SubmitField("Login")
