import flask
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
  user_id = db.IntField(unique=True)
  first_name = db.StringField(unique=True)
  last_name = db.StringField(unique=True)
  email = db.StringField(unique=True)
  password = db.StringField(unique=True)
  
  def set_password(self, password):
    self.password = generate_password_hash(password)

  def get_password_hash(self, password):
    return check_password_hash(self.password, password)

class Course(db.Document):
  courseID = db.StringField(unique=True, max_length=10)
  title = db.StringField(max_length=100)
  description = db.StringField(max_length=255)
  credits = db.IntField()
  term = db.StringField(max_length=25)

class Enrolment(db.Document):
  user_id = db.IntField()
  course_id = db.StringField(max_length=10)
