import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ex_1.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.label.setText("OK")
        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
