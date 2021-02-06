import pyautogui as a
from PySide2 import QtCore, QtWidgets
from modules.Form import Ui_Form

class Main(Ui_Form, QtWidgets.QWidget):
    """код автокликера"""
    def __init__(self):
        super().__init__()
        self.posX = "x"
        self.posY = "y"
        self.setupUi(self)
        self.installEventFilter(self)
        self.show()
        #Сигналы слоты
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.autoclick)
        self.click_status = False
        self.OnOff.clicked.connect(self.button_click)

    def button_click(self):
        """Переключение авктокликера"""
        self.click_status = not self.click_status
        if self.click_status:
            self.timer.start()
            self.OnOff.setText("STOP")
        else:
            self.OnOff.setText("START")
            self.timer.stop()

    def autoclick(self):
        """Автоклик"""
        a.tripleClick()
        a.tripleClick()
        a.tripleClick()
        print("test")

    def mouseMoveEvent(self, e):
        """Позиция курсора(Qt)"""
        self.posX.setText(str(e.x()))
        self.posY.setText(str(e.y()))

    def keyPressEvent(self, e):
        """Горячие клавищи(Qt)"""
        if e.key():
            self.label_ms.setText(str(chr(e.key())))
        e.accept()