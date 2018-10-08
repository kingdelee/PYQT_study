import sys
import traceback
from PyQt5.QtWidgets import (QApplication, QWidget, QColorDialog,
                              QFileDialog, QFontDialog,QTextEdit, QPushButton)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('颜色字体文件')

        self.text = QTextEdit(self)
        self.text.setGeometry(20, 20, 300, 270)

        self.bt1 = QPushButton('文件', self)
        self.bt1.move(350, 20)

        self.bt2 = QPushButton('字体', self)
        self.bt2.move(350, 80)

        self.bt3 = QPushButton('颜色', self)
        self.bt3.move(350, 140)

        self.bt1.clicked.connect(self.fileopen)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)

        self.show()


    def fileopen(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', './', 'python (*.py)')
        print(fname)
        if fname[0]:
            with open(r'%s' % fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.text.setText(f.read())

    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            # self.text.setCurrentFont(font)
            self.text.setFont(font)

    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.text.setTextColor(col)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
