# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormjlSzMk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AuxProg(object):
    def setupUi(self, AuxProg):
        if not AuxProg.objectName():
            AuxProg.setObjectName(u"AuxProg")
        AuxProg.setEnabled(True)
        AuxProg.resize(209, 219)
        AuxProg.setMouseTracking(False)
        AuxProg.setStyleSheet(u"QDialog {\n"
"	\n"
"	background-color: rgb(72, 72, 72);\n"
"}\n"
"\n"
"\n"
".QPushButton {\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(59, 59, 59);\n"
"	font: 75 8pt \"System\";\n"
"}\n"
"\n"
"#pushButton{\n"
"}\n"
"")
        self.pushButton = QPushButton(AuxProg)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 30, 191, 31))
        self.pushButton_2 = QPushButton(AuxProg)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 70, 191, 31))
        self.pushButton_3 = QPushButton(AuxProg)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 0, 50, 20))
        self.pushButton_4 = QPushButton(AuxProg)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 0, 50, 20))
        self.label = QLabel(AuxProg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 170, 171, 61))
        font = QFont()
        font.setFamily(u"Xirod")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_5 = QPushButton(AuxProg)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 110, 101, 21))
        self.pushButton_6 = QPushButton(AuxProg)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(120, 110, 21, 21))
        self.pushButton_7 = QPushButton(AuxProg)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 140, 101, 21))
        self.pushButton_8 = QPushButton(AuxProg)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(120, 140, 21, 21))
        self.pushButton_9 = QPushButton(AuxProg)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 170, 101, 21))
        self.lineEdit = QLineEdit(AuxProg)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 170, 81, 20))
        self.label_2 = QLabel(AuxProg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 171, 16, 16))
        self.checkBox = QCheckBox(AuxProg)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(123, 110, 21, 21))
        self.checkBox_2 = QCheckBox(AuxProg)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(123, 140, 21, 21))
        self.pushButton_10 = QPushButton(AuxProg)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(155, 115, 41, 41))
        self.pushButton_11 = QPushButton(AuxProg)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(160, 0, 50, 20))

        self.retranslateUi(AuxProg)

        QMetaObject.connectSlotsByName(AuxProg)
    # setupUi

    def retranslateUi(self, AuxProg):
        AuxProg.setWindowTitle(QCoreApplication.translate("AuxProg", u"AuxProg", None))
        self.pushButton.setText(QCoreApplication.translate("AuxProg", u"Press \"Key\" to Click", None))
        self.pushButton_2.setText(QCoreApplication.translate("AuxProg", u"Help", None))
        self.pushButton_3.setText(QCoreApplication.translate("AuxProg", u"Options", None))
        self.pushButton_4.setText(QCoreApplication.translate("AuxProg", u"File", None))
        self.label.setText(QCoreApplication.translate("AuxProg", u"AUXPROG", None))
        self.pushButton_5.setText(QCoreApplication.translate("AuxProg", u"Freeze Cursor", None))
        self.pushButton_6.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("AuxProg", u"Double Click", None))
        self.pushButton_8.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("AuxProg", u"Frequency", None))
        self.lineEdit.setText(QCoreApplication.translate("AuxProg", u"100", None))
        self.label_2.setText(QCoreApplication.translate("AuxProg", u"ms", None))
        self.checkBox.setText("")
        self.checkBox_2.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("AuxProg", u"Test", None))
        self.pushButton_11.setText(QCoreApplication.translate("AuxProg", u"Exit", None))
    # retranslateUi

