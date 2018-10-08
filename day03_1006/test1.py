from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self, parent):
        self.parent = parent
        print('11111111')
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 200, 200)
        self.bt1 = QPushButton('我', self)
        self.bt1.move(50, 50)
        self.bt1.clicked.connect(self.quit)
        self.show()

    def quit(self):
        self.parent.show()
        QCoreApplication.instance().quit()


if __name__ == '__main__':
    a = QApplication([])
    em = Example()
    a.exec_()