# Instrumentation Menu
from PyQt5 import QtCore, QtWidgets

from py_asset.decompileMenu import Ui_Form
from py_asset.mDynamic import Ui_DynamicInstrumentation
from py_asset.patchMenu import Ui_PatchMenu
from py_asset.recompileMenu import Ui_Recompile
from py_asset.signMenu import Ui_SignAPK


class Ui_Instrumentation(object):

    def bButton(self):
        import main
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def dMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def rMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Recompile()
        self.ui.setupUi(self.window)
        self.window.show()

    def sMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SignAPK()
        self.ui.setupUi(self.window)
        self.window.show()

    def pMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PatchMenu()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def dynamicMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DynamicInstrumentation()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Instrumentation):
        Instrumentation.setObjectName("Instrumentation")
        Instrumentation.setFixedSize(QtCore.QSize(571, 170))

        self.bDynamic = QtWidgets.QPushButton(Instrumentation)
        self.bDynamic.setGeometry(QtCore.QRect(30, 10, 151, 51))
        self.bDynamic.setObjectName("bDynamic")
        self.bDynamic.clicked.connect(self.dynamicMenu)
        self.bDynamic.clicked.connect(Instrumentation.close)
        
        self.bPatch = QtWidgets.QPushButton(Instrumentation)
        self.bPatch.setGeometry(QtCore.QRect(210, 10, 151, 51))
        self.bPatch.setObjectName("bPatch")
        self.bPatch.clicked.connect(self.pMenu)
        self.bPatch.clicked.connect(Instrumentation.close)

        self.bSign = QtWidgets.QPushButton(Instrumentation)
        self.bSign.setGeometry(QtCore.QRect(390, 10, 151, 51))
        self.bSign.setObjectName("bSign")
        self.bSign.clicked.connect(self.sMenu)
        self.bSign.clicked.connect(Instrumentation.close)
        
        self.bDecompile = QtWidgets.QPushButton(Instrumentation)
        self.bDecompile.setGeometry(QtCore.QRect(120, 80, 151, 51))
        self.bDecompile.setObjectName("bDecompile")
        self.bDecompile.clicked.connect(self.dMenu)
        self.bDecompile.clicked.connect(Instrumentation.close)
        
        self.bRecompile = QtWidgets.QPushButton(Instrumentation)
        self.bRecompile.setGeometry(QtCore.QRect(300, 80, 151, 51))
        self.bRecompile.setObjectName("bRecompile")
        self.bRecompile.clicked.connect(self.rMenu)
        self.bRecompile.clicked.connect(Instrumentation.close)
        
        self.bBack = QtWidgets.QPushButton(Instrumentation)
        self.bBack.setGeometry(QtCore.QRect(10, 140, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(Instrumentation.close)

        self.retranslateUi(Instrumentation)
        QtCore.QMetaObject.connectSlotsByName(Instrumentation)

    def retranslateUi(self, Instrumentation):
        _translate = QtCore.QCoreApplication.translate
        Instrumentation.setWindowTitle(_translate("Instrumentation", "Instrumentation and Tampering"))
        self.bDynamic.setText(_translate("Instrumentation", "Dynamic\nInstrumentation"))
        self.bPatch.setText(_translate("Instrumentation", "Patching"))
        self.bSign.setText(_translate("Instrumentation", "Sign APK"))
        self.bDecompile.setText(_translate("Instrumentation", "Decompile"))
        self.bRecompile.setText(_translate("Instrumentation", "Recompile"))
        self.bBack.setText(_translate("Instrumentation", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Instrumentation()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
