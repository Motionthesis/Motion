# Decompile Menu
from PyQt5 import QtCore, QtGui, QtWidgets
from py_asset.basicUtils import realDecompile
import py_asset.instrumentation as instrumentation
import tempfile
import subprocess
import os
import time

class Ui_Form(object):
    
    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = instrumentation.Ui_Instrumentation()
        self.ui.setupUi(self.window)
        self.window.show()

    locationWindows = 'C:\\'

    def timeLog(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime())
    
    def uiUpdate(self):
        QtCore.QCoreApplication.processEvents()

    def sAlert(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def bTrue(self):
        self.bSelect.setEnabled(True)
        self.bBack.setEnabled(True)
        self.bDecompile.setEnabled(True)

    def bFalse(self):
        self.bSelect.setEnabled(False)
        self.bBack.setEnabled(False)
        self.bDecompile.setEnabled(False)
    
    def browseFile(self):
        fileLocation = QtWidgets.QFileDialog.getOpenFileName(None,'Select APK\S',self.locationWindows,"Android File (*apk *apks)")
        self.lPath.setText(fileLocation[0])
        value = self.lPath.text()
        if len(value) > 1:
            self.bDecompile.setEnabled(True)
        else:
            self.bDecompile.setEnabled(False)

    def tThreading(self,fileLocation,tmpfile,base):
        tmpName = fileLocation.split("/")[-1]
        tmpbase = base+"\\decompile"
        while(True):
            QtCore.QCoreApplication.processEvents()
            with open(tmpfile) as files:
                value = files.readline()
                if value == "1":
                    if ".apks" in tmpName:
                        self.lLog.appendPlainText(self.timeLog() + ' Decompile Success')
                        self.uiUpdate()
                        msg = "Decompile Success, Location "+tmpbase+"\\"+tmpName+".out"
                        self.lLog.appendPlainText(self.timeLog() + " Decompile Location "+tmpbase+"\\"+tmpName+".out\n")
                        self.uiUpdate()
                        self.sAlert(msg)
                        self.bTrue()
                        break
                    else:
                        self.lLog.appendPlainText(self.timeLog() + ' Decompile Success')
                        self.uiUpdate()
                        tmp = tmpName.replace(".apk","")
                        msg = "Decompile Success, Location "+tmpbase+"\\"+tmp
                        self.lLog.appendPlainText(self.timeLog() + " Decompile Location "+tmpbase+"\\"+tmp+"\n")
                        self.uiUpdate()
                        self.sAlert(msg)
                        self.bTrue()
                        break

    def decompile(self):
        fileLocation = self.lPath.text()
        self.lLog.appendPlainText(self.timeLog() + ' Start Decompile')
        self.uiUpdate()
        tmpfile = tempfile.gettempdir()
        tmpfile += "\\test123.tmp"
        with open(tmpfile,"w") as files:
            files.write("0")
        base = os.getcwd()
        print(base)
        self.bFalse()
        realDecompile(fileLocation,base,tmpfile)
        self.tThreading(fileLocation,tmpfile,base)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(741, 330)

        self.lLog = QtWidgets.QPlainTextEdit(Form)
        self.lLog.setGeometry(QtCore.QRect(10, 90, 721, 200))
        self.lLog.setReadOnly(True)
        self.lLog.setObjectName("lLog")
        
        self.bSelect = QtWidgets.QPushButton(Form)
        self.bSelect.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.bSelect.setObjectName("bSelect")
        self.bSelect.clicked.connect(self.browseFile)

        self.lPath =  QtWidgets.QLineEdit(Form)
        self.lPath.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.lPath.setReadOnly(True)
        self.lPath.setObjectName("lPath")
     
        self.bDecompile = QtWidgets.QPushButton(Form)
        self.bDecompile.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bDecompile.setObjectName("bDecompile")
        self.bDecompile.setEnabled(False)
        self.bDecompile.clicked.connect(self.decompile)

        self.bBack = QtWidgets.QPushButton(Form)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Decompile"))
        self.bSelect.setText(_translate("Form", "Select APK\S"))
        self.bBack.setText(_translate("Form", "Back"))
        self.bDecompile.setText(_translate("Form", "Decompile"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())