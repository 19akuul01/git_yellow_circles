import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLineEdit


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Вычисление выражений')

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.move(170, 80)
        self.trick_button.clicked.connect(self.hello)

        self.first_value = QLineEdit(self)
        self.first_value.move(30, 80)

        self.second_value = QLineEdit(self)
        self.second_value.move(250, 80)

    def hello(self):
        text = self.first_value.text()
        self.second_value.setText(f'{eval(text)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())
