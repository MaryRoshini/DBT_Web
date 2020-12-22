from flask import Flask, render_template
import jinja2

#THIS IS TO ESTABLISHING THE CONNECTION WITH  DB
####import mysql.connector

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-GDPUM2LD\SQLEXPRESS;'
                      'Database=Payroll;'
                      'Trusted_Connection=yes;')
#THIS IS TO SET   THE FLASK PROPERTY
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('first_home.html')
app = Flask(__name__)

if __name__ == '__main__':
    app.run()
   
 


@app.route('/list_user')
def list_view():
    mycursor=conn.cursor()
    mycursor.execute("select * from Employee")
    response=mycursor.fetchall()
    return render_template('first_home.html',response=response)
    





