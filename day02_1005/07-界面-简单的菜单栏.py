import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('My Computer')
        self.statusBar().showMessage('ready')

        exitAct = QAction(QIcon('wxy.jpeg'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.exit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        # settingMenu = menubar.addMenu('设置(&S)')
        # fileMenu.setShortcut('Ctrl+F')
        fileMenu.addAction(exitAct)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

