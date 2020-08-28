from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from app.models import User

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')

    def validation_username(self, username):
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            raise ValidationError('The Username is already taken')

    def validation_email(self, email):
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            raise ValidationError('The Username is already taken')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')