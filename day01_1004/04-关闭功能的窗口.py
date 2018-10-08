import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('关闭功能的窗口')
        self.setWindowIcon(QIcon('wxy.jpeg'))

        button = QPushButton('关闭', self)
        button.clicked.connect(QCoreApplication.instance().quit)
        button.setGeometry(140, 120,100, 60)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())