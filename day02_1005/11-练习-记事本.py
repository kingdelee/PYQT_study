import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction,
                              qApp, QMessageBox, QMenu)
from PyQt5.QtGui import QIcon

class Text(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('记事本')
        self.setWindowIcon(QIcon('text.ico'))

        status = self.statusBar()
        status.showMessage('准备就绪')
        # 文件菜单
        menu = self.menuBar()  # 创建菜单栏
        file_menu = menu.addMenu('文件(&F)')  # 加入文件菜单
        file_action_list = ['新建(&N)', '打开(&O)...', '保存(&S)', '另存为(&A)...',
                            '页面设置(&U)...', '打印(&P)...', '退出(&X)']
        file_action_shortcut = ['Ctrl+N', 'Ctrl+O', 'Ctrl+s',
                                '', '', 'Ctrl+P', 'Ctrl+m']

        for action, shortcut in zip(file_action_list, file_action_shortcut):
            file_action = QAction(action, self)
            if shortcut:
                file_action.setShortcut(shortcut)
            file_menu.addAction(file_action)
            if action == '退出(&X)':
                file_action.triggered.connect(self.quit)

        # 编辑菜单
        edit_menu = menu.addMenu('编辑(&E)')
        edit_action_list = ['撤销(&U)', '剪切(T)', '复制(C)', '粘贴(&P)'
                            '删除(&L)', '查找(&F)', '查找下一个(&N)',
                            '替换(&R)', '转到(&G)', '全选(&A)', '事件/日期(&D)']

        edit_action_shortcut = ['Ctrl+Z', 'Ctrl+X', 'Ctrl+C', 'Ctrl+V', 'Del', 'Ctrl+F',
                              'F3', 'Ctrl+H', 'Ctrl+G', 'Ctrl+A', 'F5']

        for action, shortcut in zip(edit_action_list, edit_action_shortcut):
            edit_action = QAction(action, self)
            if shortcut:
                edit_action.setShortcut(shortcut)
            edit_menu.addAction(edit_action)

        # 格式菜单
        format_menu = menu.addMenu('格式(&O)')
        format_menu.addAction('自动换行(&W)')
        format_menu.addAction('字体(&F)')

        # 查看菜单
        view_menu = menu.addMenu('查看(&V)')
        view_menu.addAction('状态栏(&S)')

        # 帮助菜单
        help_menu = menu.addMenu('帮助(&H)')
        help_menu.addAction('查看帮助(&H)')
        help_menu.addAction('关于记事本(&A)')

        self.show()

    def quit(self):
        reply = QMessageBox.question(self, '退出', '是否退出',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            qApp.quit()

    def contextMenuEvent(self, event):
        print('1111111')
        menu = QMenu(self)
        file_action_list = ['撤销(&U)', '剪切(&T)', '复制(&C)', '粘贴(&P)',
                            '删除(&D)', '全选(&A)', '从左到右阅读顺序(R)',
                            '显示Unicode控制字符(&S)', '打开IME(O)', '汉字重选(R)']
        unicode_name = ['LRM', 'RLM', 'ZWJ', 'ZWNJ', 'LRE', 'RLE', 'LRO', 'PDF', 'NADS',
                        'NODS', 'ASS', 'ISS', 'AAFS', 'IAFS', 'RS', 'US']
        menu1 = QMenu('插入Unicode控制字符(&S)', self)
        for i in unicode_name:
            menu1.addAction(i)

        for j in file_action_list:
            menu.addAction(j)
            if j == '显示Unicode控制字符(&S)':
                menu.addMenu(menu1)
        menu.addSeparator()

        action = menu.exec_(self.mapToGlobal(event.pos()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    text = Text()
    sys.exit(app.exec_())
