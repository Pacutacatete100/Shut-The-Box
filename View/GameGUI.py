from tkinter import *
import random
from Game.GameUtils import *
from Game.Game import Game
from Game.Box import *


class MyFirstGUI:
    def __init__(self, root, game):
        self.root = root
        root.title("shut the box GUI")
        root.minsize(600, 300)
        self.game = game

        self.label = Label(root, text="Shut The Box GUI", font=('Arial', 18))
        self.label.pack()

        self.roll = Label(root, text=next(roll_die(6, 2)), font=('Arial', 25), fg='red')
        self.roll.pack(side=TOP, pady=100)

        number_button_frame = Frame(self.root)
        number_button_frame.pack(side=BOTTOM, pady=30)

        self.number_buttons = {}

        for n in self.game.pieces:
            self.number_buttons[n] = Button(number_button_frame, text=n, font=('Arial', 18), height=1, width=2, command=lambda num=n: [self.get_number_clicked(num), self.next_roll()])
            self.number_buttons[n].pack(side=LEFT, padx=5)

        self.root.mainloop()  # keep this at bottom

    @staticmethod
    def get_number_clicked(n):
        print(n)
        return int(n)

    def next_roll(self):
        next_roll = next(roll_die(6, 2))
        self.roll.config(text=next_roll)




if __name__ == '__main__':
    root = Tk()
    game = Game([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
    my_gui = MyFirstGUI(root, game)
