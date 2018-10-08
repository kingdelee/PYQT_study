from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                              QRadioButton, QMessageBox, QButtonGroup)
import sys
import traceback

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)

        self.bt = QPushButton('提交', self)
        self.bt.move(300, 200)


        self.rb1 = QRadioButton('你是', self)
        # self.rb1.toggled.connect(lambda:print('hello'))
        self.rb2 = QRadioButton('我是', self)
        self.rb3 = QRadioButton('他是', self)

        self.rb4 = QRadioButton('美女', self)
        self.rb5 = QRadioButton('帅哥', self)
        self.rb6 = QRadioButton('小屁孩', self)

        self.bg1 = QButtonGroup(self)
        self.bg2 = QButtonGroup(self)

        for position, i in zip([(x, y) for x in range(100, 201, 100) for y in range(100, 170, 30)],
                               [self.rb1, self.rb2, self.rb3, self.rb4, self.rb5, self.rb6]):
            i.move(position[0], position[1])
            if position[0] == 100:
                self.bg1.addButton(i, position[1])
            else:
                self.bg2.addButton(i, position[1])

        self.bg1.buttonClicked.connect(self.rbcclicked)
        self.bg2.buttonClicked.connect(self.rbcclicked)

        self.bt.clicked.connect(self.submit)

        self.info1 = ''
        self.info2 = ''

        self.show()

    def submit(self):
        if self.info1 == '' and self.info2 == '':
            QMessageBox.information(self, '提示', '你一项没选')

        else:
            QMessageBox.information(self, '提示', self.info1 + self.info2)

    def rbcclicked(self):
        sender = self.sender()
        if sender == self.bg1:
            if sender.checkedId() == 100:
            # if sender.checkedButton() == self.rb1:
                print(sender.checkedId())
                # print(sender.checkedButton())
                self.info1 = '你是'
            elif sender.checkedId() == 130:
                self.info1 = '我是'
            elif sender.checkedId() == 160:
                self.info1 = '他是'
            else:
                self.info1 = ''
        elif sender == self.bg2:
            if sender.checkedId() == 100:
                self.info2 = '美女'
            elif sender.checkedId() == 130:
                self.info2 = '帅哥'
            elif sender.checkedId() == 160:
                self.info2 = '小屁孩'
            else:
                self.info2 = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    em = Example()
    sys.exit(app.exec_())