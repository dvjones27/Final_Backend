from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class UserSignUpForm(FlaskForm):
    # email, password, submit, first_name, last_name
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    password = PasswordField('Create Password', validators=[DataRequired()])
    submit_button = SubmitField()
    
class UserSigninForm(FlaskForm):
    # email, password, submit, first_name, last_name
    # email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Enter Password', validators=[DataRequired()])
    submit_button = SubmitField()
