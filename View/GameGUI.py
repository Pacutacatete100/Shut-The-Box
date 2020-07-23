import tkinter as tk
from tkinter import *


class GameWindowStart(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.master = master
        self.master.title('fist window')

        single_button = Button(self, text='Single Player', padx=10, pady=5)
        single_button.place(x=125, y=100)


if __name__ == '__main__':
    root = Tk()
    geo = '500x400'
    root.geometry(geo)

    app = GameWindowStart(root)

    root.mainloop()
