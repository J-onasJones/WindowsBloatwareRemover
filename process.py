# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Working(object):
    def setupUi(self, Working):
        Working.setObjectName("Working")
        Working.resize(881, 426)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Working.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Working)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 70, 821, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.titleLabel.setObjectName("titleLabel")
        self.progressOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.progressOutput.setGeometry(QtCore.QRect(30, 100, 821, 301))
        self.progressOutput.setObjectName("progressOutput")
        Working.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Working)
        self.statusbar.setObjectName("statusbar")
        Working.setStatusBar(self.statusbar)

        self.retranslateUi(Working)
        QtCore.QMetaObject.connectSlotsByName(Working)

    def retranslateUi(self, Working):
        _translate = QtCore.QCoreApplication.translate
        Working.setWindowTitle(_translate("Working", "Working...."))
        self.titleLabel.setText(_translate("Working", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Working...</span></p></body></html>"))
