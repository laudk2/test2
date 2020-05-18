import mysql.connector


db = mysql.connector.connect(
   host="localhost",
   user='root',
   passwd="root",
   db= 'student'

    )

#mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE student")
#mycursor.execute("CREATE TABLE Person (firstname VARCHAR (50), lastname VARCHAR(50),ssn int Primary key)")
#mycursor.execute("INSERT INTO Person (firstname,lastname,ssn) VALUES (%s,%s, %s)", ("Tim","bob", 19))
#db.commit()
#mycursor.execute("select * from Person")
#mycursor.execute("DESCRIBE Person")

