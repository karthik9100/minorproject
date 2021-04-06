# from flask import Flask, render_template,url_for
# from forms import RegistrationForm,LoginForm
# app = Flask(__name__)
# app.config['SECRET_KEY']='e5e35fa0bf4eb12ad59f673c0b11ab05'
# @app.route("/first")



# def first():
# 	posts = [
# 		{
# 			'author':'mark',
# 			'posted_on':'20-10-2020',
# 			'desc':'this is regarding a post1'
# 		},
# 		{
# 			'author':'jukerberg',
# 			'posted_on':'21-10-2020',
# 			'desc':'this is regarding a post2'
# 		}
# 	]
# 	return render_template("first.html",posts=posts)

# @app.route("/about")
# def about():
# 	return render_template("about.html",title='about')

# @app.route("/register")
# def register():
# 	form = RegistrationForm()
# 	return render_template('register.html',title = 'register',form=form)

# @app.route("/login")
# def login():
# 	form = LoginForm()
# 	return render_template('login.html',title = 'login',form=form)

# if __name__ == '__main__':
# 	app.run(debug=1)

from markupsafe import escape
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/about")
def about():
	return "about us"


@app.route("/register/")
def register():
	return render_template("register.html",title="Register")


@app.route("/login", methods = ["GET","POST"])
def login():
	return render_template("login.html",title = "Login")

@app.route("/home")
def home():
	return render_template("home.html",title = "Home")
if __name__ == "__main__":
	app.run(debug = True)
	
