# Sign Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.instrumentation as instrumentation

class Ui_SignAPK(object):

    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = instrumentation.Ui_Instrumentation()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def bTrue(self):
        self.bSelect.setEnabled(True)
        self.bSign.setEnabled(True)
        self.cAndroid.setEnabled(True)
        self.bBack.setEnabled(True)
    
    def bFalse(self):
        self.bSelect.setEnabled(False)
        self.bSign.setEnabled(False)
        self.cAndroid.setEnabled(False)
        self.bBack.setEnabled(False)
   
    def setupUi(self, SignAPK):
        SignAPK.setObjectName("SignAPK")
        SignAPK.setFixedSize(QtCore.QSize(741, 330))

        self.lPath = QtWidgets.QLineEdit(SignAPK)
        self.lPath.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.lPath.setReadOnly(True)
        self.lPath.setObjectName("lPath")

        self.bSelect = QtWidgets.QPushButton(SignAPK)
        self.bSelect.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.bSelect.setObjectName("bSelect")

        self.bSign = QtWidgets.QPushButton(SignAPK)
        self.bSign.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bSign.setObjectName("bSign")
        self.bSign.setEnabled(False)

        self.lLog = QtWidgets.QPlainTextEdit(SignAPK)
        self.lLog.setGeometry(QtCore.QRect(10, 90, 721, 200))
        self.lLog.setReadOnly(True)
        self.lLog.setObjectName("lLog")
        
        self.cAndroid = QtWidgets.QCheckBox(SignAPK)
        self.cAndroid.setGeometry(QtCore.QRect(520, 50, 91, 31))
        self.cAndroid.setObjectName("cAndroid")

        self.bBack = QtWidgets.QPushButton(SignAPK)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(SignAPK.close)

        self.retranslateUi(SignAPK)
        QtCore.QMetaObject.connectSlotsByName(SignAPK)

    def retranslateUi(self, SignAPK):
        _translate = QtCore.QCoreApplication.translate
        SignAPK.setWindowTitle(_translate("SignAPK", "Sign APK"))
        self.bSelect.setText(_translate("SignAPK", "Select APK"))
        self.bBack.setText(_translate("SignAPK", "Back"))
        self.bSign.setText(_translate("SignAPK", "Sign"))
        self.cAndroid.setText(_translate("SignAPK", "APKSigner"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SignAPK()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
