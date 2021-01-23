# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormfOzHqs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AuxProg(QDialog):
    def setupUi(self, AuxProg):
        if not AuxProg.objectName():
            AuxProg.setObjectName(u"AuxProg")
        AuxProg.setEnabled(True)
        AuxProg.resize(210, 251)
        AuxProg.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u"../../../../b8ca4fe6d5fa432462cc4dadb22c6068.png", QSize(), QIcon.Normal, QIcon.Off)
        AuxProg.setWindowIcon(icon)
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
        self.presskeytoclick = QPushButton(AuxProg)
        self.presskeytoclick.setObjectName(u"presskeytoclick")
        self.presskeytoclick.setGeometry(QRect(10, 30, 191, 31))
        self.help = QPushButton(AuxProg)
        self.help.setObjectName(u"help")
        self.help.setGeometry(QRect(10, 70, 191, 31))
        self.options = QPushButton(AuxProg)
        self.options.setObjectName(u"options")
        self.options.setGeometry(QRect(50, 0, 50, 20))
        self.file = QPushButton(AuxProg)
        self.file.setObjectName(u"file")
        self.file.setGeometry(QRect(0, 0, 50, 20))
        self.label = QLabel(AuxProg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 200, 171, 61))
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
        self.freezecursor = QPushButton(AuxProg)
        self.freezecursor.setObjectName(u"freezecursor")
        self.freezecursor.setGeometry(QRect(10, 110, 101, 21))
        self.pushButton_6 = QPushButton(AuxProg)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(120, 110, 21, 21))
        self.dobuleclick = QPushButton(AuxProg)
        self.dobuleclick.setObjectName(u"dobuleclick")
        self.dobuleclick.setGeometry(QRect(10, 140, 101, 21))
        self.pushButton_8 = QPushButton(AuxProg)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(120, 140, 21, 21))
        self.pushButton_9 = QPushButton(AuxProg)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 170, 101, 21))
        self.ms = QLineEdit(AuxProg)
        self.ms.setObjectName(u"ms")
        self.ms.setGeometry(QRect(120, 170, 81, 20))
        self.label_ms = QLabel(AuxProg)
        self.label_ms.setObjectName(u"label_ms")
        self.label_ms.setGeometry(QRect(180, 171, 16, 16))
        self.checkBox = QCheckBox(AuxProg)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(123, 110, 21, 21))
        self.checkBox_2 = QCheckBox(AuxProg)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(123, 140, 21, 21))
        self.test = QPushButton(AuxProg)
        self.test.setObjectName(u"test")
        self.test.setGeometry(QRect(155, 115, 41, 41))
        self.exit = QPushButton(AuxProg)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(160, 0, 50, 20))
        self.posX = QLabel(AuxProg)
        self.posX.setObjectName(u"posX")
        self.posX.setGeometry(QRect(20, 200, 48, 13))
        self.posX.setStyleSheet(u"#posX{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.posY = QLabel(AuxProg)
        self.posY.setObjectName(u"posY")
        self.posY.setGeometry(QRect(120, 200, 48, 13))
        self.posY.setStyleSheet(u"#posY{\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.retranslateUi(AuxProg)
        self.help.clicked.connect(self.presskeytoclick.hide)
        self.presskeytoclick.clicked.connect(self.dobuleclick.update)

        QMetaObject.connectSlotsByName(AuxProg)
    # setupUi

    def retranslateUi(self, AuxProg):
        AuxProg.setWindowTitle(QCoreApplication.translate("AuxProg", u"AuxProg", None))
        self.presskeytoclick.setText(QCoreApplication.translate("AuxProg", u"Press \"Key\" to Click", None))
        self.help.setText(QCoreApplication.translate("AuxProg", u"Help", None))
        self.options.setText(QCoreApplication.translate("AuxProg", u"Options", None))
        self.file.setText(QCoreApplication.translate("AuxProg", u"File", None))
        self.label.setText(QCoreApplication.translate("AuxProg", u"AUXPROG", None))
        self.freezecursor.setText(QCoreApplication.translate("AuxProg", u"Freeze Cursor", None))
        self.pushButton_6.setText("")
        self.dobuleclick.setText(QCoreApplication.translate("AuxProg", u"Double Click", None))
        self.pushButton_8.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("AuxProg", u"Frequency", None))
        self.ms.setText(QCoreApplication.translate("AuxProg", u"100", None))
        self.label_ms.setText(QCoreApplication.translate("AuxProg", u"ms", None))
        self.checkBox.setText("")
        self.checkBox_2.setText("")
        self.test.setText(QCoreApplication.translate("AuxProg", u"Test", None))
        self.exit.setText(QCoreApplication.translate("AuxProg", u"Exit", None))
        self.posX.setText(QCoreApplication.translate("AuxProg", u"TextLabel", None))
        self.posY.setText(QCoreApplication.translate("AuxProg", u"TextLabel", None))
    # retranslateUi