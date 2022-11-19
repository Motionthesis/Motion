# Decompile Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.instrumentation as instrumentation

class Ui_Form(object):
    
    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = instrumentation.Ui_Instrumentation()
        self.ui.setupUi(self.window)
        self.window.show()

    def bTrue(self):
        self.bSelect.setEnabled(True)
        self.bBack.setEnabled(True)
        self.bDecompile.setEnabled(True)

    def bFalse(self):
        self.bSelect.setEnabled(False)
        self.bBack.setEnabled(False)
        self.bDecompile.setEnabled(False)

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

        self.lPath =  QtWidgets.QLineEdit(Form)
        self.lPath.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.lPath.setReadOnly(True)
        self.lPath.setObjectName("lPath")
     
        self.bDecompile = QtWidgets.QPushButton(Form)
        self.bDecompile.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bDecompile.setObjectName("bDecompile")
        self.bDecompile.setEnabled(False)

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