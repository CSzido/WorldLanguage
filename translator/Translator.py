# Imports
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

from googletrans import Translator

# Constants
FileURL = ""
keywords_base = {
    'var': 'variable',
    'and': 'and',
    'or': 'or',
    'not': 'not',
    'if': 'if',
    'elif': 'else if',
    'else': 'else',
    'from': 'from',
    'to': 'to',
    'step': 'step',
    'while': 'while',
    'func': 'function',
    'do': 'do',
    'end': 'end',
    'return': 'return',
    'continue': 'continue',
    'break': 'break',
    'print': 'print',
    'input': 'input',
    'int_input': 'integer input',
    'int': 'integer',
    'float': 'float',
    'Expected': 'Expected',
    'identifier': 'identifier',
    'is_int': 'is integer?',
    'is_str': 'is string?',
    'is_lst': 'is list?',
    'is_func': 'is function?',
    'null': 'null',
    'true': 'true',
    'false': 'false',
    'clear': 'clean',
    'append': 'append',
    'extend': 'extend',
    'pop': 'pop',
    'len': 'size',
    'NEWLINE': 'new line'
}
languages = [
    "Arabic",
    "English",
    "Turkish",
    "Japanese",
    "German"
]

# GUI
root = Tk()
root.title("WorldLangT")
root.iconbitmap("data/world.ico")
root.geometry("500x415")
OpenButton = Button(root, text="Select file", bg="#21A8F4", fg="#fff", width=70, cursor="hand2")
OpenButton.place(x=0, y=0)
img = PhotoImage(file="data/world.png")
Label(root, image=img).place(x=150, y=27)
container = Frame(root, width=500, height=50, bg="#1A2ABF", borderwidth=12).place(x=0, y=327)
Label(root, text="Select Language : ", bg="#1A2ABF", fg="#fff").place(x=0, y=340)
lang = ttk.Combobox(root, values=languages, width=60)
lang.place(x=100, y=340)
lang.current(1)
Translate_btn = Button(root, text="Translate", bg="#21A8F4", fg="#fff", width=70, cursor="hand2")
Translate_btn.place(x=0, y=365)
mode = StringVar()

offline_btn = ttk.Radiobutton(root, text="Offline", value="Offline", variable=mode)
offline_btn.place(x=360, y=392)

online_btn = ttk.Radiobutton(root, text="Online", value="Online", variable=mode)
online_btn.place(x=430, y=392)


# Functions
def openfile():
    if mode.get() == "":
        messagebox.showerror(title="Select file", message="Please select The mode first! ")
    else:
        global FileURL
        file = filedialog.askopenfilename(filetypes=[("World Files", "*.world"), ("All Files", "*.*")])
        FileURL = file


def translate():
    translator = Translator()
    if FileURL == "":
        messagebox.showerror(title="Select file", message="Please select a file first! ")
    else:
        # Translating Code
        code = open(FileURL, "r", encoding="UTF-8")
        mycode = code.read()
        code.close()
        data = open("keywords.txt", "r", encoding="UTF-8")
        my_data = data.readlines()
        data_dict = dict()
        for i in my_data:
            data_dict[i.split(",")[0].strip()] = i.split(",")[1].strip()
        for i in data_dict:
            mycode = mycode.replace(f"{data_dict[i]}", translator.translate(text=keywords_base[i], dest=lang.get()).text)
        code = open(FileURL, "w+", encoding="UTF-8")
        code.write(mycode)
        code.close()
        # Applying Translation
        f = open("keywords.txt", "w+", encoding="UTF-8")
        f.write("")
        f.close()
        f = open("keywords.txt", "a+", encoding="UTF-8")
        for i in keywords_base:
            f.write(
                f"{i}, {translator.translate(src='En', dest=f'{lang.get()}', text=keywords_base[i]).text.replace(' ', '_')}\n")
        f.close()
        messagebox.showinfo(title="Yuppi :)", message="Done ^u^")


def offline():
    lang.config(state="readonly")
    Translate_btn.config(command=Offline_translate)


def online():
    lang.config(state="normal")
    Translate_btn.config(command=translate)


def Offline_translate():
    # getting current language trans and putting it in a dict
    if FileURL == "":
        messagebox.showerror(title="Select file", message="Please select a file first! ")
    else:
        old_keywords = open("keywords.txt", "r", encoding="UTF-8")
        my_data = old_keywords.readlines()
        old_kw_dict = dict()
        for i in my_data:
            old_kw_dict[i.split(",")[0].strip()] = i.split(",")[1].strip()
        print(old_kw_dict)
        old_keywords.close()
        new_keywords = open(f"data/{lang.get()}_KW.txt", "r", encoding="UTF-8")
        my_data = new_keywords.readlines()
        new_kw_dict = dict()
        for i in my_data:
            new_kw_dict[i.split(",")[0].strip()] = i.split(",")[1].strip()
        print(new_kw_dict)
        new_keywords.close()
    # getting code
        code = open(FileURL, "r", encoding="UTF-8")
        mycode = code.read()
        code.close()
        # replacing old values by new values
        print(old_kw_dict)
        print(new_kw_dict)
        for i in keywords_base:
            mycode = mycode.replace(f"{old_kw_dict[i]}", f"{new_kw_dict[i]}")
        #writing data
        code = open(FileURL, "w+", encoding="UTF-8")
        code.write(mycode)
        code.close()
        open("keywords.txt", "w+", encoding="UTF-8").write(open(f"data/{lang.get()}_KW.txt", "r", encoding="UTF-8").read())
        messagebox.showinfo(title="Yuppi :)", message="Done ^u^")


def test():
    print(mode.get())


OpenButton.config(command=openfile)
offline_btn.config(command=offline)
online_btn.config(command=online)
root.mainloop()
