print(a.position())  # Позиция курсора
print(a.size())  # Размер экрана
a.PAUSE = 0.3
a.move(-200, 300)  # Переход в точку
a.move(-200, 300, duration=0.5)  # Перемещение курсора
a.moveTo(500, 500)  # Переход в точку
a.moveTo(100, 100, duration=0.5)  # Переход в точку
a.click()  # Клик
a.moveTo(800, 1080)
a.click(button='right')  # Клик
a.moveTo(850, 980)
a.click()  # Клик
