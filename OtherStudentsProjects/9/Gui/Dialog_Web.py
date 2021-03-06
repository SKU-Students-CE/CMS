# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Dialog_Web.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogWeb(object):
    def setupUi(self, DialogWeb):
        DialogWeb.setObjectName("DialogWeb")
        DialogWeb.resize(622, 751)
        self.widget = QtWidgets.QWidget(DialogWeb)
        self.widget.setGeometry(QtCore.QRect(0, 0, 621, 751))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0.0524476, y1:0.0909091, x2:1, y2:1, stop:0 rgba(209, 109, 165, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.widget.setObjectName("widget")
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
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 370, 101, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEditFirst = QtWidgets.QLineEdit(self.widget)
        self.lineEditFirst.setGeometry(QtCore.QRect(130, 190, 461, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditFirst.setFont(font)
        self.lineEditFirst.setStyleSheet("background-color: rgb(207, 182, 196);color:#004242")
        self.lineEditFirst.setText("")
        self.lineEditFirst.setClearButtonEnabled(True)
        self.lineEditFirst.setObjectName("lineEditFirst")
        self.pushButtonWebAdd = QtWidgets.QPushButton(self.widget)
        self.pushButtonWebAdd.setGeometry(QtCore.QRect(500, 430, 91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.pushButtonWebAdd.setFont(font)
        self.pushButtonWebAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonWebAdd.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(33, 255, 181);")
        self.pushButtonWebAdd.setCheckable(False)
        self.pushButtonWebAdd.setAutoDefault(False)
        self.pushButtonWebAdd.setDefault(False)
        self.pushButtonWebAdd.setFlat(False)
        self.pushButtonWebAdd.setObjectName("pushButtonWebAdd")
        self.lineEditLast = QtWidgets.QLineEdit(self.widget)
        self.lineEditLast.setGeometry(QtCore.QRect(130, 250, 461, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditLast.setFont(font)
        self.lineEditLast.setStyleSheet("background-color: rgb(207, 182, 196);color:#004242")
        self.lineEditLast.setText("")
        self.lineEditLast.setClearButtonEnabled(True)
        self.lineEditLast.setObjectName("lineEditLast")
        self.lineEditEmail = QtWidgets.QLineEdit(self.widget)
        self.lineEditEmail.setGeometry(QtCore.QRect(130, 310, 461, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditEmail.setFont(font)
        self.lineEditEmail.setStyleSheet("background-color: rgb(207, 182, 196);color:#004242")
        self.lineEditEmail.setText("")
        self.lineEditEmail.setClearButtonEnabled(True)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPhone = QtWidgets.QLineEdit(self.widget)
        self.lineEditPhone.setGeometry(QtCore.QRect(130, 370, 461, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditPhone.setFont(font)
        self.lineEditPhone.setStyleSheet("background-color: rgb(207, 182, 196);color:#004242")
        self.lineEditPhone.setText("")
        self.lineEditPhone.setClearButtonEnabled(True)
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 101, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 101, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 101, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.pushButtonWebGet = QtWidgets.QPushButton(self.widget)
        self.pushButtonWebGet.setGeometry(QtCore.QRect(500, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.pushButtonWebGet.setFont(font)
        self.pushButtonWebGet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonWebGet.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(33, 255, 181);")
        self.pushButtonWebGet.setCheckable(False)
        self.pushButtonWebGet.setAutoDefault(False)
        self.pushButtonWebGet.setDefault(False)
        self.pushButtonWebGet.setFlat(False)
        self.pushButtonWebGet.setObjectName("pushButtonWebGet")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 471, 51))
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
        self.label_error = QtWidgets.QLabel(self.widget)
        self.label_error.setGeometry(QtCore.QRect(10, 720, 601, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("color:rgb(170, 0, 0)")
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_error.setObjectName("label_error")

        self.retranslateUi(DialogWeb)
        QtCore.QMetaObject.connectSlotsByName(DialogWeb)

    def retranslateUi(self, DialogWeb):
        _translate = QtCore.QCoreApplication.translate
        DialogWeb.setWindowTitle(_translate("DialogWeb", "Web Contact"))
        self.label.setText(_translate("DialogWeb", "Contact Manager System"))
        self.label_6.setText(_translate("DialogWeb", "Phone"))
        self.pushButtonWebAdd.setText(_translate("DialogWeb", "Add"))
        self.label_5.setText(_translate("DialogWeb", "Email"))
        self.label_3.setText(_translate("DialogWeb", "First Name"))
        self.label_4.setText(_translate("DialogWeb", "Last Name"))
        self.pushButtonWebGet.setText(_translate("DialogWeb", "Get Info"))
        self.label_2.setText(_translate("DialogWeb", "Click To Get Data From \"www.fakenamegenerator.com\""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogWeb = QtWidgets.QDialog()
    ui = Ui_DialogWeb()
    ui.setupUi(DialogWeb)
    DialogWeb.show()
    sys.exit(app.exec_())
