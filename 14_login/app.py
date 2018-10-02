#OrangeJuice (Kenny Li & Soojin Choi)
#SoftDev1 Pd8
#K14 -- Do I know you?
#2018-10-1

import os
from flask import Flask, request, render_template, redirect, url_for, session
app = Flask(__name__)

app.secret_key = os.urandom(32) #generates private key

#hard coded username and password
username = "oj"
password = "password"

@app.route("/")
def login():
    if username in session:
        return render_template("template.html", loggedIn = True, username = username) #redirects to welcome page
    else:
        return render_template("template.html", loggedIn = False) #redirects to login page

@app.route("/auth", methods = ["POST"])
def auth():
    if username == request.form["username"]: #checks if username matches
        if password == request.form["password"]: #checks if password matches
            session[username] = username #creates session
            return render_template("template.html", loggedIn = True, username = username) #redirects to welcome page
        else:
            return render_template("template.html", loggedIn = False, error = "Password") #password error
    else:
        if password == request.form["password"]:
            return render_template("template.html", loggedIn = False, error = "Username") #username error
        else:
            return render_template("template.html", loggedIn = False, error = "Username and password") #username and password error

@app.route("/logout", methods = ["POST"])
def logout():
    session.pop(username) #removes session
    return redirect(url_for("login")) #redirects to login

if __name__ == "__main__":
    app.debug = True
    app.run()
