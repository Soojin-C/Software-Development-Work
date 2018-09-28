# Soojin Choi
# SoftDev1 pd08
# K13 -- Echo Echo Echo
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
# renders the template for a form
def form():
    print (app)
    return render_template("template.html", request = "form")

# requests the value that is associated with "username"
# renders the template for the output of method and greeting.
@app.route("/auth")
def authenticate():
    # testing each request: 
    print ("request.args: " )
    print ( request.args )
    print ( "\n ------------")

    print ("request.headers: " )
    print ( request.headers )
    print ( "\n -----------")

    print ("request.form: " )
    print ( request.form )
    print ( "\n -----------")

    username = request.args["username"]
    
    return render_template("template.html", request = "output", user = username, method = request.method)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
