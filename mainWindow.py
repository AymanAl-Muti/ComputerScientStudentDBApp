from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from pushInformation import *

class Ui_MainWindow(object):
    usernmame = ''

    def showNextWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = modifyStudents()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 455)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        #Welcome text
        self.sText = QtWidgets.QLabel(self.centralwidget)
        self.sText.setGeometry(QtCore.QRect(152, 50, 282, 41))
        self.sText.setFont(QtGui.QFont('Arial', 12))
        self.sText.setObjectName("sText")
        self.sText.setText("Welcome! Please enter the students info")

        #username text
        self.usernameText = QtWidgets.QLabel(self.centralwidget)
        self.usernameText.setGeometry(QtCore.QRect(259, 95, 282, 41))
        self.usernameText.setFont(QtGui.QFont('Arial', 10))
        self.usernameText.setObjectName("usernameText")
        self.usernameText.setText("username")
        
        #username in order to access the table.
        self.usernameDatabase= QtWidgets.QLineEdit(self.centralwidget)
        self.usernameDatabase.setGeometry(QtCore.QRect(215, 130, 141, 16))
        self.usernameDatabase.setObjectName("usernameDatabase")
        username = self.usernameDatabase.text()

        #First Name
        self.firstNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNameInput.setGeometry(QtCore.QRect(10, 170, 141, 16))
        self.firstNameInput.setObjectName("firstNameInput")

        #Last Name
        self.lastNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.lastNameInput.setGeometry(QtCore.QRect(170, 170, 141, 16))
        self.lastNameInput.setObjectName("lastNameInput")

        #Gender Menu
        self.genderMenu = QtWidgets.QComboBox(self.centralwidget)
        self.genderMenu.addItem("Gender")
        self.genderMenu.addItems(['Male', 'Female', 'Other'])
        self.genderMenu.setGeometry(330, 170, 141, 16)

        #age input
        self.ageInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ageInput.setGeometry(QtCore.QRect(490, 170, 50, 16))
        self.ageInput.setObjectName("ageInput")

        def onButtonClick():
                creatingTable(self.usernameDatabase.text(),self.firstNameInput.text(), self.lastNameInput.text(), self.ageInput.text(), str(self.genderMenu.currentText()),0)
                
                

        #The button that pushes information to the list/file
        self.pushInformationButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushInformationButton.setGeometry(QtCore.QRect(252, 200, 75, 23))
        self.pushInformationButton.setObjectName("pushInformationButton")
        self.pushInformationButton.setText("Enter")
        self.pushInformationButton.clicked.connect(onButtonClick)

        self.modifyInfo = QtWidgets.QPushButton(self.centralwidget)
        self.modifyInfo.setGeometry(QtCore.QRect(252, 250, 75, 23))
        self.modifyInfo.setObjectName("modifyInfo")
        self.modifyInfo.setText("Change pre existing student info")
        self.modifyInfo.clicked.connect(self.showNextWindow)
        
        MainWindow.setCentralWidget(self.centralwidget)



class modifyStudents(object):
       def setupUi(self, MainWindow):
        databaseConnection = mysql.connector.connect(user='p2qc4wz6zc6hbbkb', password='myaslorqvek6c29y',
                                host='eyw6324oty5fsovx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                database='z4vwcj96hi45ocay')
        mycursor = databaseConnection.cursor()
        print()
        query = 'SELECT * FROM MrTombs'
        mycursor.execute(query)
        
        rows = mycursor.fetchall()        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 455)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        #Database Data view
        self.scroll = QtWidgets.QScrollArea()
        
        self.databaseView = QtWidgets.QTableWidget(self.centralwidget)
        self.databaseView.setGeometry(0,0,550,200)
        self.databaseView.setColumnCount(4)
        self.databaseView.setHorizontalHeaderLabels(["First Name", "Last Name", "Sex", "Age"])
        self.databaseView.setRowCount(len(rows))
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.buttonD = QtWidgets.QPushButton(self.centralwidget)
        self.buttonD.setGeometry(QtCore.QRect(200, 250, 170, 30))
        self.buttonD.setObjectName("modifyInfo")
        self.buttonD.setText("Change pre existing student info")
        
        tableindex = 0
        for r in rows:
                self.databaseView.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(r[0]))
                self.databaseView.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(r[1]))
                self.databaseView.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(r[2]))
                self.databaseView.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(r[3]))
                tableindex+=1
        
        MainWindow.setCentralWidget(self.centralwidget)

        