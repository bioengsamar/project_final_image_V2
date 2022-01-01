# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laplace.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ui_mainwindow(object):
    def setupUi(self, ui_mainwindow):
        ui_mainwindow.setObjectName("ui_mainwindow")
        ui_mainwindow.resize(474, 465)
        self.centralwidget = QtWidgets.QWidget(ui_mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 90, 301, 201))
        self.label.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        ui_mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ui_mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 21))
        self.menubar.setObjectName("menubar")
        ui_mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ui_mainwindow)
        self.statusbar.setObjectName("statusbar")
        ui_mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(ui_mainwindow)
        QtCore.QMetaObject.connectSlotsByName(ui_mainwindow)

    def retranslateUi(self, ui_mainwindow):
        _translate = QtCore.QCoreApplication.translate
        ui_mainwindow.setWindowTitle(_translate("ui_mainwindow", "laplacian"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_mainwindow = QtWidgets.QMainWindow()
    ui = Ui_ui_mainwindow()
    ui.setupUi(ui_mainwindow)
    ui_mainwindow.show()
    sys.exit(app.exec_())

