# Multiple APK -> APK Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.patchMenu as patchMenu

class Ui_PatchAPK(object):

    def bTrue(self):
        self.bMultiple.setEnabled(True)
        self.bSelect.setEnabled(True)
        self.bBack.setEnabled(True)

    def bFalse(self):
        self.bMultiple.setEnabled(False)
        self.bSelect.setEnabled(False)
        self.bBack.setEnabled(False)

    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = patchMenu.Ui_PatchMenu()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, PatchAPK):
        PatchAPK.setObjectName("PatchAPK")
        PatchAPK.setFixedSize(QtCore.QSize(742, 330))

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

        self.bBack = QtWidgets.QPushButton(PatchAPK)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(PatchAPK.close)

        self.bMultiple = QtWidgets.QPushButton(PatchAPK)
        self.bMultiple.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bMultiple.setObjectName("bMultiple")
        self.bMultiple.setEnabled(False)

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