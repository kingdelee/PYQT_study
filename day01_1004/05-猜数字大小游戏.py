import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                              QMessageBox, QLineEdit)
from PyQt5.QtGui import QIcon
from random import randint

class Example(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()
        self.num = randint(1, 100)
        print(self.num)

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('猜数字大小游戏')
        self.setWindowIcon(QIcon('wxy.jepg'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        self.bt1.clicked.connect(self.showMessage)

        self.text = QLineEdit('在这里输入数字', self)
        # print(self.text.text())
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def showMessage(self):
        guessnum = int(self.text.text())

        if guessnum > self.num:
            QMessageBox.about(self, '看结果', '猜大了')
            # self.text.clear()
            self.text.setFocus()
        elif guessnum < self.num:
            QMessageBox.about(self, '看结果', '猜小了')
            # self.text.clear()
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '猜对了!进入下一轮')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()

    sys.exit(app.exec_())