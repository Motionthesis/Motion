#Uninstall Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.basicUtils as basicUtils
import py_asset.utilMenu as utilmenu
import json

class Ui_UninstallAPK(object):

    def bButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = utilmenu.Ui_Utility()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def gAlert(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()

    appJSON = ""
    
    def FridaCheck(self):
        self.lApps.clear()
        retval = basicUtils.checkFrida()
        if retval == 3:
            self.gAlert("No Device Connected")
        elif retval == 1:
            self.listingAPP()
        else:
            self.gAlert("Frida Server Not Found")

    #Ui
    def sAlert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
        msg.setWindowTitle("Information")
        msg.setText("Uninstall Success")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def fAlert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
        msg.setWindowTitle("Information")
        msg.setText("Fail to Uninstall")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()

    def lAlert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))
        msg.setWindowTitle("Information")
        msg.setText("Cant Find Package or Apps")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()
    ###

    def listingAPP(self):
        vAPP = basicUtils.fridaList().decode()
        self.appJSON = json.loads(vAPP)
        self.lApps.clear()
        self.appJSON = sorted(self.appJSON,key=lambda d:d['name'].lower())
        for i in self.appJSON:
            self.lApps.addItem(i['name'])

    def getAppsNaP(self):
        row = self.lApps.currentRow()
        self.eFilename.setText("Name => " + self.appJSON[row]['name'] + " Identifier => " + self.appJSON[row]['identifier'])
        self.bUninstall.setEnabled(True)

    def pUninstall(self):
        pName = self.eFilename.text()
        if len(pName) == 0:
            self.lAlert()
        else:
            packageName = pName.split(" ")[-1]
            value = basicUtils.uninstall(packageName)
            if b'Success' in value:
                self.sAlert()
            else:
                self.fAlert()
            self.listingAPP()
            self.eFilename.clear()
            self.bUninstall.setEnabled(False)
        
    def setupUi(self, UninstallAPK):
        UninstallAPK.setObjectName("UninstallAPK")
        UninstallAPK.setFixedSize(QtCore.QSize(741, 330))
        UninstallAPK.setWindowIcon(QtGui.QIcon('py_asset/logo.png'))

        #Listing Apps
        self.lApps = QtWidgets.QListWidget(UninstallAPK)
        self.lApps.setGeometry(QtCore.QRect(10, 90, 721, 200))
        self.lApps.setObjectName("lApps")
        self.lApps.itemClicked.connect(self.getAppsNaP)

        # Uninstall Button
        self.bUninstall = QtWidgets.QPushButton(UninstallAPK)
        self.bUninstall.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bUninstall.setAutoDefault(False)
        self.bUninstall.setDefault(False)
        self.bUninstall.setEnabled(False)
        self.bUninstall.setObjectName("bUninstall")
        self.bUninstall.clicked.connect(self.pUninstall)

        #Listing Apps Button
        self.bApplist = QtWidgets.QPushButton(UninstallAPK)
        self.bApplist.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.bApplist.setObjectName("bApplist")
        self.bApplist.clicked.connect(self.FridaCheck)

        #File Text
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
