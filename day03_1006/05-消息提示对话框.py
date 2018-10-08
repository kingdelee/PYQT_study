import sys
import traceback
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('消息提示对话框')

        self.la = QLabel('这里将显示消息提示', self)
        self.la.move(100, 10)

        self.bt1 = QPushButton('提示', self)
        self.bt1.move(50, 60)

        self.bt2 = QPushButton('询问', self)
        self.bt2.move(150, 60)

        self.bt3 = QPushButton('警告', self)
        self.bt3.move(250, 60)

        self.bt4 = QPushButton('错误', self)
        self.bt4.move(50, 120)

        self.bt5 = QPushButton('关于', self)
        self.bt5.move(150, 120)

        self.bt6 = QPushButton('关于QT', self)
        self.bt6.move(250, 120)

        self.bt1.clicked.connect(self.info)
        self.bt2.clicked.connect(self.question)
        self.bt3.clicked.connect(self.warning)
        self.bt4.clicked.connect(self.critical)
        self.bt5.clicked.connect(self.about)
        self.bt6.clicked.connect(self.aboutqt)

        self.show()

    def info(self):
        reply = QMessageBox.information(self, '提示', '这是一个消息提示',
                                     QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close )

        if reply == QMessageBox.Ok:
            self.la.setText('你选择了Ok')
        else:
            self.la.setText('你选择了Close')


    def question(self):
        reply = QMessageBox.question(self, '询问', '这是一个消息询问',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.la.setText('Yes')
        elif reply == QMessageBox.No:
            self.la.setText('No')
        else:
            self.la.setText('Cancel')

    def warning(self):
        # reply = QMessageBox.question(self, '警告', '这是一个消息警告',
        #                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        try:
            cb = QCheckBox('所有文档按此操作')
            msgbox = QMessageBox()
            msgbox.setWindowTitle('警告')
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText('<b>这是一个消息警告</b>')
            msgbox.setInformativeText('出现更改愿意保存吗')
            save = msgbox.addButton('保存', QMessageBox.AcceptRole)
            docancle = msgbox.addButton('取消', QMessageBox.RejectRole)
            nosave = msgbox.addButton('不保存', QMessageBox.DestructiveRole)
            msgbox.setDefaultButton(save)
            msgbox.setCheckBox(cb)
            msgbox.setWindowModality(Qt.WindowModal)
            # msgbox.setWindowModality(Qt.ApplicationModal)
            cb.stateChanged.connect(self.check)
            # cb.setWindowModality(Qt.WindowModal)
            reply = msgbox.exec()
            if reply == QMessageBox.AcceptRole:
                if cb.isChecked():
                    self.la.setText('您选择了保存并记住此操作')
                else:
                    self.la.setText('你选择了保存')
            elif reply == QMessageBox.RejectRole:
                self.la.setText('你选择了取消')
            else:
                self.la.setText('你选择了不保存')
        except:
            traceback.print_exc()

    def critical(self):
        pass

    def about(self):
        pass

    def aboutqt(self):
        QMessageBox.aboutQt(self, '关于qt')

    def check(self):
        if self.sender().isChecked():
            self.la.setText('你打钩了')
        else:
            self.la.setText('你没打勾')
















if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())