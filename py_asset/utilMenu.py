#Util Menu
from PyQt5 import QtCore, QtGui, QtWidgets
from py_asset.uninstallMenu import Ui_UninstallAPK

class Ui_Utility(object):

    def bButton(self):
        import main
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def uninstallMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UninstallAPK()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Utility):
        Utility.setObjectName("Utility")
        Utility.setFixedSize(QtCore.QSize(571, 100))

        self.bUninstall = QtWidgets.QPushButton(Utility)
        self.bUninstall.setGeometry(QtCore.QRect(390, 10, 151, 51))
        self.bUninstall.setObjectName("bUninstall")
        self.bUninstall.clicked.connect(self.uninstallMenu)
        self.bUninstall.clicked.connect(Utility.close)

        self.bScreenshoot = QtWidgets.QPushButton(Utility)
        self.bScreenshoot.setGeometry(QtCore.QRect(30, 10, 151, 51))
        self.bScreenshoot.setObjectName("bScreenshoot")

        self.bShell = QtWidgets.QPushButton(Utility)
        self.bShell.setGeometry(QtCore.QRect(210, 10, 151, 51))
        self.bShell.setObjectName("bShell")

        self.bBack = QtWidgets.QPushButton(Utility)
        self.bBack.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(Utility.close)

        self.retranslateUi(Utility)
        QtCore.QMetaObject.connectSlotsByName(Utility)

    def retranslateUi(self, Utility):
        _translate = QtCore.QCoreApplication.translate
        Utility.setWindowTitle(_translate("Utility", "Utility"))
        self.bUninstall.setText(_translate("Utility", "Uninstall"))
        self.bScreenshoot.setText(_translate("Utility", "Screenshot"))
        self.bShell.setText(_translate("Utility", "Shell"))
        self.bBack.setText(_translate("Utility", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Utility = QtWidgets.QWidget()
    ui = Ui_Utility()
    ui.setupUi(Utility)
    Utility.show()
    sys.exit(app.exec_())
