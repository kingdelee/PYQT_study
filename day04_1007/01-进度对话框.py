from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog)
from PyQt5.QtCore import Qt
import sys
import time

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 150)
        self.setWindowTitle("微信公众号：学点编程吧--进度对话框")
        self.setWindowModality(Qt.ApplicationModal)

        self.lb = QLabel("文件数量", self)
        self.lb.move(20, 40)

        self.bt1 = QPushButton('开始', self)
        self.bt1.move(20, 80)

        self.bt2 = QPushButton('你好', self)
        self.bt2.move(20, 100)

        self.edit = QLineEdit('1000000', self)
        self.edit.move(100, 40)

        self.show()

        self.bt1.clicked.connect(self.showDialog)

    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5)
        # progress.setAutoReset(False)
        # progress.setWindowModality(Qt.WindowModal)
        progress.setWindowModality(Qt.ApplicationModal)
        # progress.setWindowModality(Qt.NonModal)
        progress.setRange(500000, 1000000)
        # progress.setMinimum(5000000)
        # progress.setMaximum(10000000)
        for i in range(num + 10):
            # time.sleep(0.1)
            print(i)
            if i < 500000:
                continue
            # print(i)
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作失败")
                break
        # else:
        #     progress.setValue(i)
            if i == 1000000:
                QMessageBox.information(self, "提示", "操作成功")
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())