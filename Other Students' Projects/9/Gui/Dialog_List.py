# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Dialog_List.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogList(object):
    def setupUi(self, DialogList):
        DialogList.setObjectName("DialogList")
        DialogList.resize(622, 751)
        self.widget = QtWidgets.QWidget(DialogList)
        self.widget.setGeometry(QtCore.QRect(0, 0, 621, 751))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0.0524476, y1:0.0909091, x2:1, y2:1, stop:0 rgba(209, 109, 165, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 601, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(141)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;font: 12pt \"B Nazanin\";")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 30, 581, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(370, 130, 61, 51))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;font: 12pt \"B Nazanin\";")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.radioButtonName = QtWidgets.QRadioButton(self.widget)
        self.radioButtonName.setGeometry(QtCore.QRect(430, 130, 88, 19))
        self.radioButtonName.setStyleSheet("color:white;font: 10pt \"B Nazanin\";")
        self.radioButtonName.setChecked(True)
        self.radioButtonName.setObjectName("radioButtonName")
        self.radioButtonFamily = QtWidgets.QRadioButton(self.widget)
        self.radioButtonFamily.setGeometry(QtCore.QRect(430, 160, 131, 19))
        self.radioButtonFamily.setStyleSheet("color:white;font: 10pt \"B Nazanin\";")
        self.radioButtonFamily.setObjectName("radioButtonFamily")

        self.retranslateUi(DialogList)
        QtCore.QMetaObject.connectSlotsByName(DialogList)

    def retranslateUi(self, DialogList):
        _translate = QtCore.QCoreApplication.translate
        DialogList.setWindowTitle(_translate("DialogList", "List Of Contacts"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DialogList", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DialogList", "Famliy Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DialogList", "Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DialogList", "Phone"))
        self.label_2.setText(_translate("DialogList", "Contacts List :"))
        self.label.setText(_translate("DialogList", "Contact Manager System"))
        self.label_3.setText(_translate("DialogList", "Sort"))
        self.radioButtonName.setText(_translate("DialogList", "Name"))
        self.radioButtonFamily.setText(_translate("DialogList", "Family Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogList = QtWidgets.QDialog()
    ui = Ui_DialogList()
    ui.setupUi(DialogList)
    DialogList.show()
    sys.exit(app.exec_())