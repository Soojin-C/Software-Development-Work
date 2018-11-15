# Soojin Choi
# SoftDev1 pd08
# K25 -- Getting More REST
# 2018-11-14

from flask import Flask, render_template
import urllib.request

import json
app = Flask(__name__)

@app.route("/")
def home():

    #NASA API
    url = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=SXcgvyAUE0NVXPjQiVmHUd6wPidKafhrz9vCgPkU");
    info = url.read()

    nasa_info = json.loads(info)
    descrip = nasa_info["title"]
    nasa_img = nasa_info["url"]

    #SpaceX API
    url = urllib.request.urlopen("https://api.spacexdata.com/v3/launches/latest");
    info = url.read()

    mission_info = json.loads(info)
    #print(dict_info)
    miss_name = mission_info["mission_name"]
    img_space = mission_info["links"]["mission_patch"]
    img_descrip = mission_info["details"]

    return render_template("home.html", title = descrip, main_img = nasa_img, heading = miss_name, space_img = img_space, details = img_descrip)

if __name__ == "__main__":
    app.debug = True
    app.run()
