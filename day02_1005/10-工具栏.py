import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, qApp
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('My Computer')

        self.statusBar().showMessage('ready')

        self.exit_act = QAction('退出(&E)', self)
        self.exit_act.setShortcut('ctrl+e')
        self.exit_act.setStatusTip('退出')
        self.exit_act.triggered.connect(qApp.quit)

        self.save_menu = QMenu('保存方式(&S)', self)

        save_act = QAction(QIcon('wxy.jpeg'), '保存', self)
        save_act.setShortcut('ctrl+s')
        save_act.setStatusTip('保存文件')

        saves_act = QAction('另存为', self)
        saves_act.setShortcut('ctrl+alt+s')
        saves_act.setStatusTip('另存文件')

        self.save_menu.addAction(save_act)
        self.save_menu.addAction(saves_act)
        self.save_menu.addAction('hello')

        menu = self.menuBar()
        file_menu = menu.addMenu('文件(&F)')
        file_menu.addMenu(self.save_menu)
        file_menu.addSeparator()
        # file_menu.setStatusTip('文件')
        file_menu.addAction(self.exit_act)

        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(save_act)
        toolbar.addAction(saves_act)


        self.show()

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        new = menu.addAction('新建')
        save = menu.addMenu(self.save_menu)
        _exit = menu.addAction(self.exit_act)
        a = event.pos()
        b = self.mapToGlobal(a)
        action = menu.exec_(a)
        # if action == _exit:


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())