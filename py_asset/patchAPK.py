# Multiple APK -> APK Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.patchMenu as patchMenu
import py_asset.pAPKSolo as pAPK
import tempfile
import os
import time

class Ui_PatchAPK(object):

    base = os.getcwd()

    def bTrue(self):
        self.bMultiple.setEnabled(True)
        self.bSelect.setEnabled(True)
        self.bBack.setEnabled(True)

    def bFalse(self):
        self.bMultiple.setEnabled(False)
        self.bSelect.setEnabled(False)
        self.bBack.setEnabled(False)

    def uiUpdate(self):
        QtGui.QGuiApplication.processEvents()

    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = patchMenu.Ui_PatchMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    def sAlert(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def timeLog(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime())

    locationWindows = 'C:\\'

    def getFolder(self):
        folderLocation = QtWidgets.QFileDialog.getExistingDirectory(None,"Select A Folder",self.locationWindows)
        self.lPath.setText(folderLocation)
        value = self.lPath.text()
        if len(value) > 3:
            self.bMultiple.setEnabled(True)
        else:
            self.bMultiple.setEnabled(False)

    def tThreading(self,tmpfile):
        while(True):
            QtCore.QCoreApplication.processEvents()
            with open(tmpfile) as files:
                value = files.readline()
                if value == "1":
                    location = os.getcwd().replace("\\","/")
                    self.bTrue()
                    self.lLog.appendPlainText(self.timeLog() + " Merging Succesful")
                    self.lLog.appendPlainText(self.timeLog() + " APK Location " + location + "/base/dist\n")
                    self.sAlert("Merging Succesful APK Location " + location + "/base/dist\n")
                    os.chdir(self.base)
                    break

    #Multiple APK -> APK
    def patch(self):
        self.bFalse()
        self.lLog.appendPlainText(self.timeLog() + " Start Merge Multiple APK to APK")
        self.uiUpdate()
        tmpfile = tempfile.gettempdir()
        tmpfile += "\\test123.tmp"
        with open(tmpfile,"w") as files:
            files.write("0")
        filename = self.lPath.text()
        pAPK.realRun(filename,tmpfile)
        self.tThreading(tmpfile)
    
    def setupUi(self, PatchAPK):
        PatchAPK.setObjectName("PatchAPK")
        PatchAPK.setFixedSize(QtCore.QSize(742, 330))
        PatchAPK.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))

        self.lLog = QtWidgets.QPlainTextEdit(PatchAPK)
        self.lLog.setGeometry(QtCore.QRect(10, 90, 721, 200))
        self.lLog.setReadOnly(True)
        self.lLog.setObjectName("lLog")

        self.lPath = QtWidgets.QLineEdit(PatchAPK)
        self.lPath.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.lPath.setReadOnly(True)
        self.lPath.setObjectName("lPath")

        self.bSelect = QtWidgets.QPushButton(PatchAPK)
        self.bSelect.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.bSelect.setObjectName("bSelect")
        self.bSelect.clicked.connect(self.getFolder)

        self.bBack = QtWidgets.QPushButton(PatchAPK)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(PatchAPK.close)

        self.bMultiple = QtWidgets.QPushButton(PatchAPK)
        self.bMultiple.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bMultiple.setObjectName("bMultiple")
        self.bMultiple.setEnabled(False)
        self.bMultiple.clicked.connect(self.patch)

        self.retranslateUi(PatchAPK)
        QtCore.QMetaObject.connectSlotsByName(PatchAPK)

    def retranslateUi(self, PatchAPK):
        _translate = QtCore.QCoreApplication.translate
        PatchAPK.setWindowTitle(_translate("PatchAPK", "Patch Multiple APK"))
        self.bSelect.setText(_translate("PatchAPK", "Select Folder"))
        self.bBack.setText(_translate("PatchAPK", "Back"))
        self.bMultiple.setText(_translate("PatchAPK", "Multiple APK to APK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatchAPK = QtWidgets.QWidget()
    ui = Ui_PatchAPK()
    ui.setupUi(PatchAPK)
    PatchAPK.show()
    sys.exit(app.exec_())