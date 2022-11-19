# Frida Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.instrumentation as instrumentation

class Ui_DynamicInstrumentation(object):

    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = instrumentation.Ui_Instrumentation()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, DynamicInstrumentation):
        DynamicInstrumentation.setObjectName("DynamicInstrumentation")
        DynamicInstrumentation.setFixedSize(QtCore.QSize(741, 370))

        self.ComboBox = QtWidgets.QComboBox(DynamicInstrumentation)
        self.ComboBox.setGeometry(QtCore.QRect(10, 50, 321, 31))
        self.ComboBox.setObjectName("ComboBox")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")
        self.ComboBox.addItem("")

        # Listing APP 
        self.tListApp = QtWidgets.QListWidget(DynamicInstrumentation)
        self.tListApp.setGeometry(QtCore.QRect(10, 130, 721, 200))
        self.tListApp.setObjectName("tListApp")

        # Button Listing
        self.ListApp = QtWidgets.QPushButton(DynamicInstrumentation)
        self.ListApp.setGeometry(QtCore.QRect(10, 90, 101, 31))
        self.ListApp.setObjectName("ListApp")

        # Spawn Button
        self.bSpawn = QtWidgets.QPushButton(DynamicInstrumentation)
        self.bSpawn.setGeometry(QtCore.QRect(460, 50, 131, 31))
        self.bSpawn.setObjectName("bSpawn")
        self.bSpawn.setEnabled(False)

        # Attach Button
        self.bAttach = QtWidgets.QPushButton(DynamicInstrumentation)
        self.bAttach.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bAttach.setObjectName("bAttach")
        self.bAttach.setEnabled(False)

        # Text Information
        self.tApp = QtWidgets.QTextEdit(DynamicInstrumentation)
        self.tApp.setGeometry(QtCore.QRect(10, 10, 721, 31))
        self.tApp.setReadOnly(True)
        self.tApp.setObjectName("tApp")

        # Back
        self.bBack = QtWidgets.QPushButton(DynamicInstrumentation)
        self.bBack.setGeometry(QtCore.QRect(10, 340, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(DynamicInstrumentation.close)


        self.retranslateUi(DynamicInstrumentation)
        QtCore.QMetaObject.connectSlotsByName(DynamicInstrumentation)

    def retranslateUi(self, DynamicInstrumentation):
        _translate = QtCore.QCoreApplication.translate
        DynamicInstrumentation.setWindowTitle(_translate("DynamicInstrumentation", "Dynamic Instrumentation"))
        self.ComboBox.setItemText(0, _translate("DynamicInstrumentation", "SSL Pinning"))
        self.ComboBox.setItemText(1, _translate("DynamicInstrumentation", "Root Bypass"))
        self.ComboBox.setItemText(2, _translate("DynamicInstrumentation", "Alert"))
        self.bBack.setText(_translate("DynamicInstrumentation", "Back"))
        self.ListApp.setText(_translate("DynamicInstrumentation", "List App"))
        self.bSpawn.setText(_translate("DynamicInstrumentation", "Spawn"))
        self.bAttach.setText(_translate("DynamicInstrumentation", "Attach"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DynamicInstrumentation = QtWidgets.QWidget()
    ui = Ui_DynamicInstrumentation()
    ui.setupUi(DynamicInstrumentation)
    DynamicInstrumentation.show()
    sys.exit(app.exec_())
