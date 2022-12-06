# Frida Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.instrumentation as instrumentation
import py_asset.basicUtils as basicUtils
import json
import os
import time

class Ui_DynamicInstrumentation(object):
    
    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = instrumentation.Ui_Instrumentation()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def fAlert(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()

    appJSON = ""
    
    def FridaCheck(self):
        self.tListApp.clear()
        retval = basicUtils.checkFrida()
        if retval == 3:
            self.fAlert("No Device Connected")
        elif retval == 1:
            self.listingAPP()
        else:
            self.fAlert("Frida Server Not Found")
    
    def crafter(self,script,SorA):
        row = self.tListApp.currentRow()
        if SorA == 0:
            idtf = self.appJSON[row]['identifier']
            if script == 0:
                com = "start cmd /c frida -U -l py_asset/script/ssl.js -f "+idtf+" --no-pause"
                return com
            elif script == 1:
                com = "start cmd /c frida -U -l py_asset/script/root.js -f "+idtf+" --no-pause"
                return com
            elif script == 2:
                com = "start cmd /c frida -U -l py_asset/script/alert.js -f "+idtf+" --no-pause"
                return com
        else:
            pid = str(self.appJSON[row]['pid'])
            if script == 0:
                com = "start cmd /c frida -U -l py_asset/script/ssl.js -F "+pid+" --no-pause"
                return com
            elif script == 1:
                com = "start cmd /c frida -U -l py_asset/script/root.js -F "+pid+" --no-pause"
                return com
            elif script == 2:
                com = "start cmd /c frida -U -l py_asset/script/alert.js -F "+pid+" --no-pause"
                return com

    def cDynamicSpawn(self):
        # text
        # value = self.ComboBox.currentText()
        # currentIndex
        value = self.ComboBox.currentIndex()
        com = self.crafter(value,0)
        os.system(com)
        time.sleep(1.7)
        self.listingAPP()
    
    def cDyanmicAttach(self):
        value = self.ComboBox.currentIndex()
        com = self.crafter(value,1)
        os.system(com)
        time.sleep(1.7)
        self.listingAPP()

    def listingAPP(self):
        self.bSpawn.setEnabled(False)
        self.bAttach.setEnabled(False)
        self.tApp.clear()
        vAPP = basicUtils.fridaList().decode()
        self.appJSON = json.loads(vAPP)
        self.tListApp.clear()
        self.appJSON = sorted(self.appJSON,key=lambda d:d['name'].lower())
        for i in self.appJSON:
            self.tListApp.addItem(i['name'])
    
    def currentAPP(self):
        row = self.tListApp.currentRow()
        self.tApp.setText("Name => " + self.appJSON[row]['name'] + " || Pid => " + str(self.appJSON[row]['pid']))
        self.bSpawn.setEnabled(True)
        if str(self.appJSON[row]['pid']) == "None":
            self.bAttach.setEnabled(False)
        else:
            self.bAttach.setEnabled(True)

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
        self.tListApp.itemClicked.connect(self.currentAPP)

        # Button Listing
        self.ListApp = QtWidgets.QPushButton(DynamicInstrumentation)
        self.ListApp.setGeometry(QtCore.QRect(10, 90, 101, 31))
        self.ListApp.setObjectName("ListApp")
        self.ListApp.clicked.connect(self.FridaCheck)

        # Spawn Button
        self.bSpawn = QtWidgets.QPushButton(DynamicInstrumentation)
        self.bSpawn.setGeometry(QtCore.QRect(460, 50, 131, 31))
        self.bSpawn.setObjectName("bSpawn")
        self.bSpawn.setEnabled(False)
        self.bSpawn.clicked.connect(self.cDynamicSpawn)

        # Attach Button
        self.bAttach = QtWidgets.QPushButton(DynamicInstrumentation)
        self.bAttach.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bAttach.setObjectName("bAttach")
        self.bAttach.setEnabled(False)
        self.bAttach.clicked.connect(self.cDyanmicAttach)

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
