import traceback
from PyQt5.QtWidgets import (QDialog, QApplication, QLineEdit,QLabel,QWidget,
                              QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator


class PasswdDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(350, 100)
        self.setWindowTitle('密码输入框')

        self.la = QLabel('请输入密码', self)

        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)
        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit.setPlaceholderText('密码6-15位，只能数字和字母，必须以字母开头')
        self.edit.setEchoMode(QLineEdit.Password)

        self.bt1 = QPushButton('确认', self)
        self.bt2 = QPushButton('取消', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.bt1)
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.la)
        vbox.addWidget(self.edit)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        regex = QRegExp(r'^[a-zA-Z][a-zA-Z0-9]{14}$')
        validator = QRegExpValidator(regex, self.edit)
        self.edit.setValidator(validator)

        self.bt1.clicked.connect(self.ok)
        self.bt2.clicked.connect(self.cancel)

        object = QObject()

    def eventFilter(self, object, event):
        if object == self.edit:  # 如果接受事件的对象是QLineEdit生成的对象
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or \
                        key.matches(QKeySequence.Paste):
                    return True

        return QDialog.eventFilter(self, object, event)


    def ok(self):
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, '警告', '密码为空')
        elif len(self.text) < 6:
            QMessageBox.warning(self, '警告', '密码长度低于6位')
        else:
            self.done(1)

    def cancel(self):
        self.done(0)

def a():
    passwd = PasswdDialog()
    r = passwd.exec_()

if __name__ == '__main__':
    app = QApplication([])
    ex = QWidget()
    ex.setGeometry(300, 300, 300, 300)
    bt = QPushButton('haha', ex)
    bt.move(100, 100)
    bt.clicked.connect(a)
    ex.show()
    app.exec_()
