from typing import Counter
import mysql.connector

databaseConnection = mysql.connector.connect(user='p2qc4wz6zc6hbbkb', password='myaslorqvek6c29y',
                              host='eyw6324oty5fsovx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                              database='z4vwcj96hi45ocay')

mycursor = databaseConnection.cursor()

def pushingInfo(username, firstName, lastName, age, sex):
    query = "INSERT INTO {} (firstName, lastName, sex, age) VALUES (%s, %s, %s, %s)".format(username)
    values = (firstName, lastName, sex, age)
    mycursor.execute(query, values)
    databaseConnection.commit()
    print("success!")

def creatingTable(username,firstName, lastName, age, sex, usernameAlreadyExists):
    usernameAlreadyExists = 0

    query = ("show tables like '{}'".format(username))
    mycursor.execute(query)

    for row in mycursor:
        new_lst=(','.join(row))     
        print("Welcome back: " + new_lst)
        usernameAlreadyExists = 1
        pushingInfo(username, firstName, lastName, age, sex)

    if(usernameAlreadyExists == 0):
        print("Creating new table ...")
        mycursor.execute("CREATE TABLE {} (firstName VARCHAR(255), lastName VARCHAR(255), sex VARCHAR(25), age VARCHAR(10))".format(username))
        pushingInfo(username, firstName, lastName, age, sex)

  