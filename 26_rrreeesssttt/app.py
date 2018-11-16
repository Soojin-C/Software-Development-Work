# Soojin Choi
# SoftDev1 pd08
# K26 -- Getting More REST
# 2018-11-15 
from flask import Flask, render_template

import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def home():

    #TOP STORIES API
    key = "f082088a56d24635afdac19812728ba2"
    url = urllib.request.urlopen("http://api.nytimes.com/svc/topstories/v2/home.json?api-key=" + key)
    info = url.read()
    article_info = json.loads(info)
    #print("===============TOP STORIES===============")    
    #print(article_info)
    #print("=========================================")
    article = article_info["results"][2]
    article_img = article["multimedia"][0]

    all_info = [article_info["copyright"], article["title"] ,article["published_date"], article_img["url"], article_img["height"], article_img["width"]]
    
    #The CAT API
    key = "83904938-a6cc-48b7-9d62-a942fa2de88b"
    url = urllib.request.urlopen("https://api.thecatapi.com/v1/images/search?size=full&mime_types=jpg&format=json&order=RANDOM&page=0&limit=10&category_ids&x-api-key=" + key)
    info = url.read()
    cat_info = json.loads(info)
    
    #Google Books
    isbn_num = "0538497815"
    url = urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn_num)
    info = url.read()
    book_info = json.loads(info)
    book = book_info["items"][0]["volumeInfo"]
    
    all_book_info = [book["authors"][0], book["description"], book["averageRating"], book["title"]]
    #print("===============Google Books API===============")    
    #print(article_info)
    #print("=========================================")
    
    return render_template("home.html", nyt_head = all_info, gb = all_book_info, cat_img = cat_info[0]["url"] )

if __name__ == "__main__":
    app.debug = True
    app.run()
