# Recompile Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.instrumentation as instrumentation

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

    def setupUi(self, Recompile):
        Recompile.setObjectName("Recompile")
        Recompile.setFixedSize(QtCore.QSize(741, 330))

        self.bRecompile = QtWidgets.QPushButton(Recompile)
        self.bRecompile.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bRecompile.setObjectName("bRecompile")
        self.bRecompile.setEnabled(False)\

        self.lLog = QtWidgets.QPlainTextEdit(Recompile)
        self.lLog.setGeometry(QtCore.QRect(10, 90, 721, 201))
        self.lLog.setReadOnly(True)
        self.lLog.setObjectName("lLog")

        self.bSelect = QtWidgets.QPushButton(Recompile)
        self.bSelect.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.bSelect.setObjectName("bSelect")

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
