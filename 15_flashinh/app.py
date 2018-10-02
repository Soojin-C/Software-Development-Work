#OrangeJuice (Kenny Li & Soojin Choi)
#SoftDev1 pd08
#K15 -- Oh yes, perhaps I do...
#2018-10-02

import os
from flask import Flask, request, render_template, redirect, url_for, session, flash
app = Flask(__name__)

app.secret_key = os.urandom(32) #generates private key

#hard coded username and password
username = "oj"
password = "password"

@app.route("/")
def login():
    if username in session:
        return render_template("welcome.html", username = username) #redirects to welcome page
    else:
        return render_template("login.html") #redirects to login page

@app.route("/auth", methods = ["POST"])
def auth():
    if username == request.form["username"]: #checks if username matches
        if password == request.form["password"]: #checks if password matches
            session[username] = username #creates session
            # return render_template("template.html",  username = username) #redirects to welcome page
        else:
            flash( "Password ") #password error
    else:
        if password == request.form["password"]:
            flash ("Username ") #username error
        else:
            flash("Username and password ") #username and password error
    return redirect (url_for("login")) #redirects to login

@app.route("/logout", methods = ["POST"])
def logout():
    session.pop(username) #removes session
    return redirect(url_for("login")) #redirects to login

if __name__ == "__main__":
    app.debug = True
    app.run()
