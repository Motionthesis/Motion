# Patch Menu (Toast,Multiple,APKS)
from PyQt5 import QtCore, QtGui, QtWidgets

import py_asset.instrumentation as instrumentation
from py_asset.patchAPK import Ui_PatchAPK
from py_asset.patchAPKS import Ui_PatchAPKS
from py_asset.patchToast import Ui_PatchToast


class Ui_PatchMenu(object):

    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = instrumentation.Ui_Instrumentation()
        self.ui.setupUi(self.window)
        self.window.show()

    def bToastAlert(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PatchToast()
        self.ui.setupUi(self.window)
        self.window.show()

    def bAPKS(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PatchAPKS()
        self.ui.setupUi(self.window)
        self.window.show()

    def bAPK(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PatchAPK()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, PatchMenu):
        PatchMenu.setObjectName("PatchMenu")
        PatchMenu.setFixedSize(QtCore.QSize(531, 100))
        PatchMenu.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))

        self.bBack = QtWidgets.QPushButton(PatchMenu)
        self.bBack.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(PatchMenu.close)
        
        self.bMultiple = QtWidgets.QPushButton(PatchMenu)
        self.bMultiple.setGeometry(QtCore.QRect(30, 10, 151, 51))
        self.bMultiple.setObjectName("bMultiple")
        self.bMultiple.clicked.connect(self.bAPK)
        self.bMultiple.clicked.connect(PatchMenu.close)
        
        self.bApks = QtWidgets.QPushButton(PatchMenu)
        self.bApks.setGeometry(QtCore.QRect(190, 10, 151, 51))
        self.bApks.setObjectName("bApks")
        self.bApks.clicked.connect(self.bAPKS)
        self.bApks.clicked.connect(PatchMenu.close)
        
        self.bToast = QtWidgets.QPushButton(PatchMenu)
        self.bToast.setGeometry(QtCore.QRect(350, 10, 151, 51))
        self.bToast.setObjectName("bToast")
        self.bToast.clicked.connect(self.bToastAlert)
        self.bToast.clicked.connect(PatchMenu.close)

        self.retranslateUi(PatchMenu)
        QtCore.QMetaObject.connectSlotsByName(PatchMenu)

    def retranslateUi(self, PatchMenu):
        _translate = QtCore.QCoreApplication.translate
        PatchMenu.setWindowTitle(_translate("PatchMenu", "Patch Menu"))
        self.bBack.setText(_translate("PatchMenu", "Back"))
        self.bMultiple.setText(_translate("PatchMenu", "Patch Multiple APK\nto APK"))
        self.bApks.setText(_translate("PatchMenu", "Patch APKS"))
        self.bToast.setText(_translate("PatchMenu", "Patch Toast"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PatchMenu = QtWidgets.QWidget()
    ui = Ui_PatchMenu()
    ui.setupUi(PatchMenu)
    PatchMenu.show()
    sys.exit(app.exec_())
