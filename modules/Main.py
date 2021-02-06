import pyautogui as a
from PySide2 import QtCore, QtWidgets
from modules.Form import Ui_Form

class Main(Ui_Form, QtWidgets.QWidget):
    """Код автокликера"""
    def __init__(self):
        super().__init__()
        self.click_x = 0
        self.click_y = 0
        self.tempo = 100
        self.setupUi(self)
        self.installEventFilter(self)
        self.show()
        #Сигналы-слоты
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(self.tempo)
        self.timer.timeout.connect(self.auto_click)
        self.click_status = False
        self.Startstop.clicked.connect(self.button_click)

    def button_click(self):
        """Автокликер-Переключатель"""
        self.click_status = not self.click_status
        if self.click_status:
            self.timer.start()
            self.Startstop.setText("стоп/СТАРТ")
        else:
            self.timer.stop()
            self.Startstop.setText("СТОП/старт")

    def auto_click(self):
        """Автокликек-Кликер"""
        a.click()

    def mousePressEvent(self, e):
        """Автокликер-Позиция курсора(Qt)"""
        self.posX.setText(str(e.x()))
        self.posY.setText(str(e.y()))