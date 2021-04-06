from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField ,BooleanField,SubmitField
from wtforms.validators import DataRequired, Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    email = StringField('email',validators=[DataRequired(),Email()])
    submit = SubmitField('sign up')


class LoginForm(FlaskForm):
    password = PasswordField('password',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired(),Email()])
    remember = BooleanField('remember me')
    submit = SubmitField('login up')

    
