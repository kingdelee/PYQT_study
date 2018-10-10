from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('小车快跑')

        self.sld1 = QSlider(Qt.Horizontal, self)
        self.sld1.setGeometry(350, 350, 120, 30)
        self.sld1.setMinimum(0)
        self.sld1.setMaximum(99)
        self.sld1.setTickPosition(QSlider.TicksAbove)

        self.sld2 = QSlider(Qt.Vertical, self)
        self.sld2.setMinimum(0)
        self.sld2.setMaximum(99)
        self.sld2.setGeometry(50, 50, 30, 120)
        self.sld2.setTickPosition(QSlider.TicksLeft)

        self.sld1.valueChanged[int].connect(self.changevalue)
        self.sld2.valueChanged[int].connect(self.changevalue)

        self.lb1 = QLabel(self)
        self.lb1.setPixmap(QPixmap('car.png'))
        self.lb1.setGeometry(100, 100, 300, 200)

        self.lb2 = QLabel('滑块1当前的值：0 ', self)
        self.lb3 = QLabel('滑块2当前的值：0 ', self)

        self.lb2.move(380, 380)
        self.lb3.move(50, 280)

        self.show()

    def changevalue(self, value):
        sender = self.sender()
        if sender == self.sld1:
            self.sld2.setValue(value)
        else:
            self.sld1.setValue(value)
        self.lb2.setText('滑块1当前值为：' + str(value))
        self.lb3.setText('滑块2当前值为：' + str(value))

        if value == 0:
            self.lb1.setPixmap(QPixmap('car.png'))
        elif value > 0 and value < 30:
            self.lb1.setPixmap(QPixmap('car1.png'))
        elif value > 30 and value < 80:
            self.lb1.setPixmap(QPixmap('car2.png'))
        else:
            self.lb1.setPixmap(QPixmap('car3.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())