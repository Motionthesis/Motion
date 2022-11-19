from PyQt5 import QtCore, QtWidgets
from py_asset.installAPK import Ui_InstallAPK
from py_asset.utilMenu import Ui_Utility
from py_asset.instrumentation import Ui_Instrumentation
import py_asset.basicUtils as basicUtils
import os

class Ui_MainWindow(object):

    #Run Firstime
    def makeDir(self):
        try:
            os.mkdir("screenshot")
            print("Directory Screenshot Created")
        except:
            print("Directory Screenshot Exist")
        try:
            os.mkdir("log")
            print("Directory Log Created")
        except:
            print("Directory Log Exist")
            pass
        try:
            os.mkdir("decompile")
            print("Directory Decompile Created")
        except:
            print("Directory Decompile Exist")

    #Ui
    def fAlert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("No Device Connected")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()
    ###

    def adbDevice(self):
        value = basicUtils.deviceChecking()
        if value == 1:
            self.lCheck.setText("Not Connected")
            return value
        else:
            self.lCheck.setText("Connected")
            return value
    
    #Call Menu
    def ownMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def installMenu(self):
        if self.adbDevice() == 1:
            self.fAlert()
            self.ownMenu()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_InstallAPK()
            self.ui.setupUi(self.window)
            self.window.show()

    def uMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Utility()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def iMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Instrumentation()
        self.ui.setupUi(self.window)
        self.window.show()
    ###

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QtCore.QSize(571, 140))

        self.makeDir()

        #Check Devices
        self.bCheck = QtWidgets.QPushButton(MainWindow)
        self.bCheck.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.bCheck.setObjectName("bCheck")
        self.bCheck.clicked.connect(self.adbDevice)

        self.lCheck = QtWidgets.QLabel(MainWindow)
        self.lCheck.setGeometry(QtCore.QRect(140, 10, 121, 31))
        self.lCheck.setObjectName("lCheck")

        #Install APK
        self.bInstall = QtWidgets.QPushButton(MainWindow)
        self.bInstall.setGeometry(QtCore.QRect(10, 60, 171, 71))
        self.bInstall.setObjectName("bInstall")
        self.bInstall.clicked.connect(self.installMenu)
        self.bInstall.clicked.connect(MainWindow.close)

        self.bDynamic = QtWidgets.QPushButton(MainWindow)
        self.bDynamic.setGeometry(QtCore.QRect(200, 60, 171, 71))
        self.bDynamic.setObjectName("bDynamic")
        self.bDynamic.clicked.connect(self.iMenu)
        self.bDynamic.clicked.connect(MainWindow.close)

        self.bUtil = QtWidgets.QPushButton(MainWindow)
        self.bUtil.setGeometry(QtCore.QRect(390, 60, 171, 71))
        self.bUtil.setObjectName("bUtil")
        self.bUtil.clicked.connect(self.uMenu)
        self.bUtil.clicked.connect(MainWindow.close)

        # self.bDownload = QtWidgets.QPushButton(MainWindow)
        # self.bDownload.setGeometry(QtCore.QRect(440, 10, 121, 31))
        # self.bDownload.setObjectName("bDownload")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Motion"))
        self.bCheck.setText(_translate("MainWindow", "Device Checking"))
        self.lCheck.setText(_translate("MainWindow", ""))
        self.bInstall.setText(_translate("MainWindow", "Install APK"))
        self.bDynamic.setText(_translate("MainWindow", "Instrumentation and\nTampering"))
        self.bUtil.setText(_translate("MainWindow", "Utility"))
        # self.bDownload.setText(_translate("MainWindow", "Download Assets"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
