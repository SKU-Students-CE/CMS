# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Files\Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 740)
        MainWindow.setStyleSheet("background-color:#002942")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 611, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButtonEditList = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEditList.setGeometry(QtCore.QRect(230, 190, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEditList.setFont(font)
        self.pushButtonEditList.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonEditList.setStyleSheet("background-color:#F4CA16;border-radius:35px;")
        self.pushButtonEditList.setObjectName("pushButtonEditList")
        self.pushButtonIdentufy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonIdentufy.setGeometry(QtCore.QRect(230, 330, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonIdentufy.setFont(font)
        self.pushButtonIdentufy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonIdentufy.setStyleSheet("background-color:#F4CA16;border-radius:35px;")
        self.pushButtonIdentufy.setObjectName("pushButtonIdentufy")
        self.pushButtonWeb = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonWeb.setGeometry(QtCore.QRect(230, 470, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonWeb.setFont(font)
        self.pushButtonWeb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonWeb.setStyleSheet("background-color:#F4CA16;border-radius:35px;")
        self.pushButtonWeb.setObjectName("pushButtonWeb")
        self.pushButtonOpen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpen.setGeometry(QtCore.QRect(140, 610, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonOpen.setFont(font)
        self.pushButtonOpen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonOpen.setStyleSheet("background-color:#F4CA16;border-radius:35px;")
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setGeometry(QtCore.QRect(330, 610, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSave.setStyleSheet("background-color:#F4CA16;border-radius:35px;")
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 270, 581, 16))
        self.line.setStyleSheet("color:#FFFFFF")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 410, 581, 16))
        self.line_2.setStyleSheet("color:#FFFFFF")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 550, 581, 16))
        self.line_3.setStyleSheet("color:#FFFFFF")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 420, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 560, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(30, 130, 581, 16))
        self.line_4.setStyleSheet("color:#FFFFFF")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 140, 20, 581))
        self.line_5.setStyleSheet("color:white")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(610, 140, 20, 581))
        self.line_6.setStyleSheet("color:white")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(30, 690, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet("color:#9ACD32")
        self.labelError.setText("")
        self.labelError.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelError.setObjectName("labelError")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contacts Manager"))
        self.label.setText(_translate("MainWindow", "MyCMS"))
        self.pushButtonEditList.setText(_translate("MainWindow", "Edit\\List"))
        self.pushButtonIdentufy.setText(_translate("MainWindow", "Identify"))
        self.pushButtonWeb.setText(_translate("MainWindow", "Web"))
        self.pushButtonOpen.setText(_translate("MainWindow", "Open"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.label_2.setText(_translate("MainWindow", "Contacts:"))
        self.label_3.setText(_translate("MainWindow", "Data Extracting:"))
        self.label_4.setText(_translate("MainWindow", "Web Scraping:"))
        self.label_5.setText(_translate("MainWindow", "File Functions:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
