from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'student'

mysql = MySQL(app)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       if request.form['action'] == 'StudentView':
            return redirect('/users')
       elif request.form['action'] == 'ProfessorView':
            return redirect('/professor')
       elif request.form['action'] == 'Add':
           userDetails = request.form
           firstname = userDetails['firstname']
           lastname = userDetails['lastname']
           ssn  = userDetails['ssn']
           cur = mysql.connection.cursor()
           cur.execute("INSERT INTO Person (firstname,lastname,ssn) VALUES (%s,%s, %s)", (firstname, lastname, ssn))
           mysql.connection.commit()
           cur.close()

    return render_template('index.html')

@app.route('/users',methods=['GET', 'POST'])
def users():
    cur = mysql.connection.cursor()
    cur.execute("Select firstname,lastname from Person")
    userDetails = cur.fetchall()
    cur.close()
    if request.method == 'POST':
        if request.form['action'] == 'Search':
           userDetails = request.form
           search = userDetails['search']
           cur = mysql.connection.cursor()
           termSearch = str(search)
           termSearch = "'" + termSearch + "'"
           cur.execute("Select firstname, lastname from Person where firstname=" + termSearch)
           userDetails = cur.fetchall()
           cur.close()
           return render_template('users.html', userDetails=userDetails)
        elif request.form['action'] == 'Back':
           return redirect('/')
    return render_template('users.html', userDetails=userDetails)

@app.route('/professor',methods=['GET', 'POST'])
def prof():
    cur = mysql.connection.cursor()
    result = cur.execute("Select * from Person")
    userDetails = cur.fetchall()
    cur.close()

    if request.method == 'POST':
        if request.form['action'] == 'Search':
         userDetails = request.form
         search = userDetails['search']
         cur = mysql.connection.cursor()
         termSearch = str(search)
         termSearch = "'" + termSearch + "'"
         cur.execute("Select firstname, lastname,ssn from Person where firstname=" + termSearch)
         userDetails = cur.fetchall()
         cur.close()
         return render_template('professors.html', userDetails=userDetails)
        elif request.form['action'] == 'Back':
           return redirect('/')
    return render_template('professors.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run()
