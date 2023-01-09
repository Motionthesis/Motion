# Sign Menu
from PyQt5 import QtCore, QtGui, QtWidgets
import py_asset.instrumentation as instrumentation
import os
import subprocess
import time

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
        
    locationWindows = "C:\\"

    base = os.getcwd()

    def sAlert(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def timeLog(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime())
    
    def uiUpdate(self):
        QtGui.QGuiApplication.processEvents()

    def browseFile(self):
        fileLocation = QtWidgets.QFileDialog.getOpenFileName(None,'Select APK',self.locationWindows,"Android File (*apk)")
        self.lPath.setText(fileLocation[0])
        if ".apk" in fileLocation[0]:
            self.bSign.setEnabled(True)
        else:
            self.bSign.setEnabled(False)

    def sign(self):
        self.bFalse()
        fileLocation = self.lPath.text()
        tmpLocation = fileLocation.split("/")
        tmp = fileLocation.replace(tmpLocation[-1],"")
        self.lLog.appendPlainText(self.timeLog() + " Signing " + tmpLocation[-1])
        self.uiUpdate()
        os.chdir(tmp)
        s = subprocess.Popen(['keytool','-genkey','-noprompt','-keystore' ,'file.keystore','-alias','alias1','-keysize','2048','-validity','10000','-dname', 'CN=pp,OU=ID,O=IBM,L=H,S=H,C=GB', '-storepass','123456', '-keypass','123456','-keyalg','RSA'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).wait()
        self.lLog.appendPlainText(self.timeLog() + " Keystore Generated")
        self.uiUpdate()
        if self.cAndroid.isChecked():
            y = subprocess.Popen(['zipalign','-p','-f','4',fileLocation,'signed.apk'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            c = subprocess.Popen(['apksigner','sign','--ks-key-alias','alias1','--ks','file.keystore','--ks-pass','pass:123456','signed.apk'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            self.lLog.appendPlainText(self.timeLog() + " APK Sign By APKSigner")
            self.uiUpdate()
        else:
            x = subprocess.Popen(['jarsigner','-sigalg','SHA1withRSA','-digestalg','SHA1','-keystore','file.keystore',fileLocation,'alias1','-storepass','123456','-keypass','123456'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out,err = x.communicate()
            # print(out,err)
            self.lLog.appendPlainText(self.timeLog() + " APK Sign By Jarsigner")
            self.uiUpdate()
            y = subprocess.Popen(['zipalign','-p','-f','4',fileLocation,'signed.apk'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out,err = y.communicate()
            # print(out,err)
        self.lLog.appendPlainText(self.timeLog() + " Signed APK Location " + tmp + "signed.apk")
        self.uiUpdate()
        self.sAlert("Sign Success, Location "+tmp+"signed.apk")
        self.uiUpdate()
        self.lLog.appendPlainText(self.timeLog() + " Sign Success\n")
        self.uiUpdate()
        os.chdir(self.base)
        self.bTrue()
   
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
        self.bSelect.clicked.connect(self.browseFile)

        self.bSign = QtWidgets.QPushButton(SignAPK)
        self.bSign.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.bSign.setObjectName("bSign")
        self.bSign.setEnabled(False)
        self.bSign.clicked.connect(self.sign)

        self.lLog = QtWidgets.QPlainTextEdit(SignAPK)
        self.lLog.setGeometry(QtCore.QRect(10, 90, 721, 200))
        self.lLog.setReadOnly(True)
        self.lLog.setObjectName("lLog")
        
        self.cAndroid = QtWidgets.QCheckBox(SignAPK)
        self.cAndroid.setGeometry(QtCore.QRect(510, 50, 91, 31))
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
