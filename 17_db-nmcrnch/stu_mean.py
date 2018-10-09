# Jiggumbob - Wei Wen Zhou, Soojin Choi
# SoftDev1 pd08
# K17 : Average
# 2018-10-04

import sqlite3
DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

#dictionary that holds all the students' data
studentGrades = {}

#looks up the students grade and keeps them.
#studentsGrades should be studentName : [id , [grades...]]
def look_up():
    name_id = c.execute("SELECT name, id FROM peeps;")

    #loops through to get the keys and id for each student
    for each_peeps in name_id:

        peepsName = each_peeps[0]
        peepsId = each_peeps[1]
        studentGrades[peepsName] = peepsId

    #loops through the dictionary and pulls the id data 
    for each in studentGrades:
        targetID = studentGrades[each]

        info = [targetID]
        grade = []
        id_grades = c.execute("SELECT id, mark FROM courses")  

        #Then loops through the courses table to pull grades that match the student's id.
        for each_courses in id_grades:
        
            courseId = each_courses[0]
            courseGrade = each_courses[1]
        
            if targetID == courseId:
                grade.append(courseGrade)
            
        info.append(grade)
        studentGrades[each] = info

look_up()

#Removes the grades of the student and replaces it with the average of the grades.
# studentGrades should be studentName : [id , avgGrade]
def avg_grade():
    for each in studentGrades:
    
        average = 0
        counter = 0
        for grade in studentGrades[each].pop():
            average += grade
            counter += 1

            #calculates the avg
            average = average / counter
            studentGrades[each].append(average)

avg_grade()

#displays the student's name, id and average grade
def display():
    command = ""
    for student in studentGrades:
        avgGrade = studentGrades[student][1]
        id = studentGrades[student][0]
        command = "Student name: {0} | ID: {1} | Grade: {2}". format(student, id , avgGrade)
        print (command)

display()

#creates a table ,peeps_avg, that inserts the values of id and avgGrade
def create_table():
    command = "CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, grade INTEGER)"
    c.execute(command)

    for student in studentGrades:
        avgGrade = studentGrades[student][1]
        id = studentGrades[student][0]
        command = "INSERT INTO peeps_avg values ({0}, {1})".format(id, avgGrade)
        c.execute(command)

create_table()

#adds to the courses table, a course name, student id and mark as one row.
def add_to_courses(courseName, studentId, mark):
    c.execute("INSERT INTO courses vales (\"{0}\", {1}, {2})".format(courseName, mark, studentId) )
    
