from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '15021985'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.195.104.168'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add

@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/add_new_record/")
def add_new():
	cur = mysql.connec
	cur.execute('''INSERT INTO student (studentName, email) values("third student", "third@mail.com")''')

@app.route("/update_info/")
def update_info(): 
	cur = mysql.connection.cursor()
	cur.execute('''UPDATE student SET (studentName=%s, email=%s WHERE  studentName=%s)''',(newfirstName, email1@gmail.com, "first student"))


if __name__ == "__main__":
        app.run(host='0.0.0.0', port='12398') #Run the flask app at port 5000

