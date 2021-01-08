import sys
import pyautogui as a
from PySide2 import QtWidgets
from modules.Form import Ui_AuxProg

class Main(object):
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui_AuxProg = Ui_AuxProg()
    ui_AuxProg.setupUi(form)
    form.show()

    def test1(self):
        print("test1")
        print(a.position())

    def test2(self):
        self.ui_AuxProg.test.setText('asdfghjkl')

    ui_AuxProg.freezecursor.clicked.connect(test1)
    ui_AuxProg.test.clicked.connect(test2)

    sys.exit(app.exec_())