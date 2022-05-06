import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="sundar@2001sql",database="songrecommended")
mycursor = mydb.cursor()
mycursor.execute("select * from happysongs")
result = mycursor.fetchall()
for i in result:
    print(i)
