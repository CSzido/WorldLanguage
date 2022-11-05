################################
# Imports
################################
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

################################
# Constants
################################
languages = [
    "Arabic",
    "English",
    "Turkish",
    "Japanese",
    "German"
]
lines = []
Currentline = None
################################
# GUI
################################
root = Tk()
root.title("WorldPad")
# Icon
root.config(background="#222")
root.grid_columnconfigure(0, weight=1)

class Line:
    next = 1
    count = 0

    def __init__(self):
        global Currentline
        self.number = Line.next
        self.nxtline = self.number + 1
        self.input = Entry(root, borderwidth=0, bg="#222", font=("Terminal", 18), fg="#fff")
        # increment
        Line.count += 1
        Line.next += 1
        # adding line to the list
        lines.append(self)
        Currentline = self

    def currentline(self):
        global Currentline
        Currentline = self
        self.input.config(bg="#333")
        self.input.focus_set()
        self.input.grid(sticky="we")

    def reset(self):
        self.input.config(bg="#222")

    def nextline(self, new=False):
        global Currentline
        if new:
            print(self.number)
            if self.number != Line.count:
                theline = Line()
                theline.input.grid(sticky="we")
                theline.currentline()
            else:
                theline = Line()
                theline.input.grid(sticky="we")
                theline.currentline()
                Currentline = lines[self.number]

    def __del__(self):
        self.number -= 1
# noinspection PyUnresolvedReferences
def nxt(e):
    Currentline.reset()
    Currentline.nextline(new=True)


# noinspection PyUnresolvedReferences
def down(e):
    Currentline.reset()
    if Currentline.number < len(lines):
        lines[Currentline.number].currentline()
    Currentline.currentline()


# noinspection PyUnresolvedReferences
def remove(e):
    global Currentline
    if Currentline.number - 1 > 0 and Currentline.input.get() == "":
        if not lines[Currentline.number-1]:
            lines[Currentline.number-1].currentline()
        else:
            lines[Currentline.number-1].reset()
            lines[Currentline.number - 2].currentline()
            del(lines[Currentline.number])
            print(lines)
            Line.count -= 1
            #print(Currentline.number)
            print(Line.count)


# noinspection PyUnresolvedReferences
def up(e):
    global Currentline
    if Currentline.number - 1 > 0 and Currentline.input.get() == "":
        lines[Currentline.number - 2].currentline()
        lines[Currentline.number].reset()


line1 = Line()
line1.currentline()
print(Currentline)
root.bind('<Return>', nxt)
root.bind('<Down>', down)
root.bind('<BackSpace>', remove)
root.bind('<Up>', up)
root.mainloop()
