# Patch Toast Menu
import tempfile
import time

from PyQt5 import QtCore, QtGui, QtWidgets

import py_asset.basicUtils as basicUtils
import py_asset.patchMenu as patchMenu


class Ui_PatchToast(object):

    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = patchMenu.Ui_PatchMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    locationWindows = "C:\\"

    def timeLog(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime())

    def bTrue(self):
        self.bBack.setEnabled(True)
        self.bToast.setEnabled(True)
        self.bSelect.setEnabled(True)

    def bFalse(self):
        self.bBack.setEnabled(False)
        self.bToast.setEnabled(False)
        self.bSelect.setEnabled(False)

    def sAlert(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def browseFile(self):
        fileLocation = QtWidgets.QFileDialog.getOpenFileName(None,'Select Smali',self.locationWindows,"Android File (*smali)")
        self.lPath.setText(fileLocation[0])
        if len(fileLocation[0]) == 0:
            self.bToast.setEnabled(False)
        else:
            self.bToast.setEnabled(True)

    def tThreading(self,tmpfile):
        while(True):
            QtCore.QCoreApplication.processEvents()
            with open(tmpfile) as files:
                value = files.readline()
                if value == "2":
                    self.bTrue()
                    self.lLog.appendPlainText(self.timeLog() + " Smali Patch Succesful")
                    self.sAlert("Smali Patch Succesful")
                    break

    def smaliPatch(self):
        self.bFalse()
        filename = self.lPath.text()
        self.lLog.appendPlainText(self.timeLog() + " Start Patch Smali File")
        QtGui.QGuiApplication.processEvents()
        tmpfile = tempfile.gettempdir()
        tmpfile += "\\test123.tmp"
        with open(tmpfile,"w") as files:
            files.write("0")
        basicUtils.realpatchXML(filename,tmpfile)
        self.tThreading(tmpfile)

    def setupUi(self, PatchToast):
        PatchToast.setObjectName("PatchToast")
        PatchToast.setFixedSize(QtCore.QSize(742, 330))
        PatchToast.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
 
        self.bSelect = QtWidgets.QPushButton(PatchToast)
        self.bSelect.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.bSelect.setObjectName("bSelect")
        self.bSelect.clicked.connect(self.browseFile)
        
        self.bBack = QtWidgets.QPushButton(PatchToast)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(PatchToast.close)
        
        self.lLog = QtWidgets.QPlainTextEdit(PatchToast)
        self.lLog.setGeometry(QtCore.QRect(10, 90, 721, 200))
        self.lLog.setReadOnly(True)
        self.lLog.setObjectName("lLog")
        
        self.bToast = QtWidgets.QPushButton(PatchToast)
        self.bToast.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bToast.setEnabled(False)
        self.bToast.setObjectName("bToast")
        self.bToast.clicked.connect(self.smaliPatch)
        
        self.lPath = QtWidgets.QLineEdit(PatchToast)
        self.lPath.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.lPath.setReadOnly(True)
        self.lPath.setObjectName("lPath")

        self.retranslateUi(PatchToast)
        QtCore.QMetaObject.connectSlotsByName(PatchToast)

    def retranslateUi(self, PatchToast):
        _translate = QtCore.QCoreApplication.translate
        PatchToast.setWindowTitle(_translate("PatchToast", "Patch Toast"))
        self.bSelect.setText(_translate("PatchToast", "Select Smali"))
        self.bBack.setText(_translate("PatchToast", "Back"))
        self.bToast.setText(_translate("PatchToast", "Toast"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatchToast = QtWidgets.QWidget()
    ui = Ui_PatchToast()
    ui.setupUi(PatchToast)
    PatchToast.show()
    sys.exit(app.exec_())
