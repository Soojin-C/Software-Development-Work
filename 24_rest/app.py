# Soojin Choi
# SoftDev1 pd08
# K24 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib.request

import json
app = Flask(__name__)

@app.route("/")
def home():
    url = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=SXcgvyAUE0NVXPjQiVmHUd6wPidKafhrz9vCgPkU");
    info = url.read()

    dict_info = json.loads(info)
    descrip = dict_info["title"]
    image = dict_info["url"]

    return render_template("home.html", img = image, title = descrip)

if __name__ == "__main__":
    app.debug = True
    app.run()
