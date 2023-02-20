# Patch APKS -> APK
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.patchMenu as patchMenu
import py_asset.pAPK as pAPK
import os
import tempfile
import time

class Ui_PatchAPKS(object):

    #Global Variable
    locationWindows = "C:\\"
    base = os.getcwd()

    #Ui 
    def timeLog(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime())

    def uiUpdate(self):
        QtGui.QGuiApplication.processEvents()

    def bTrue(self):
        self.bApks.setEnabled(True)
        self.bBack.setEnabled(True)
        self.bSelect.setEnabled(True)

    def bFalse(self):
        self.bApks.setEnabled(False)
        self.bBack.setEnabled(False)
        self.bSelect.setEnabled(False)

    def sAlert(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()
    
    #BrowseFile
    def browseFile(self):
        fileLocation = QtWidgets.QFileDialog.getOpenFileName(None,'Select APKS',self.locationWindows,"Android File (*apks)")
        self.lPath.setText(fileLocation[0])
        if len(fileLocation[0]) == 0:
            self.bApks.setEnabled(False)
        elif ".apks" in fileLocation[0]:
            self.bApks.setEnabled(True)

    #Threading
    def tThreading(self,tmpfile):
        while(True):
            QtCore.QCoreApplication.processEvents()
            with open(tmpfile) as files:
                value = files.readline()
                if value == "1":
                    location = os.getcwd().replace("\\", "/")
                    filename = self.lPath.text().split("/")[-1]
                    self.bTrue()
                    self.lLog.appendPlainText(self.timeLog() + " Merging Succesful")
                    self.lLog.appendPlainText(self.timeLog() + " APK Location " + location + "/" + filename + ".out" + "/unknown/base/dist\n")
                    self.sAlert("Merging Succesful APK Location " + location + "/" + filename + ".out" + "/unknown/base/dist\n")
                    os.chdir(self.base)
                    break

    #Patch APKS -> APK
    def patch(self):
        self.bFalse()
        self.lLog.appendPlainText(self.timeLog() + " Start Merge APKS to APK")
        self.uiUpdate()
        tmpfile = tempfile.gettempdir()
        tmpfile += "\\test123.tmp"
        with open(tmpfile,"w") as files:
            files.write("0")
        filename = self.lPath.text()
        pAPK.realRun(filename,tmpfile)
        self.tThreading(tmpfile)
            
    #Back Button
    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = patchMenu.Ui_PatchMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, PatchAPKS):
        PatchAPKS.setObjectName("PatchAPKS")
        PatchAPKS.setFixedSize(QtCore.QSize(742, 330))
        PatchAPKS.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))

        self.bSelect = QtWidgets.QPushButton(PatchAPKS)
        self.bSelect.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.bSelect.setObjectName("bSelect")
        self.bSelect.clicked.connect(self.browseFile)
        
        self.bBack = QtWidgets.QPushButton(PatchAPKS)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(PatchAPKS.close)
        
        self.lLog = QtWidgets.QPlainTextEdit(PatchAPKS)
        self.lLog.setGeometry(QtCore.QRect(10, 90, 721, 200))
        self.lLog.setReadOnly(True)
        self.lLog.setObjectName("lLog")
        
        self.lPath = QtWidgets.QLineEdit(PatchAPKS)
        self.lPath.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.lPath.setReadOnly(True)
        self.lPath.setObjectName("ePath")
        
        self.bApks = QtWidgets.QPushButton(PatchAPKS)
        self.bApks.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bApks.setObjectName("bApks")
        self.bApks.setEnabled(False)
        self.bApks.clicked.connect(self.patch)

        self.retranslateUi(PatchAPKS)
        QtCore.QMetaObject.connectSlotsByName(PatchAPKS)

    def retranslateUi(self, PatchAPKS):
        _translate = QtCore.QCoreApplication.translate
        PatchAPKS.setWindowTitle(_translate("PatchAPKS", "Patch APKS"))
        self.bSelect.setText(_translate("PatchAPKS", "Select APKS"))
        self.bBack.setText(_translate("PatchAPKS", "Back"))
        self.bApks.setText(_translate("PatchAPKS", "APKS to APK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatchAPKS = QtWidgets.QWidget()
    ui = Ui_PatchAPKS()
    ui.setupUi(PatchAPKS)
    PatchAPKS.show()
    sys.exit(app.exec_())
