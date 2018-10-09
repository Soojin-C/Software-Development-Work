#Jiggumbob - Wei Wen Zhou, Soojin Choi 
#SoftDev1 pd8
#K #17: Average
#2018-10-04

# Jiggumbob - a thingamabob; a gadget; a whatsit; a gewgaw 1

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE courses (name TEXT, mark INTEGER, id INTEGER);"
#build SQL stmt, save as string

c.execute(command)    #run SQL statement

with open('courses.csv') as file:
    courses = csv.DictReader(file)
    for row in courses:
        command = 'INSERT INTO courses values ("{0}", {1}, {2})'.format(row['code'], row['mark'], row['id'])
        #print(row['code'], row['mark'], row['id'])
        c.execute(command)    #run SQL statement

command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);"
c.execute(command)    #run SQL statement

with open('peeps.csv') as file:
    peeps = csv.DictReader(file)
    for row in peeps:
        command = 'INSERT INTO peeps values ("{0}", {1}, {2})'.format(row['name'], row['age'], row['id'])
        #print(row['name'], row['age'], row['id'])
        c.execute(command)    #run SQL statement


#==========================================================

db.commit() #save changes
db.close()  #close database


