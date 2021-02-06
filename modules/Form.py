# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledOfmyOa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(190, 190)
        icon = QIcon()
        icon.addFile(u"../../../../b8ca4fe6d5fa432462cc4dadb22c6068.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(60,60,60);")
        self.OnOff = QPushButton(Form)
        self.OnOff.setObjectName(u"OnOff")
        self.OnOff.setGeometry(QRect(20, 10, 151, 50))
        font = QFont()
        font.setFamily(u"Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.OnOff.setFont(font)
        self.OnOff.setStyleSheet(u"#OnOff{\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(85, 85, 255);\n"
"}")
        self.pos_x = QLabel(Form)
        self.pos_x.setObjectName(u"pos_x")
        self.pos_x.setGeometry(QRect(40, 160, 71, 20))
        self.pos_x.setFont(font)
        self.pos_x.setStyleSheet(u"#pos_x{\n"
"	color: rgb(85, 85, 255);\n"
"}")
        self.y = QLabel(Form)
        self.y.setObjectName(u"y")
        self.y.setGeometry(QRect(80, 160, 20, 21))
        self.y.setFont(font)
        self.x = QLabel(Form)
        self.x.setObjectName(u"x")
        self.x.setGeometry(QRect(10, 160, 31, 20))
        self.x.setFont(font)
        self.pos_y = QLabel(Form)
        self.pos_y.setObjectName(u"pos_y")
        self.pos_y.setGeometry(QRect(110, 160, 71, 20))
        self.pos_y.setFont(font)
        self.pos_y.setStyleSheet(u"#pos_y{\n"
"	color: rgb(85, 85, 255);\n"
"}")
        self.tempotext = QLabel(Form)
        self.tempotext.setObjectName(u"tempotext")
        self.tempotext.setGeometry(QRect(20, 100, 161, 31))
        self.tempotext.setFont(font)
        self.tempotext.setStyleSheet(u"#tempotext{\n"
"	color: rgb(85, 85, 255);\n"
"}")
        self.freeze = QCheckBox(Form)
        self.freeze.setObjectName(u"freeze")
        self.freeze.setGeometry(QRect(20, 70, 151, 17))
        self.freeze.setFont(font)
        self.freeze.setStyleSheet(u"#freeze{\n"
"	color: rgb(85, 85, 255);\n"
"}")
        self.tempo = QLineEdit(Form)
        self.tempo.setObjectName(u"tempo")
        self.tempo.setGeometry(QRect(20, 130, 151, 20))
        self.tempo.setFont(font)
        self.tempo.setStyleSheet(u"#tempo{\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(85, 85, 255);\n"
"}")
        self.symbol = QLabel(Form)
        self.symbol.setObjectName(u"symbol")
        self.symbol.setGeometry(QRect(150, 150, 41, 41))
        font1 = QFont()
        font1.setFamily(u"Berlin Sans FB Demi")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.symbol.setFont(font1)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AuxProg", None))
        self.OnOff.setText(QCoreApplication.translate("Form", u"Start/Stop", None))
        self.pos_x.setText(QCoreApplication.translate("Form", u"0", None))
        self.y.setText(QCoreApplication.translate("Form", u"Y:", None))
        self.x.setText(QCoreApplication.translate("Form", u"X :", None))
        self.pos_y.setText(QCoreApplication.translate("Form", u"0", None))
        self.tempotext.setText(QCoreApplication.translate("Form", u"Repetition rate:", None))
        self.freeze.setText(QCoreApplication.translate("Form", u"FreezeCursor", None))
        self.symbol.setText(QCoreApplication.translate("Form", u"#", None))
    # retranslateUi

