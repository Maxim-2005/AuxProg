import pyautogui as a
from PySide2 import QtCore, QtWidgets
from modules.Form import Ui_Auxprog

class Main(Ui_Auxprog, QtWidgets.QWidget):
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
        self.Delay01.editingFinished.connect(self.set_tempo)
        self.timer.timeout.connect(self.auto_click)
        self.click_status = False
        self.Startstop.clicked.connect(self.button_click)

    def set_tempo(self):
        self.tempo = int(self.Delay01.text())
        print(self.tempo)

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
        print('1')

    def mouseMoveEvent(self, e):
        """Автокликер-Позиция курсора(Qt)"""
        self.posX.setText(str(e.x()))
        self.posY.setText(str(e.y()))

    def keyPressEvent(self, e):
        """Автокликер-Горячие клавиши(Qt)"""
        if e.key():
            #self.label_2.setText(str(chr(e.key())))
        e.accept()