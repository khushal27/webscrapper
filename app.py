from flask import Flask,render_template
import database
import pandas as pd
app = Flask(__name__)

@app.route('/',methods=['GET'])
def base():
    return render_template('index.html')

@app.route('/teachers',methods=['GET','POST'])
def guru():
    pointerDB = database.mongoDatabase(dbname='ineuron', collections='teachers')
    teachersList = []
    for i in pointerDB.getCollection():
       teachersList.append(i)
    return render_template('teachers.html',teachers=teachersList)

if __name__=='__main__':
    app.run(debug=True)