# Patch APKS -> APK
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.patchMenu as patchMenu

class Ui_PatchAPKS(object):

    def bTrue(self):
        self.bApks.setEnabled(True)
        self.bBack.setEnabled(True)
        self.bSelect.setEnabled(True)

    def bFalse(self):
        self.bApks.setEnabled(False)
        self.bBack.setEnabled(False)
        self.bSelect.setEnabled(False)

    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = patchMenu.Ui_PatchMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, PatchAPKS):
        PatchAPKS.setObjectName("PatchAPKS")
        PatchAPKS.setFixedSize(QtCore.QSize(742, 330))

        self.bSelect = QtWidgets.QPushButton(PatchAPKS)
        self.bSelect.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.bSelect.setObjectName("bSelect")
        
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
