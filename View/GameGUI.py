from tkinter import *
import random
from Game.GameUtils import *
from Game.Game import Game
from Game.Box import Box


class MyFirstGUI:
    def __init__(self, root, game):
        self.root = root
        root.title("shut the box GUI")
        root.minsize(600, 300)
        self.game = game
        self.total = 0

        self.label = Label(root, text="Shut The Box", font=('Arial', 20))
        self.label.pack()

        self.start_game = Button(root, text='Start Game', font=('Arial', 18), height=1, width=10, command=lambda: self.play_game())
        self.start_game.pack(side=BOTTOM, pady=100)

        self.root.mainloop()  # keep this at bottom

    def play_game(self):

        self.start_game.destroy()

        label1 = Label(root, text="You rolled a:", font=('Arial', 25), fg='red')
        label1.pack(side=TOP, pady=1)
        roll_label = Label(root, text=(next(roll_die(6, 2))), font=('Arial', 25), fg='red')
        roll_label.pack(side=TOP, pady=1)

        number_button_frame = Frame(self.root)
        number_button_frame.pack(side=TOP, pady=30)

        buttons = []

        numbers = self.game.box.pieces

        for index in range(len(numbers)):
            n = numbers[index]

            button = Button(number_button_frame, text=n, font=('Arial', 18), height=1, width=2,
                            command=lambda num=n, i=index: [self.get_number_clicked(num), self.disable_button(i, buttons),
                                                            self.get_button_index(i)])
            button.grid(padx=5, pady=2, row=2, column=index)

            buttons.append(button)

        extra_button_frame = Frame(self.root)
        extra_button_frame.pack(side=BOTTOM)

        end = Button(extra_button_frame, text='End Game', font=('Arial', 13), height=1, width=13)
        reset = Button(extra_button_frame, text='Reset Selection', font=('Arial', 13), height=1, width=13)
        reset.grid(padx=5, pady=5, row=2)
        end.grid(padx=5, pady=5, row=1)

        playing = True
        roll = 0
        change_roll = True
        # while playing:
        #     number_of_die = self.game.number_of_die()
        #     roll = self.game.get_next_roll()
        #     roll_label.config(text='You rolled a ' + str(roll))
        #     if not self.game.box.combination_not_possible(roll):
        #         pass
                # get user button choices

                # if button is 'end' button, display lose message

                # else, process choices (function of game object)

            # if roll not possible, display lose message



    def get_number_clicked(self, n):
        return n

    def get_button_index(self, i):
        return i

    def disable_button(self, i, buttons):
        buttons[i].config(state='disabled')

    # def next_roll(self):
    #     next_roll = self.game.get_next_roll()
    #     self.roll.config('text'="You rolled a " + str(next_roll))


if __name__ == '__main__':
    root = Tk()
    box = Box([1, 2, 3, 4, 5, 6, 7, 8, 9])
    game = Game(box)
    my_gui = MyFirstGUI(root, game)
