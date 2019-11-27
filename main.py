# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from wxpy import *
import datetime as dt
import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 141, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 141, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 141, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 130, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 180, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 180, 256, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 260, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(Dialog.reject)
        self.pushButton.clicked.connect(self.send)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "定时发送"))
        self.label.setText(_translate("Dialog", "目标在你微信列表的名字"))
        self.label_2.setText(_translate("Dialog", "发送的时间"))
        self.label_3.setText(_translate("Dialog", "发送内容"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))


    def send(self):
        self.name = self.lineEdit.text()
        self.sendtime = self.lineEdit_2.text()
        self.message = self.lineEdit_3.text()
        self.textBrowser.setText('请登录')
        self.bot = Bot()
        self.textBrowser.setText('登录成功')
        timer = threading.Timer(2,self.getContent)
        timer.start()


    def getContent(self):
        name = self.name
        sendtime = self.sendtime
        message = self.message
        bot = self.bot
        nowtime = dt.datetime.now().strftime('%H:%M')
        # print("正在执行")
        # self.textBrowser.setText('正在等待')
        if nowtime == '%s'%(sendtime):
            # self.textBrowser.setText('正在发送')
            my_friend = bot.friends().search('%s'%(name))[0]
            my_friend.send('%s'%(message))
            # self.textBrowser.setText('发送成功')
            time.sleep(60)
        timer = threading.Timer(10,self.getContent)
        timer.start()

class MainWindow(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()  # Ui_Dialog为.ui产生.py文件中窗体类名
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
