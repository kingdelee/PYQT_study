import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                              QLineEdit, QMessageBox, QHBoxLayout,
                              QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt

class QQLongin(QWidget):

    def __init__(self):
        super().__init__()
        self.login()
        self.passwd = 123456

    def login(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('达内聊天室')
        self.setWindowIcon(QIcon('qq.jpg'))

        self.button1 = QPushButton('登录', self)
        self.button2 = QPushButton('退出', self)
        # self.button1.setGeometry(150, 150, 100, 50)
        # self.button2.setGeometry(250, 150, 100, 50)
        self.button2.clicked.connect(QCoreApplication.instance().quit)
        self.button1.clicked.connect(self.verify_passwd)

        self.text1 = QLineEdit('用户名', self)
        self.text2 = QLineEdit(self)
        self.text2.setEchoMode(QLineEdit.Password)
        self.text2.setContextMenuPolicy(Qt.NoContextMenu)
        self.text2.setPlaceholderText('请输入密码')
        self.text1.setGeometry(150, 50, 200, 50)
        # self.text2.setGeometry(150, 100, 200, 50)
        self.text1.selectAll()
        self.text2.selectAll()
        self.text1.setFocus()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.text1)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.text2)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.button1)
        hbox3.addWidget(self.button2)
        hbox3.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = QQLongin()
    sys.exit(app.exec_())

