import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
                              QLCDNumber, QPushButton)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个格栅布局实例并设置窗口为格栅布局
        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('计算器')

        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd, 0, 0, 3, 0)
        # grid.setSpacing(10)
        # 按键的名称
        names = ['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        postions = [(x, y) for x in range(4, 9) for y in range(4, 8)]

        for name, postion in zip(names, postions):
            if name == '':
                continue

            button = QPushButton(name, self)
            grid.addWidget(button, *postion)
            button.clicked.connect(self.clk)

        self.show()

    def clk(self):
        sender = self.sender()
        if sender.text() in ['/', '*', '+', '-', '=']:
            self.lcd.display('A')

        else:
            self.lcd.display(sender.text())

if __name__ == '__main__':
    print('2222222')
    app = QApplication(sys.argv)
    calc = Calculator()

    sys.exit(app.exec_())