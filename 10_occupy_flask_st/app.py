# Choidhury —- Soojin Choi and Raunak Chowdhury
# Softdev1 pd8
# K#10: Jinja Tuning
# 2018-09-23

from flask import Flask, render_template
from occupations import entries, title, total, random_average

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/occupations")
def occupation():
    return render_template("occupations.html", randVal = random_average(), collection = entries, title = title, total = total)

if __name__ == '__main__':
    app.debug = True
    app.run()
