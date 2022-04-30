from app import app, db
print(app)
print(db)
from flask import render_template
from flask import request, Response, redirect, flash, url_for
import json
from app.models import User, Course, Enrolment
from app.forms import LoginForm, RegisterForm

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
  return render_template("index.html", index=True)

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    user_id = User.objects.count()
    user_id += 1
    email = form.email.data
    password = form.password.data
    first_name = form.first_name.data
    last_name = form.last_name.data

    user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()
    flash("You have succesfully registered", "success")
    return redirect(url_for('index'))
  return render_template("register.html", form=form, register=True)

@app.route("/courses")
@app.route("/courses/<term>")
def courses(term=2022):
  classes = Course.objects.order_by("courseID")
  return render_template("courses.html", courseData=classes, courses=True, term=term)

@app.route("/login", methods=["GET", "POST"])
def login():
  form = LoginForm()

  if form.validate_on_submit():
    email = form.email.data
    password = form.password.data

    user = User.objects(email=email).first()
    if user and user.get_password_hash(password):
      flash("You are logged in", "success")
      return redirect("/index")
    else:
      flash("Something went wrong", "danger")
  return render_template("login.html", form=form, title="Login", login=True)

@app.route("/enrollment", methods=['GET', 'POST'])
def enrollment():
  course_id = request.form.get('courseID')
  term = request.form.get('title')
  title = request.form.get('term')
  return render_template("enrollment.html", enrollment=True, data={'id': course_id, 'title': title, 'term': term})


@app.route("/user")
def user():
  User(user_id=1, first_name="Samar", last_name="Manjeshwar", email="sam.manjeshwar@gmail.com", password="qwerty1234").save()
  users = User.objects.all()
  return render_template("users.html", users=users)
  
