# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DescribeScreenSGNaCP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(428, 337)
        MainWindow.setStyleSheet(u"[objectName=\"centralwidget\"] {\n"
"background-color: rgb(85, 0, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.q_edt = QTextEdit(self.centralwidget)
        self.q_edt.setObjectName(u"q_edt")
        font = QFont()
        font.setPointSize(15)
        self.q_edt.setFont(font)

        self.gridLayout.addWidget(self.q_edt, 0, 0, 1, 1)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(50, 50))
        font1 = QFont()
        font1.setFamily(u"aakar")
        font1.setPointSize(15)
        self.save_btn.setFont(font1)
        self.save_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;}")

        self.gridLayout.addWidget(self.save_btn, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u" SAVE ", None))
    # retranslateUi

