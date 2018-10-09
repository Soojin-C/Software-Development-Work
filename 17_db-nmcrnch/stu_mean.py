# Jiggumbob - Wei Wen Zhou, Soojin Choi
# SoftDev1 pd08
# K17 : Average
# 2018-10-04

import sqlite3
DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

studentGrades = {}

name_id = c.execute("SELECT name, id FROM peeps;")

#Creates a dictionary with the key as the name of the student and holds the value of an array with the students id.
for each_peeps in name_id:

    peepsName = each_peeps[0]
    peepsId = each_peeps[1]
    studentGrades[peepsName] = peepsId

#Loops through the dictionary and pops of the id to retrieve it.
for each in studentGrades:
    #print (each)
    targetID = studentGrades[each]
    #print (targetID)

    info = [targetID]
    grade = []
    id_grades = c.execute("SELECT id, mark FROM courses")  

    #Then loops through the courses table to pull grades that match the student.
    for each_courses in id_grades:
        
        courseId = each_courses[0]
        courseGrade = each_courses[1]
        
        if targetID == courseId:
            grade.append(courseGrade)
    print (grade)
    info.append(grade)

    studentGrades[each] = info

#Prints the grades, Removes the grades of the student and replaces it with the average of the grades.
for each in studentGrades:
    
    average = 0
    counter = 0
    for grade in studentGrades[each].pop():
        average += grade
        counter += 1

    average = average / counter
    #print (average)
    studentGrades[each].append(average)
    #print(studentGrades[each])

def display():
    command = ""
    for student in studentGrades:
        avgGrade = studentGrades[student][1]
        id = studentGrades[student][0]
        command = "Student name: {0} | ID: {1} | Grade: {2}". format(student, id , avgGrade)
        print (command)

display()

def create_table():
    command = "CREATE TABLE grades (id INTEGER PRIMARY KEY, grade INTEGER)"
    c.execute(command)

    for student in studentGrades:
        avgGrade = studentGrades[student][1]
        id = studentGrades[student][0]
        command = "INSERT INTO grades values ({0}, {1})".format(id, avgGrade)
        c.execute(command)

create_table()
    
def add_to_courses(courseName, studentId, mark):
    c.execute("INSERT INTO courses vales (\"{0}\", {1}, {2})".format(courseName, mark, studentId) )
    
