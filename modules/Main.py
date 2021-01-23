import pyautogui as a
from PySide2 import QtCore
from modules.Form import Ui_Auxprog

class Main(Ui_Auxprog):
    """Код автокликера"""
    def __init__(self):
        super().__init__()
        self.click_x = 0
        self.click_y = 0
        self.setupUi(self)
        self.show()
        #Сигналы-слоты
        self.click_status = False
        self.Startstop.clicked.connect(self.button_click)

    def button_click(self):
        self.click_status = not self.click_status
        if self.click_status:
            self.auto_click()

    def auto_click(self):
        while True:
            a.click()
        print('1')