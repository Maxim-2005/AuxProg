import pyautogui as a
from PySide2 import QtCore
from modules.Form import Ui_AuxProg

class Main(Ui_AuxProg):
    """код автокликера"""
    def __init__(self):
        super().__init__()
        self.click_X = "x"
        self.click_Y = "y"
        self.setupUi(self)
        self.show()
        #Сигналы слоты
        self.click_status = False
        self.presskeytoclick.clicked.connect(self.button_click)

    def button_click(self):
        self.click_status = not self.click_status
        if self.click_status:
            self.autoclick()
    def autoclick(self):
        while True:
            a.click()
            print("test")
