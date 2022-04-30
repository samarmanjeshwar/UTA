from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from app.models import User

class LoginForm(FlaskForm):
  email = StringField("Email", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=10)])
  remember_me = BooleanField("Remember me")
  submit = SubmitField("Login")

class RegisterForm(FlaskForm):
  email = StringField("Email", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])
  password_confirm = PasswordField("Confirm password", validators=[DataRequired(), EqualTo('password')])
  first_name = StringField("First name", validators=[DataRequired()])
  last_name = StringField("Last name", validators=[DataRequired()])
  submit = SubmitField("Register now", validators=[DataRequired()])

  def validate_email(self, email):
    user = User.objects(email=email.data).first()
    if user:
      raise ValidationError("Email already in use")
