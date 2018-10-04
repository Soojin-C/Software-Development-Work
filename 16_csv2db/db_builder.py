#Team Dx
#Joan Chirinos, Soojin Choi
#SoftDev1 pd08
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

with open('peeps.csv', newline='\n') as peeps:
    #Turns peeps.csv into a DictReader with first row as keys
    peepDictReader = csv.DictReader(peeps)

    #Creates TABLE peeps with name, age, and id
    c.execute("CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")

    #Takes each peep and inputs respective vals into TABLE peeps
    for each in peepDictReader:
        command = "INSERT INTO peeps VALUES('" + each['name'] + "', " + each['age'] + ", " + each['id'] + ");"#build SQL stmt, save as string\
        #print(command)
        #executes SQLite statement
        c.execute(command)

with open('courses.csv', newline='\n') as courses:
    #Turns courses.csv into a DictReader with first row as keys
    courseDictReader = csv.DictReader(courses)

    #Creates TABLE courses with name, mark, and id
    c.execute("CREATE TABLE courses(name TEXT, mark INTEGER, id INTEGER);")

    #Takes each course and inputs respective vals into TABLE peeps
    for each in courseDictReader:
        command = "INSERT INTO courses VALUES('" + each['code'] + "', " + each['mark'] + ", " + each['id'] + ");"#build SQL stmt, save as string\
        #print(command)
        #executes SQLite statement
        c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
