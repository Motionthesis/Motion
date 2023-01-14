# Install APK Menu
from platform import platform
from PyQt5 import QtCore, QtGui, QtWidgets
import platform
import time
import tempfile
import os
import py_asset.basicUtils as basicUtils
import py_asset.iAPK as insAPK

class Ui_InstallAPK(object):

    def bButton(self):
        import main
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    locationWindows = 'C:\\'
    #Ui
    def timeLog(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime())

    def uiUpdate(self):
        QtCore.QCoreApplication.processEvents()

    def sAlert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
        msg.setWindowTitle("Information")
        msg.setText("Installation Success")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def fAlert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
        msg.setWindowTitle("Information")
        msg.setText("Fail to Install")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()
    
    def dAlert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
        msg.setWindowTitle("Information")
        msg.setText("No Device Connected")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()

    def lAlert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
        msg.setWindowTitle("Information")
        msg.setText("Please Input a File")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()
    
    def bFalse(self):
        self.installButton.setEnabled(False)
        self.selectFile.setEnabled(False)
        self.bBack.setEnabled(False)

    def bTrue(self):
        self.installButton.setEnabled(True)
        self.selectFile.setEnabled(True)
        self.bBack.setEnabled(True)
    ###
    
    def adbDevices(self):
        return basicUtils.deviceChecking()

    def tThreading(self,tmpfile):
        while(True):
            QtCore.QCoreApplication.processEvents()
            with open(tmpfile) as files:
                value = files.readline()
                if value == "1":
                    self.logViewer.appendPlainText(self.timeLog() + ' Installation Success.\n')
                    self.sAlert()
                    self.bTrue()
                    break
                elif value == "2":
                    self.logViewer.appendPlainText(self.timeLog() + ' Failed to Install.\n')
                    self.fAlert()
                    self.bTrue()
                    break

    def iAPKF(self):
        fileLocation = self.filePath.text()
        if self.adbDevices() == 1:
            self.dAlert()
        elif len(fileLocation) == 0:
            self.lAlert()
        else:
            if 'Windows' in platform.system():
                fileName = fileLocation.replace('/','\\')
                tmpfileName = fileName.split("\\")[-1]
                tmpfile = tempfile.gettempdir()
                tmpfile += "\\test123.tmp"
                with open(tmpfile,"w") as files:
                    files.write("0")
                self.bFalse()
                if fileName.endswith('.apk'):
                    self.logViewer.appendPlainText(self.timeLog() + ' APK Detected.')
                    self.logViewer.appendPlainText(self.timeLog() + ' Begin Installation (Check Your Device for Confirmation).')
                    self.uiUpdate()
                    insAPK.realInstall(fileName,1,tmpfileName,"Windows",tmpfile)
                    self.tThreading(tmpfile)                            
                else:
                    self.logViewer.appendPlainText(self.timeLog() + ' APKS Detected.')
                    self.logViewer.appendPlainText(self.timeLog() + ' Begin Installation (Check Your Device for Confirmation).')
                    self.uiUpdate()
                    insAPK.realInstall(fileName,2,tmpfileName,"Windows",tmpfile)
                    self.tThreading(tmpfile)
        
    def browseFile(self):
        fileLocation = QtWidgets.QFileDialog.getOpenFileName(None,'Select APK\S',self.locationWindows,"Android File (*apks *xapk *apk)")
        self.filePath.setText(fileLocation[0])
    
    def setupUi(self, InstallAPK):
        InstallAPK.setObjectName("InstallAPK")
        InstallAPK.setFixedSize(QtCore.QSize(741, 330))
        InstallAPK.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))

        #Install APK Button
        self.installButton = QtWidgets.QPushButton(InstallAPK)
        self.installButton.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.installButton.setObjectName("installButton")
        self.installButton.clicked.connect(self.iAPKF)

        #File Path
        self.filePath = QtWidgets.QLineEdit(InstallAPK)
        self.filePath.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.filePath.setReadOnly(True)
        self.filePath.setObjectName("filePath")
        
        #Select File
        self.selectFile = QtWidgets.QPushButton(InstallAPK)
        self.selectFile.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.selectFile.setObjectName("selectFile")
        self.selectFile.clicked.connect(self.browseFile)

        self.logViewer = QtWidgets.QPlainTextEdit(InstallAPK)
        self.logViewer.setGeometry(QtCore.QRect(11, 90, 721, 200))
        self.logViewer.setReadOnly(True)
        self.logViewer.setObjectName("logViewer")

        self.bBack = QtWidgets.QPushButton(InstallAPK)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(InstallAPK.close)

        self.retranslateUi(InstallAPK)
        QtCore.QMetaObject.connectSlotsByName(InstallAPK)

    def retranslateUi(self, InstallAPK):
        _translate = QtCore.QCoreApplication.translate
        InstallAPK.setWindowTitle(_translate("InstallAPK", "Install APK/S"))
        self.installButton.setText(_translate("InstallAPK", "Install APK/S"))
        self.selectFile.setText(_translate("InstallAPK", "Select File"))
        self.bBack.setText(_translate("InstallAPK", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InstallAPK()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())