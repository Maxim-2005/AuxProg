import sys
import pyautogui as a
from PySide2 import QtWidgets
from modules.Form import Ui_Auxprog

class Main(object):
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui_Auxprog = Ui_Auxprog()
    ui_Auxprog.setupUi(form)
    form.show()

    def test1(self):
        print(a.position())

    def test2(self):
        pass

    ui_Auxprog.pushButton_4.clicked.connect(test1)


    sys.exit(app.exec_())