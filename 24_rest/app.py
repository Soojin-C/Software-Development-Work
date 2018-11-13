from flask import Flask
import urllib.request
app = Flask(__name__)

@app.route("/")
def index():
    urllib.request.urlopen("");
    
    return "hello world"
    
if __name__ == "__main__":
    app.debug = True
    app.run()
