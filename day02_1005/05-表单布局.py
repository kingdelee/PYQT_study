import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QHBoxLayout,
                              QVBoxLayout, QLineEdit, QMessageBox, QFormLayout, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class QQLongin(QWidget):

    def __init__(self):
        super().__init__()
        self.login()
        self.passwd = 123456

    def login(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('QQ登录')
        self.setWindowIcon(QIcon('../day01_1004/qq.jpg'))

        self.button1 = QPushButton('登录', self)
        self.button2 = QPushButton('退出', self)

        # self.button2.clicked.connect(QCoreApplication.instance().quit)
        self.button2.clicked.connect(self.quit)
        self.button1.clicked.connect(self.verify_passwd)

        self.text1 = QLineEdit('用户名', self)
        self.text2 = QLineEdit('密码', self)
        self.text1.selectAll()
        self.text2.selectAll()
        self.text1.setFocus()
        self.text2.setFocus()

        name_label = QLabel('name', self)
        passwd_label = QLabel('password', self)

        form = QFormLayout()

        form.addRow(name_label, self.text1)
        form.addRow(passwd_label, self.text2)
        form.addRow(self.button1, self.button2)

        hbox= QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(form)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.show()

    def verify_passwd(self):
        input_passwd = int(self.text2.text())
        if input_passwd == self.passwd:
            QMessageBox.about(self, '密码验证', '密码正确')
        else:
            QMessageBox.about(self, '密码验证', '密码错误')
            self.text2.clear()
            self.text2.setFocus()

    def closeEvent(self, event):
        reply = QMessageBox.warning(self, '退出', '确认退出？',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def quit(self):
        print('111111111')
        reply = QMessageBox.critical(self, '退出', '确认退出吗',
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No )

        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = QQLongin()
    sys.exit(app.exec_())

