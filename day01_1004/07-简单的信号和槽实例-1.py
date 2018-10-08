import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial

class Example(QWidget):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300 ,400, 300)
        self.setWindowTitle(self.title)

        lcd = QLCDNumber(self)
        lcd.setGeometry(100, 50, 150, 60)

        dial = QDial(self)
        dial.setGeometry(120, 120, 100, 100)

        dial.valueChanged.connect(lcd.display)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    title = os.path.basename(sys.argv[0]).split('.')[0]

    window = Example(title)

    sys.exit(app.exec_())