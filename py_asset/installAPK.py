# Install APK Menu
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InstallAPK(object):

    def bButton(self):
        import main
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def bFalse(self):
        self.installButton.setEnabled(False)
        self.selectFile.setEnabled(False)
        self.bBack.setEnabled(False)

    def bTrue(self):
        self.installButton.setEnabled(True)
        self.selectFile.setEnabled(True)
        self.bBack.setEnabled(True)
    
    def setupUi(self, InstallAPK):
        InstallAPK.setObjectName("InstallAPK")
        InstallAPK.setFixedSize(QtCore.QSize(741, 330))

        #Install APK Button
        self.installButton = QtWidgets.QPushButton(InstallAPK)
        self.installButton.setGeometry(QtCore.QRect(600, 50, 131, 31))
        self.installButton.setObjectName("installButton")

        #File Path
        self.filePath = QtWidgets.QLineEdit(InstallAPK)
        self.filePath.setGeometry(QtCore.QRect(10, 10, 581, 31))
        self.filePath.setReadOnly(True)
        self.filePath.setObjectName("filePath")
        
        #Select File
        self.selectFile = QtWidgets.QPushButton(InstallAPK)
        self.selectFile.setGeometry(QtCore.QRect(600, 10, 131, 31))
        self.selectFile.setObjectName("selectFile")

        self.logViewer = QtWidgets.QPlainTextEdit(InstallAPK)
        self.logViewer.setGeometry(QtCore.QRect(11, 90, 721, 200))
        self.logViewer.setReadOnly(True)
        self.logViewer.setObjectName("logViewer")

        self.bBack = QtWidgets.QPushButton(InstallAPK)
        self.bBack.setGeometry(QtCore.QRect(10, 300, 81, 21))
        self.bBack.setObjectName("bBack")
        self.bBack.clicked.connect(self.bButton)
        self.bBack.clicked.connect(InstallAPK.close)

        self.retranslateUi(InstallAPK)
        QtCore.QMetaObject.connectSlotsByName(InstallAPK)

    def retranslateUi(self, InstallAPK):
        _translate = QtCore.QCoreApplication.translate
        InstallAPK.setWindowTitle(_translate("InstallAPK", "Install APK/S"))
        self.installButton.setText(_translate("InstallAPK", "Install APK/S"))
        self.selectFile.setText(_translate("InstallAPK", "Select File"))
        self.bBack.setText(_translate("InstallAPK", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InstallAPK()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())