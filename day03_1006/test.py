from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
import test1
import traceback

def func(m):
    try:
        # m.hide()
        em = test1.Example(m)
    except Exception as e:
        traceback.print_exc()

a = QApplication([])
m = QWidget()
m.setGeometry(300, 300, 200, 200)
bt = QPushButton('另一个', m)
bt.clicked.connect(lambda:func(m))
bt.move(100, 100)
m.show()

a.exec_()