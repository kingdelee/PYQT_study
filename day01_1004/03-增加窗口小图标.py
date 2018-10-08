import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('增加窗口小图标')
        icon = QIcon('wxy.jpeg')
        # icon = QIcon('web.ico')
        self.setWindowIcon(icon)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()

    sys.exit(app.exec_())