#Uninstall Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.utilMenu as utilmenu
class Ui_UninstallAPK(object):

    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = utilmenu.Ui_Utility()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, UninstallAPK):
        UninstallAPK.setObjectName("UninstallAPK")
        UninstallAPK.setFixedSize(QtCore.QSize(741, 330))

        self.lApps = QtWidgets.QListWidget(UninstallAPK)
        self.lApps.setGeometry(QtCore.QRect(10, 90, 721, 200))
        self.lApps.setObjectName("lApps")

        self.bUninstall = QtWidgets.QPushButton(UninstallAPK)
        self.bUninstall.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bUninstall.setAutoDefault(False)
        self.bUninstall.setDefault(False)
        self.bUninstall.setEnabled(False)
        self.bUninstall.setObjectName("bUninstall")

        self.bApplist = QtWidgets.QPushButton(UninstallAPK)
        self.bApplist.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.bApplist.setObjectName("bApplist")

        self.eFilename = QtWidgets.QLineEdit(UninstallAPK)
        self.eFilename.setGeometry(QtCore.QRect(10, 10, 721, 31))
        self.eFilename.setReadOnly(True)
        self.eFilename.setObjectName("eFilename")

        self.bBack = QtWidgets.QPushButton(UninstallAPK)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(UninstallAPK.close)

        self.retranslateUi(UninstallAPK)
        QtCore.QMetaObject.connectSlotsByName(UninstallAPK)

    def retranslateUi(self, UninstallAPK):
        _translate = QtCore.QCoreApplication.translate
        UninstallAPK.setWindowTitle(_translate("UninstallAPK", "Uninstall APK"))
        self.bUninstall.setText(_translate("UninstallAPK", "Uninstall"))
        self.bBack.setText(_translate("UninstallAPK", "Back"))
        self.bApplist.setText(_translate("UninstallAPK", "List App"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UninstallAPK = QtWidgets.QWidget()
    ui = Ui_UninstallAPK()
    ui.setupUi(UninstallAPK)
    UninstallAPK.show()
    sys.exit(app.exec_())
