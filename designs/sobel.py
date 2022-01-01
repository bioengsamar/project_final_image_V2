# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sobel.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ui_main(object):
    def setupUi(self, ui_main):
        ui_main.setObjectName("ui_main")
        ui_main.resize(500, 516)
        self.centralwidget = QtWidgets.QWidget(ui_main)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 50, 81, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 110, 301, 201))
        self.label_3.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        ui_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ui_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        ui_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ui_main)
        self.statusbar.setObjectName("statusbar")
        ui_main.setStatusBar(self.statusbar)

        self.retranslateUi(ui_main)
        QtCore.QMetaObject.connectSlotsByName(ui_main)

    def retranslateUi(self, ui_main):
        _translate = QtCore.QCoreApplication.translate
        ui_main.setWindowTitle(_translate("ui_main", "sobel"))
        self.comboBox.setCurrentText(_translate("ui_main", "Directions"))
        self.comboBox.setItemText(0, _translate("ui_main", "Directions"))
        self.comboBox.setItemText(1, _translate("ui_main", "X"))
        self.comboBox.setItemText(2, _translate("ui_main", "Y"))
        self.comboBox.setItemText(3, _translate("ui_main", "XY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_main = QtWidgets.QMainWindow()
    ui = Ui_ui_main()
    ui.setupUi(ui_main)
    ui_main.show()
    sys.exit(app.exec_())

