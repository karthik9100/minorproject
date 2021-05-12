from flaskblog.models import User
from flaskblog import db
from flaskblog import app
from flask import render_template, request, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flask_login import login_user
from scripts import Query

@app.route("/about")
def about():
    return "about us"


@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    
    if request.method == "POST" and form.validate():
        # users = User.query.filter_by(email=form.email.data)
        users = User.query.all()
        # print(*users)
        # for user in users:
        #     print(user)
        # if(users != None):
        #     flash("User already exists!", "error")
        # else:
        user = User(username=form.username.data, email=form.email.data,
                    password=form.password.data, confirm_password=form.confirm_password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created for User "+form.username.data +
                " Now you can Login", "success")
        return redirect(url_for('login'))
    return render_template('registration.html', title="Registeration", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    print(request.method,form.validate())
    if request.method == "POST":
        
        user = User.query.filter_by(email=form.email.data).first()
        print(user.password)
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful!Please enter valid details")
    return render_template("login.html", title="Login", form=form)

@app.route("/home",methods = ["GET","POST"])


@app.route("/home")
def home():
    if(request.method=="POST"):
        item = request.form['search']
        obj = Query()
        obj.scratch(item)
        names,prices,ratings = obj.display(obj.names,obj.prices,obj.ratings)
        
        return render_template("home.html",names = names,prices = prices,ratings = ratings, title="Home",zip = zip)
    return render_template("home.html", title="Home")
