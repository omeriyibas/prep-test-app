# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QuestionScreenohTgIv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import rsc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1104, 785)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"[objectName=\"centralwidget\"] {\n"
"background-color: rgb(85, 0, 255);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridFrame = QFrame(self.centralwidget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalFrame = QFrame(self.gridFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.q_edt = QTextEdit(self.horizontalFrame)
        self.q_edt.setObjectName(u"q_edt")
        font = QFont()
        font.setPointSize(15)
        self.q_edt.setFont(font)

        self.horizontalLayout.addWidget(self.q_edt)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.horizontalFrame_2 = QFrame(self.gridFrame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 30, -1)
        self.cb1 = QCheckBox(self.horizontalFrame_2)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.cb1)
        self.cb1.setObjectName(u"cb1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb1.sizePolicy().hasHeightForWidth())
        self.cb1.setSizePolicy(sizePolicy2)
        self.cb1.setMinimumSize(QSize(40, 40))
        self.cb1.setMaximumSize(QSize(40, 40))
        self.cb1.setFont(font)
        self.cb1.setLayoutDirection(Qt.RightToLeft)
        self.cb1.setStyleSheet(u"QCheckBox{border-radius:5px;\n"
"padding-right:3px}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	\n"
"	image: url(:/newPrefix/icons/check.png);\n"
"};\n"
"")
        self.cb1.setIconSize(QSize(15, 15))
        self.cb1.setTristate(False)

        self.horizontalLayout_2.addWidget(self.cb1)

        self.a1_edt = QTextEdit(self.horizontalFrame_2)
        self.a1_edt.setObjectName(u"a1_edt")
        self.a1_edt.setFont(font)

        self.horizontalLayout_2.addWidget(self.a1_edt)


        self.verticalLayout.addWidget(self.horizontalFrame_2)

        self.horizontalFrame_3 = QFrame(self.gridFrame)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, 30, -1)
        self.cb2 = QCheckBox(self.horizontalFrame_3)
        self.buttonGroup.addButton(self.cb2)
        self.cb2.setObjectName(u"cb2")
        sizePolicy2.setHeightForWidth(self.cb2.sizePolicy().hasHeightForWidth())
        self.cb2.setSizePolicy(sizePolicy2)
        self.cb2.setMinimumSize(QSize(40, 40))
        self.cb2.setMaximumSize(QSize(40, 40))
        self.cb2.setFont(font)
        self.cb2.setLayoutDirection(Qt.RightToLeft)
        self.cb2.setStyleSheet(u"QCheckBox{border-radius:5px;\n"
"padding-right:3px}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	\n"
"	image: url(:/newPrefix/icons/check.png);\n"
"};\n"
"")
        self.cb2.setIconSize(QSize(15, 15))
        self.cb2.setTristate(False)

        self.horizontalLayout_3.addWidget(self.cb2)

        self.a2_edt = QTextEdit(self.horizontalFrame_3)
        self.a2_edt.setObjectName(u"a2_edt")
        self.a2_edt.setFont(font)

        self.horizontalLayout_3.addWidget(self.a2_edt)


        self.verticalLayout.addWidget(self.horizontalFrame_3)

        self.horizontalFrame_4 = QFrame(self.gridFrame)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_4.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, -1, 30, -1)
        self.cb3 = QCheckBox(self.horizontalFrame_4)
        self.buttonGroup.addButton(self.cb3)
        self.cb3.setObjectName(u"cb3")
        sizePolicy2.setHeightForWidth(self.cb3.sizePolicy().hasHeightForWidth())
        self.cb3.setSizePolicy(sizePolicy2)
        self.cb3.setMinimumSize(QSize(40, 40))
        self.cb3.setMaximumSize(QSize(40, 40))
        self.cb3.setFont(font)
        self.cb3.setLayoutDirection(Qt.RightToLeft)
        self.cb3.setStyleSheet(u"QCheckBox{border-radius:5px;\n"
"padding-right:3px}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	\n"
"	image: url(:/newPrefix/icons/check.png);\n"
"};\n"
"")
        self.cb3.setIconSize(QSize(15, 15))
        self.cb3.setTristate(False)

        self.horizontalLayout_4.addWidget(self.cb3)

        self.a3_edt = QTextEdit(self.horizontalFrame_4)
        self.a3_edt.setObjectName(u"a3_edt")
        self.a3_edt.setFont(font)

        self.horizontalLayout_4.addWidget(self.a3_edt)


        self.verticalLayout.addWidget(self.horizontalFrame_4)

        self.horizontalFrame_5 = QFrame(self.gridFrame)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_5.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_5.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, -1, 30, -1)
        self.cb4 = QCheckBox(self.horizontalFrame_5)
        self.buttonGroup.addButton(self.cb4)
        self.cb4.setObjectName(u"cb4")
        sizePolicy2.setHeightForWidth(self.cb4.sizePolicy().hasHeightForWidth())
        self.cb4.setSizePolicy(sizePolicy2)
        self.cb4.setMinimumSize(QSize(40, 40))
        self.cb4.setMaximumSize(QSize(40, 40))
        self.cb4.setFont(font)
        self.cb4.setLayoutDirection(Qt.RightToLeft)
        self.cb4.setStyleSheet(u"QCheckBox{border-radius:5px;\n"
"padding-right:3px}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	\n"
"	image: url(:/newPrefix/icons/check.png);\n"
"};\n"
"")
        self.cb4.setIconSize(QSize(15, 15))
        self.cb4.setTristate(False)

        self.horizontalLayout_5.addWidget(self.cb4)

        self.a4_edt = QTextEdit(self.horizontalFrame_5)
        self.a4_edt.setObjectName(u"a4_edt")
        self.a4_edt.setFont(font)

        self.horizontalLayout_5.addWidget(self.a4_edt)


        self.verticalLayout.addWidget(self.horizontalFrame_5)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.save_btn = QPushButton(self.gridFrame)
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

        self.gridLayout.addWidget(self.save_btn, 2, 1, 1, 1)

        self.describe_btn = QPushButton(self.gridFrame)
        self.describe_btn.setObjectName(u"describe_btn")
        self.describe_btn.setMinimumSize(QSize(50, 50))
        self.describe_btn.setFont(font1)
        self.describe_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;}")

        self.gridLayout.addWidget(self.describe_btn, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gridFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cb1.setText("")
        self.cb2.setText("")
        self.cb3.setText("")
        self.cb4.setText("")
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u" SAVE ", None))
        self.describe_btn.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

