from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from pushInformation import *

class Ui_MainWindow(object):
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


        
        MainWindow.setCentralWidget(self.centralwidget)



#runs and shows the application
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())