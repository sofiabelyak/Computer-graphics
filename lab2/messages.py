"""
    Модуль для вывода сообщений
"""

import tkinter as tk
from PIL import ImageTk, Image


NAME = 'Беляк Софья'
GROUP = 'ИУ7-42Б'
AUTHOR = NAME + '\n' + GROUP

levels = []

def create_okbox(title, text, shift):
    infobox = tk.Toplevel()
    levels.append(infobox)
    infobox.title(title)
    infobox.geometry(shift)
    infobox.resizable(False, False)
    lbl_img = tk.Label(infobox)
    lbl_img.grid(row=1, column=1)
    lbl_text = tk.Label(infobox)
    lbl_text.grid(row=1, column=3)
    lbl_text.configure(text=text, justify=tk.LEFT, font=('Courier', 12))
    btn_ok = tk.Button(infobox)
    btn_ok.grid(row=3, column=0, columnspan=5)
    btn_ok.configure(text='OK')
    btn_ok.configure(command=infobox.destroy)


def create_infobox(title, text):
    create_okbox(title, text, '+700+450')

def create_errorbox(title, text):
    create_okbox(title, text, '+700+450')

def author():
    create_infobox('Об авторе', AUTHOR)

def destroy_toplevels():
    for level in levels:
        level.destroy()
