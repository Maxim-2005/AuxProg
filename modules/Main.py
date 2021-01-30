import pyautogui as a
from PySide2 import QtCore, QtWidgets
from modules.Form import Ui_AuxProg

class Main(Ui_AuxProg, QtWidgets.QDialog):
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
        self.timer.setInterval(0)
        self.timer.timeout.connect(self.autoclick)
        self.click_status = False
        self.presskeytoclick.clicked.connect(self.button_click)

    def button_click(self):
        """Переключение авктокликера"""
        self.click_status = not self.click_status
        if self.click_status:
            self.timer.start()
            self.presskeytoclick.setText("STOP")
        else:
            self.presskeytoclick.setText("START")
            self.timer.stop()

    def autoclick(self):
        """Автоклик"""
        a.tripleClickclick()
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