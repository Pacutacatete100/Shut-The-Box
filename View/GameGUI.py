from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def clicked():
    print('clicked')


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 300, 500, 400)
    win.setWindowTitle("Shut The Box")

    single = QtWidgets.QPushButton(win)
    single.setText("Single Player")
    single.move(125, 100)
    single.resize(250, 50)
    single.clicked.connect(clicked)

    multi = QtWidgets.QPushButton(win)
    multi.setText("Multiplayer")
    multi.move(125, 250)
    multi.resize(250, 50)
    multi.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())


window()
