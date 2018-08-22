# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Oct 27 12:02:13 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtCore, QtGui
from generatereport import GenerateReport
from aktualizuj import Aktualizuj
from time import sleep

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        Aktualizuj(2.4)
        MainWindow.resize(777, 497)
        MainWindow.setMinimumSize(QtCore.QSize(777, 497))
        MainWindow.setMaximumSize(QtCore.QSize(777, 497))
        MainWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Pictures/picture_notepad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("Qt::WStyle_Customize | Qt::WStyle_NoBorderr | Qt::WStyle_Dialog"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("Qt::WStyle_Customize | Qt::WStyle_NoBorderr | Qt::WStyle_Dialog"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.label.setMinimumSize(QtCore.QSize(801, 0))
        self.label.setMaximumSize(QtCore.QSize(801, 501))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 31, 51))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 340, 271, 291))
        self.label_3.setMinimumSize(QtCore.QSize(271, 291))
        self.label_3.setMaximumSize(QtCore.QSize(271, 291))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 400, 501, 51))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 60, 221, 271))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 50, 211, 61))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 440, 191, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 10, 411, 51))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.button_reset = QtGui.QPushButton(self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(280, 450, 101, 31))
        self.button_reset.setStyleSheet(_fromUtf8("border:2px solid white;\n"
"color:white;\n"
"font-family:\'Segoe UI Light\',\'Segoe UI\',sans-serif;\n"
"font-size:18px;"))
        self.button_reset.setObjectName(_fromUtf8("button_reset"))
        self.button_start = QtGui.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(390, 450, 101, 31))
        self.button_start.setStyleSheet(_fromUtf8("border:2px solid rgb(72, 216, 0);\n"
"color:white;\n"
"font-family:\'Segoe UI Light\',\'Segoe UI\',sans-serif;\n"
"font-size:18px;"))
        self.button_start.setObjectName(_fromUtf8("button_start"))
        self.ready = QtGui.QLabel(self.centralwidget)
        self.ready.setGeometry(QtCore.QRect(500, 440, 41, 51))
        self.ready.setObjectName(_fromUtf8("ready"))
        self.button_minimalize = QtGui.QPushButton(self.centralwidget)
        self.button_minimalize.setGeometry(QtCore.QRect(730, 10, 21, 21))
        self.button_minimalize.setStyleSheet(_fromUtf8("background-image: url(:/Buttons/button_minimize.png);\n"
"background-repeat:no-repeat;\n"
"border:0px solid white;"))
        self.button_minimalize.setText(_fromUtf8(""))
        self.button_minimalize.setObjectName(_fromUtf8("button_minimalize"))
        self.button_exit = QtGui.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(750, 10, 21, 23))
        self.button_exit.setStyleSheet(_fromUtf8("background-image: url(:/Buttons/button_exit.png);\n"
"background-repeat:no-repeat;\n"
"border:0px solid white;"))
        self.button_exit.setText(_fromUtf8(""))
        self.button_exit.setObjectName(_fromUtf8("button_exit"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(23, 130, 491, 261))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.button_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.button_minimalize, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.lower)
        QtCore.QObject.connect(self.button_reset, QtCore.SIGNAL(_fromUtf8("clicked()")), self.czysc)
        QtCore.QObject.connect(self.button_start, QtCore.SIGNAL(_fromUtf8("clicked()")), self.generatedef)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def czysc(self):
            self.plainTextEdit.clear()
            self.ready.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Buttons/picture_statusbad.png\"/></p></body></html>", None))
    def generatedef(self):
            if str(self.plainTextEdit.toPlainText())==None:
                pass
            else:

                GenerateReport(str(self.plainTextEdit.toPlainText()))
                self.ready.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Buttons/picture_statusgood.png\"/></p></body></html>", None))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "APNOZ", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Pictures/backround.png\"/></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Pictures/picture_arrow.png\"/></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Pictures/picture_notepad.png\"/></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Pictures/picture_bluebar.png\"/></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Text/text_manual.png\"/></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Pictures/picture_logo.png\"/></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Text/text_about.png\"/></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Text/text_title.png\"/></p></body></html>", None))
        self.button_reset.setText(_translate("MainWindow", "Reset", None))
        self.button_start.setText(_translate("MainWindow", "Start", None))
        self.ready.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Buttons/picture_statusbad.png\"/></p></body></html>", None))

import Assets_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

