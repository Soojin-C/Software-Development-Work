# Choidhury —- Soojin Choi and Raunak Chowdhury
# Softdev1 pd8
# K#10: Jinja Tuning
# 2018-09-23

from flask import Flask, render_template
from util.occupations import entries, title, total, random_average

app = Flask(__name__)

# The home route 
@app.route("/")
def index():
    return "Hello world!"

# occupations route
@app.route("/occupations")
def occupation():
    # randVal is the random occupation
    # collection, title and total are passed in
    return render_template("occupations.html",
                            randVal = random_average(),
                            collection = entries,
                            title = title,
                            total = total)

if __name__ == '__main__':
    app.debug = True
    app.run()
