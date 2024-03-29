# Main Menu
import os
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets

import py_asset.basicUtils as basicUtils
from py_asset.installAPK import Ui_InstallAPK
from py_asset.instrumentation import Ui_Instrumentation
from py_asset.utilMenu import Ui_Utility


class Ui_MainWindow(object):

    """
        Run Firstime
        Apps bakal coba testing nge create folder screenshot ama decompile kalau udah ada bakal lanjut kalau belum bakal di create
    """
    def makeDir(self):
        try:
            os.mkdir("screenshot")
        except:
            pass
        try:
            os.mkdir("decompile")
        except:
            pass
            
    """
        Checking Installed Tools
        Apps bakal ngecheck installed tools jika tidak ada maka akan di alert
            -   Apktool
            -   Jarsigner
            -   Keytool
            -   Apksigner
            -   ADB
            -   Zipalign
    """        
    def checking(self):
        NotFound = []
        s = subprocess.Popen("where apktool",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        (out,err) = s.communicate()
        if len(out) == 0:
            NotFound.append("apktool Not Found\n")
        s = subprocess.Popen("where jarsigner",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        (out,err) = s.communicate()
        if len(out) == 0:
            NotFound.append("jarsigner Not Found\n")
        s = subprocess.Popen("where keytool",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        (out,err) = s.communicate()
        if len(out) == 0:
            NotFound.append("keytool Not Found\n")
        s = subprocess.Popen("where apksigner",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        (out,err) = s.communicate()
        if len(out) == 0:
            NotFound.append("apksigner Not Found\n")
        s = subprocess.Popen("where adb",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        (out,err) = s.communicate()
        if len(out) == 0:
            NotFound.append("adb Not Found\n")
        s = subprocess.Popen("where zipalign",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        (out,err) = s.communicate()
        if len(out) == 0:
            NotFound.append("zipalign Not Found\n")
        if len(NotFound) == 0:
            self.Alert()
        elif "Not Found" in NotFound[0]:
            self.noAlert(NotFound)
              
    """
        Alert UI Spawner
    """
    def fAlert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("No Device Connected")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()
    
    def noAlert(self,list):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        Text = ""
        for i in list:
            Text += i.replace("'","").replace("[","").replace("]","").replace(",","")
        msg.setText(Text)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()
    
    def Alert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("All Tools Installed")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec()
    
    """
        Device Checker
        Menggunakan ADB Untuk melakukan pengecekan device jika device tersedia maka device akan tertulis connected
    """
    def adbDevice(self):
        value = basicUtils.deviceChecking()
        if value == 1:
            self.lCheck.setText("Not Connected")
            return value
        else:
            self.lCheck.setText("Connected")
            return value
    
    """
        Menu Spawner
        Own Menu -> Menu Awal (Main Menu)
        Install Menu -> Pindah Ke Menu Install
        uMenu -> Pindah Ke Menu Util
        iMenu -> Pindah Ke Menu Instrumentation
    """
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
    

    """
        PYQT5 Object Build
        Front End Code
    """
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

        self.bCheckTools = QtWidgets.QPushButton(MainWindow)
        self.bCheckTools.setGeometry(QtCore.QRect(410, 10, 151, 31))
        self.bCheckTools.setObjectName("bCheckTools")
        self.bCheckTools.clicked.connect(self.checking)

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
        self.bCheckTools.setText(_translate("MainWindow", "Check Required Tools"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
