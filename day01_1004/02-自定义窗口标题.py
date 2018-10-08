import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        if len(sys.argv) < 2:
            raise ValueError
        else:
            title = ' '.join(sys.argv[1:])
    # 如果没有输入参数，则名字为No Name
    except ValueError:
        title = 'No Name'

    window = QWidget()
    window.setGeometry(300, 300, 400, 300)
    window.setWindowTitle(title)
    window.show()

    sys.exit(app.exec_())