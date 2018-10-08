import sys
import traceback
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLineEdit
from passwddialog import PasswdDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('输入密码练习')

        self.bt1 = QPushButton('输入密码', self)
        self.bt1.move(100, 100)
        self.bt2 = QPushButton('输入密码', self)
        self.bt2.move(100, 150)
        self.bt3 = QPushButton('输入密码', self)
        self.bt3.move(100, 200)
        self.bt1.clicked.connect(self.click)
        self.bt2.clicked.connect(self.click)
        self.bt3.clicked.connect(self.click)

        self.show()

    def click(self):
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '密码输入框', '请输入密码', QLineEdit.Password)
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '密码输入框', '请输入密码', QLineEdit.PasswordEchoOnEdit)

        else:
            try:
                passwd = PasswdDialog()
                # passwd.edit.installEventFilter(passwd)
                print('111')
                r = passwd.exec_()
            except:
                traceback.print_exc()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())