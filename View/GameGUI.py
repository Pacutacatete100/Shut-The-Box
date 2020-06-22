from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class StartUI(QMainWindow):
    def __init__(self):
        super(StartUI, self).__init__()
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle("Shut The Box")

        self.initUI()

    def initUI(self):
        self.single = QtWidgets.QPushButton(self)
        self.single.setText("Single Player")
        self.single.move(125, 100)
        self.single.resize(250, 50)
        self.single.clicked.connect(self.clicked)

        self.multi = QtWidgets.QPushButton(self)
        self.multi.setText("Multiplayer")
        self.multi.move(125, 250)
        self.multi.resize(250, 50)
        self.multi.clicked.connect(self.clicked)

    def clicked(self):
        print('clicked')


def window():
    app = QApplication(sys.argv)
    win = StartUI()
    win.show()
    sys.exit(app.exec_())


window()
