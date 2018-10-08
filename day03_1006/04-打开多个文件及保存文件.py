import sys
import traceback
from PyQt5.QtWidgets import (QApplication, QWidget, QColorDialog,QMessageBox,
                              QFileDialog, QFontDialog,QTextEdit, QPushButton,
                              QDialog)

from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('颜色字体文件')

        self.text = QTextEdit(self)
        self.text.setGeometry(20, 20, 300, 270)

        self.bt1 = QPushButton('打开文件', self)
        self.bt1.move(350, 20)

        self.bt2 = QPushButton('打开多个文件', self)
        self.bt2.move(350, 50)

        self.bt3 = QPushButton('选择字体', self)
        self.bt3.move(350, 80)

        self.bt4 = QPushButton('选择颜色', self)
        self.bt4.move(350, 110)

        self.bt5 = QPushButton('保存文件', self)
        self.bt5.move(350, 140)

        self.bt8 = QPushButton('另存为', self)
        self.bt8.move(350, 170)


        self.bt6 = QPushButton('页面设置', self)
        self.bt6.move(350, 200)

        self.bt7 = QPushButton('打印文档', self)
        self.bt7.move(350, 230)

        self.bt1.clicked.connect(self.fileopen)
        self.bt2.clicked.connect(self.filesopen)
        self.bt3.clicked.connect(self.choicefont)
        self.bt4.clicked.connect(self.choicecolor)
        self.bt5.clicked.connect(self.fileopen)
        self.bt6.clicked.connect(self.pagesetting)
        self.bt7.clicked.connect(self.printdialog)
        self.bt8.clicked.connect(self.filesave)

        self.printer = QPrinter()

        self.show()



    def fileopen(self):
        sender = self.sender()
        if sender == self.bt1:
            self.fname = QFileDialog.getOpenFileName(self, '打开文件', './')
            if self.fname[0]:
                with open(self.fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                    self.text.setText(f.read())
        elif sender == self.bt5:
            try:
                with open(self.fname[0], 'w') as f:
                    f.write(self.text.toPlainText())
                QMessageBox.about(self, 'OK', '文件已保存')
            except:
                QMessageBox.about(self, '警告', '文件未打开')

    def filesopen(self):
        fname = QFileDialog.getOpenFileNames(self, '打开多个文件', './')
        print(fname)
        if fname[0]:
            for filename in fname[0]:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    self.text.append(f.read())

    def filesave(self):
        fname = QFileDialog.getSaveFileName(self, '文件另存为', './')
        if fname[0]:
            try:
                with open(fname[0], 'w') as f:
                    f.write(self.text.toPlainText())
            except:
                traceback.print_exc()

    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            # self.text.setCurrentFont(font)
            self.text.setFont(font)

    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.text.setTextColor(col)

    def pagesetting(self):
        printsetdialog = QPageSetupDialog(self.printer, self)
        printsetdialog.exec_()

    def printdialog(self):
        printdialog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printdialog.exec_():
            self.tx.print(self.printer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
