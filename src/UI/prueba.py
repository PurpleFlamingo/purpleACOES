# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 641)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.bExit = QtWidgets.QPushButton(self.centralWidget)
        self.bExit.setGeometry(QtCore.QRect(800, 540, 80, 25))
        self.bExit.setObjectName("bExit")
        self.bLogin = QtWidgets.QPushButton(self.centralWidget)
        self.bLogin.setGeometry(QtCore.QRect(710, 540, 80, 25))
        self.bLogin.setObjectName("bLogin")
        self.lWelcome = QtWidgets.QLabel(self.centralWidget)
        self.lWelcome.setGeometry(QtCore.QRect(10, 0, 891, 121))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lWelcome.setFont(font)
        self.lWelcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lWelcome.setObjectName("lWelcome")
        self.lUser = QtWidgets.QLabel(self.centralWidget)
        self.lUser.setGeometry(QtCore.QRect(50, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lUser.setFont(font)
        self.lUser.setObjectName("lUser")
        self.lPassword = QtWidgets.QLabel(self.centralWidget)
        self.lPassword.setGeometry(QtCore.QRect(50, 310, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lPassword.setFont(font)
        self.lPassword.setObjectName("lPassword")
        self.eUser = QtWidgets.QLineEdit(self.centralWidget)
        self.eUser.setGeometry(QtCore.QRect(170, 180, 671, 25))
        self.eUser.setObjectName("eUser")
        self.ePassword = QtWidgets.QLineEdit(self.centralWidget)
        self.ePassword.setGeometry(QtCore.QRect(180, 320, 671, 25))
        self.ePassword.setObjectName("ePassword")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        MainWindow.insertToolBarBreak(self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bExit.setText(_translate("MainWindow", "Exit"))
        self.bLogin.setText(_translate("MainWindow", "Log in"))
        self.lWelcome.setText(_translate("MainWindow", "Bienvenido a ACOES"))
        self.lUser.setText(_translate("MainWindow", "Usuario:"))
        self.lPassword.setText(_translate("MainWindow", "Contrasena:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

