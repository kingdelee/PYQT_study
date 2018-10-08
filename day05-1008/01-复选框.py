from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

class Example(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('复选框')

        self.bt = QPushButton('提交', self)
        self.bt.move(200, 200)
        self.bt.clicked.connect(self.go)

        self.ck1 = QCheckBox('你好', self)
        self.ck1.move(100, 100)

        self.ck2 = QCheckBox('我好', self)
        self.ck2.move(100, 150)

        self.ck3 = QCheckBox(self)
        self.ck3.setText('大家好 &F')
        self.ck3.setIcon(QIcon("C:/Users/Administrator/Desktop/liuyang/前端课程资料/img-css/rongrong.jpg"))
        self.ck3.move(100, 200)

        self.ck = QCheckBox('全选', self)
        self.ck.move(50, 50)

        self.ck.stateChanged.connect(self.ckall)
        for i in [self.ck1, self.ck2, self.ck3]:
            i.stateChanged.connect(self.changeStates)


        self.show()

    def go(self):
        if self.ck1.isChecked() and self.ck2.isChecked() and self.ck3.isChecked():
            QMessageBox.about(self, '显示', '你好我好大家好')
        elif self.ck1.isChecked() and self.ck2.isChecked():
            QMessageBox.adout(self, '显示', '你好我好')
        elif self.ck1.isChecked() and self.ck3.isChecked():
            QMessageBox.about(self, '显示', '你好大家好')
        elif self.ck2.isChecked() and self.ck3.isChecked():
            QMessageBox.about(self, '显示', '我好大家好')
        elif self.ck1.isChecked():
            QMessageBox.about(self, '显示', '你好')
        elif self.ck2.isChecked():
            QMessageBox.about(self, '显示', '我好')
        elif self.ck3.isChecked():
            QMessageBox.about(self, '显示', '大家好')
        else:
            QMessageBox.about(self, '显示', '大家都不好')

    def ckall(self):
        if self.ck.checkState() == Qt.Checked:
            for i in [self.ck1, self.ck2, self.ck3]:
                # i.setChecked(True)
                i.setCheckState(Qt.Checked)
        elif self.ck.checkState() == Qt.Unchecked:
            for i in [self.ck1, self.ck2, self.ck3]:
                i.setChecked(False)

    def changeStates(self):
        if self.ck1.isChecked() and self.ck2.isChecked() and self.ck3.isChecked():
            self.ck.setCheckState(Qt.Checked)
        elif self.ck1.isChecked() or self.ck2.isChecked() or self.ck3.isChecked():
            self.ck.setTristate()
            self.ck.setCheckState(Qt.PartiallyChecked)
        else:
            self.ck.setTristate(False)
            self.ck.setCheckState(Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    em = Example()
    sys.exit(app.exec_())