# Recompile Menu
import tempfile
import time

from PyQt5 import QtCore, QtGui, QtWidgets

import py_asset.instrumentation as instrumentation
from py_asset.basicUtils import realRecompile


class Ui_Recompile(object):
    
    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = instrumentation.Ui_Instrumentation()
        self.ui.setupUi(self.window)
        self.window.show()

    def bTrue(self):
        self.bRecompile.setEnabled(True)
        self.bSelect.setEnabled(True)
        self.bBack.setEnabled(True)

    def bFalse(self):
        self.bRecompile.setEnabled(False)
        self.bSelect.setEnabled(False)
        self.bBack.setEnabled(False)

    locationWindows = 'C:\\'

    def sAlert(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def timeLog(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime())

    def uiUpdate(self):
        QtGui.QGuiApplication.processEvents()

    def getFolder(self):
        folderLocation = QtWidgets.QFileDialog.getExistingDirectory(None,"Select Folder",self.locationWindows)
        self.lPath.setText(folderLocation)
        value = self.lPath.text()
        if len(value) > 3:
            self.bRecompile.setEnabled(True)
        else:
            self.bRecompile.setEnabled(False)

    def tThreading(self,fileLocation,tmpFile):
        while(True):
            QtCore.QCoreApplication.processEvents()
            with open(tmpFile) as files:
                value = files.readline()
                if value == '1':
                    self.lLog.appendPlainText(self.timeLog() + " Recompile Success")
                    self.uiUpdate()
                    msg = "Recompile Success, Location " + fileLocation + "/dist"
                    self.lLog.appendPlainText(self.timeLog() + " Recompile Location " + fileLocation + "/dist\n")
                    self.uiUpdate()
                    self.sAlert(msg)
                    self.bTrue()
                    break
    
    def recom(self):
        fileLocation = self.lPath.text()
        self.lLog.appendPlainText(self.timeLog() + " Start Recompile")
        self.uiUpdate()
        tmpfile = tempfile.gettempdir()
        tmpfile += "\\test123.tmp"
        with open(tmpfile,"w") as files:
            files.write("0")
        self.bFalse()
        realRecompile(fileLocation,tmpfile)
        self.tThreading(fileLocation,tmpfile)

    def setupUi(self, Recompile):
        Recompile.setObjectName("Recompile")
        Recompile.setFixedSize(QtCore.QSize(741, 330))
        Recompile.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))

        self.bRecompile = QtWidgets.QPushButton(Recompile)
        self.bRecompile.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bRecompile.setObjectName("bRecompile")
        self.bRecompile.setEnabled(False)
        self.bRecompile.clicked.connect(self.recom)

        self.lLog = QtWidgets.QPlainTextEdit(Recompile)
        self.lLog.setGeometry(QtCore.QRect(10, 90, 721, 201))
        self.lLog.setReadOnly(True)
        self.lLog.setObjectName("lLog")

        self.bSelect = QtWidgets.QPushButton(Recompile)
        self.bSelect.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.bSelect.setObjectName("bSelect")
        self.bSelect.clicked.connect(self.getFolder)

        self.lPath = QtWidgets.QLineEdit(Recompile)
        self.lPath.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.lPath.setReadOnly(True)
        self.lPath.setObjectName("lPath")

        self.bBack = QtWidgets.QPushButton(Recompile)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(Recompile.close)   

        self.retranslateUi(Recompile)
        QtCore.QMetaObject.connectSlotsByName(Recompile)

    def retranslateUi(self, Recompile):
        _translate = QtCore.QCoreApplication.translate
        Recompile.setWindowTitle(_translate("Recompile", "Recompile APK"))
        self.bBack.setText(_translate("Recompile", "Back"))
        self.bRecompile.setText(_translate("Recompile", "Recompile"))
        self.bSelect.setText(_translate("Recompile", "Select Folder"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Recompile()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
