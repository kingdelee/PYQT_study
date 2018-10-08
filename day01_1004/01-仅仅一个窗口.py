import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    # 设置桌面坐标(300, 300),长为200，宽为100
    window.setGeometry(300, 300, 200, 100)
    window.setWindowTitle('仅仅一个窗口')
    window.show()

    sys.exit(app.exec_())