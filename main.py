#import pandas as pd
#from flask import Flask , request,jsonify,render_template
#import requests
import functions
import database
import log


"""
@app.route('/teachers',methods=['GET','POST'])
def index():
    pointerDB = database.mongoDatabase(dbname='ineuron', collections='teachers')
    teachersList=[]
    for i in pointerDB.getCollection():
        teachersList.append(i)
    df = pd.DataFrame(teachersList)
    df = df[['Name','Email','Bio']]
    return render_template('teachers.html',teachers=df)
"""

#Scrapper
class scrapping:
    try:
        # creating object of log class
        lg = log.logFile()

        # creating object of functions class
        pointer = functions.ufunc()
        ineuronbaseURL = pointer.getBaseURL()
        ineuronCourses = pointer.getCat()
        ineuronCourseDescription = pointer.getCourseDetails()
        ineuronCoursePrice = pointer.getCoursePrice()
        ineuronInstructors = pointer.getInstructorDetails()
        ineuronCourseURL = pointer.getCourseURL()

        #print(ineuronCourseURL)
        # Database
        try:
            pointerDB = database.mongoDatabase(dbname='ineuron',collections='teachers',documents=ineuronInstructors)
            pointerDB.checkDB()
            pointerDB.createCollection()
            pointerDB.insertDocuments()
        except Exception as e:
            lg.logging.exception(e)

        try:
            pointerDB = database.mongoDatabase(dbname='ineuron',collections='courses',documents=ineuronCourses)
            pointerDB.checkDB()
            pointerDB.createCollection()
            pointerDB.insertDocuments()
        except Exception as e:
            lg.logging.exception(e)

        try:
            pointerDB = database.mongoDatabase(dbname='ineuron',collections='courses_desc',documents=ineuronCourseDescription)
            pointerDB.checkDB()
            pointerDB.createCollection()
            pointerDB.insertDocuments()
        except Exception as e:
            lg.logging.exception(e)

        try:
            pointerDB = database.mongoDatabase(dbname='ineuron',collections='courses_urls',documents=ineuronCourseURL)
            pointerDB.checkDB()
            pointerDB.createCollection()
            pointerDB.insertDocuments()
        except Exception as e:
            lg.logging.exception(e)


        try:
            pointerDB = database.mongoDatabase(dbname='ineuron',collections='pricing',documents=ineuronCoursePrice)
            pointerDB.checkDB()
            pointerDB.createCollection()
            pointerDB.insertDocuments()
        except Exception as e:
            lg.logging.exception(e)

        try:
            for i in ineuronCourseURL:
                ineuronMainTopics = pointer.getMainTopics(i['CourseName'],list(i.values())[1])
                #print(ineuronMainTopics)
                if len(ineuronMainTopics) > 0:
                    pointerDB = database.mongoDatabase(dbname='ineuron', collections='MainTopics', documents=ineuronMainTopics)
                    pointerDB.checkDB()
                    pointerDB.createCollection()
                    lg.logging.info("Inserting data for Main Topic : "+i['CourseName'])
                    pointerDB.insertDocuments()
                else:
                    lg.logging.info("No sub-topics available for data for Main Topic : " + i['CourseName'])

        except Exception as e:
            lg.logging.exception(e)

    except Exception as e:
        lg.logging.exception(e)


