from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class StartUI(QMainWindow):
    def __init__(self):
        super(StartUI, self).__init__()
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Shut The Box')

        self.initUI()

    def initUI(self):
        self.single = QtWidgets.QPushButton(self)
        self.single.setText('Single Player')
        self.single.move(125, 100)
        self.single.resize(250, 50)
        self.single.clicked.connect(self.clicked)

        self.multi = QtWidgets.QPushButton(self)
        self.multi.setText('Multiplayer')
        self.multi.move(125, 250)
        self.multi.resize(250, 50)
        self.multi.clicked.connect(self.clicked)

    def clicked(self):
        self.app1 = QApplication(sys.argv)
        self.win2 = ChooseGameUI()
        self.win2.show()

        # sys.exit(self.app1.exec_())


class ChooseGameUI(QMainWindow):
    def __init__(self):
        super(ChooseGameUI, self).__init__()
        self.setGeometry(200, 200, 500, 700)
        self.setWindowTitle('Choose Game Version')

        self.initUI()

    def initUI(self):
        self.normal_game = QtWidgets.QPushButton(self)
        self.normal_game.setText('1. The Normal Game: 9 pieces up, 2 die')
        self.normal_game.move(50, 50)
        self.normal_game.resize(250, 50)

        self.two_to_go = QtWidgets.QPushButton(self)
        self.two_to_go.setText(
            '2. 2 To Go: the 2 is automatically removed, if the first roll is a 4, the game ends')
        self.two_to_go.move(50, 100)
        self.two_to_go.resize(250, 50)

        self.three_to_go = QtWidgets.QPushButton(self)
        self.three_to_go.setText(
            '3. 3 To Go: the 3 is automatically removed, if the first roll is a 4, the game ends')
        self.three_to_go.move(50, 150)
        self.three_to_go.resize(250, 50)

        self.three_down_extreme = QtWidgets.QPushButton(self)
        self.three_down_extreme.setText(
            '4. 3 Down Extreme: numbers 1, 2 and 3 are pre-dropped, leaving numbers 4 to 9 up')
        self.three_down_extreme.move(50, 200)
        self.three_down_extreme.resize(250, 50)

        self.all_odds = QtWidgets.QPushButton(self)
        self.all_odds.setText(
            '5. Against All Odds: only the odd numbers are up')
        self.all_odds.move(50, 250)
        self.all_odds.resize(250, 50)

        self.all_evens = QtWidgets.QPushButton(self)
        self.all_evens.setText('6. Even-Stevens: only the even numbers are up')
        self.all_evens.move(50, 300)
        self.all_evens.resize(250, 50)

        self.full_house = QtWidgets.QPushButton(self)
        self.full_house.setText('7. Full House: numbers 1 - 12 are up')
        self.full_house.move(50, 350)
        self.full_house.resize(250, 50)

        self.digital = QtWidgets.QPushButton(self)
        self.digital.setText(
            '8. Digital: final score is the combination of the peices left (i.e. 1, 2, 5 = 125)')
        self.digital.move(50, 400)
        self.digital.resize(250, 50)

        self.thai_style = QtWidgets.QPushButton(self)
        self.thai_style.setText(
            '9. Thai Style: you can only chose one of the numbers you rolled or their sum')
        self.thai_style.move(50, 450)
        self.thai_style.resize(250, 50)

        self.the_300 = QtWidgets.QPushButton(self)
        self.the_300.setText(
            '10. The 300: 24 numbers to play with, 4 die (initially)')
        self.the_300.move(50, 500)
        self.the_300.resize(250, 50)

        self.twenty_twelve = QtWidgets.QPushButton(self)
        self.twenty_twelve.setText('11. 2012: 20-sided die playing 12 numbers')
        self.twenty_twelve.move(50, 550)
        self.twenty_twelve.resize(250, 50)


def window():
    app = QApplication(sys.argv)
    win = StartUI()
    win.show()

    sys.exit(app.exec_())


window()
