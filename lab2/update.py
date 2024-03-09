"""
    Модуль для обновления изображения
"""

import tkinter as tk
import copy

import messages as msg


NONNUMERIC = 'Нечисловые данные'
EMPTY = 'Пустой ввод'

NONNUM_MOVE = 'Dx и Dy должны быть представлены вещественными числами'
EMPTY_MOVE = 'Для выполнения переноса заполните поля dx и dy'

NONNUM_SCALE = 'Xc, Yc, Kx и Ky должны быть представлены вещественными числами'
EMPTY_SCALE = 'Для выполнения масштабирования заполните поля Xc, Yc, Kx и Ky'

NONNUM_ROTATION = 'Xc, Yc и угол должны быть представлены вещественными числами'
EMPTY_ROTATION = 'Для выполнения поворота заполните поля Xc, Yc и "Угол"'

FONT = 'Arial'
FONT_SIZE = 12
FONT_CONFIG = (FONT, FONT_SIZE)


class History:
    def __init__(self, index, buf):
        self.index = index
        self.buf = buf
    def add(self, func):
        self.index += 1
        self.buf = self.buf[:self.index] + [func]
    def back(self, home):
        self.index -= 1
        self.update(home)
    def forward(self, home):
        self.index += 1
        self.update(home)
    def update(self, home):
        home_copy = copy.deepcopy(self.buf[self.index])
        for i, part in enumerate(home_copy.full):
            home.full[i] = part
def renew_label(window):
    window.lbl_figure_centre.configure(font=FONT_CONFIG,text="X:{:7.2f}; Y:{:7.2f}".format(window.funcs[9].x_list[0],window.funcs[9].y_list[0]))

def move(window, home, fishes):
    try:
        dx = float(window.ent_dx.get())
        dy = float(window.ent_dy.get())
    except ValueError:
        if window.ent_dx.get() and window.ent_dy.get():
            msg.create_errorbox(NONNUMERIC, NONNUM_MOVE)
        else:
            msg.create_errorbox(EMPTY, EMPTY_MOVE)
    else:
        home.move(dx, dy)
        fishes.add(copy.deepcopy(home))
        window.funcs = home.full
        window.btn_undo.configure(state=tk.NORMAL)
        window.btn_redo.configure(state=tk.DISABLED)
        renew_label(window)
        window.create_matplotlib()


def scale(window, home, fishes):
    try:
        kx = float(window.ent_kx.get())
        ky = float(window.ent_ky.get())
        xc = float(window.ent_xc.get())
        yc = float(window.ent_yc.get())
    except ValueError:
        if (window.ent_kx.get() and window.ent_ky.get()
                and window.ent_xc.get() and window.ent_yc.get()):
            msg.create_errorbox(NONNUMERIC, NONNUM_SCALE)
        else:
            msg.create_errorbox(EMPTY, EMPTY_SCALE)
    else:
        home.scaling(kx, ky, xc, yc)
        fishes.add(copy.deepcopy(home))
        window.funcs = home.full
        window.btn_undo.configure(state=tk.NORMAL)
        window.btn_redo.configure(state=tk.DISABLED)
        window.create_matplotlib()
        renew_label(window)


def rotate(window, home, fishes):
    try:
        phi = float(window.ent_angle.get())
        xc = float(window.ent_xc.get())
        yc = float(window.ent_yc.get())
    except ValueError:
        if (window.ent_xc.get() and window.ent_yc.get()
                and window.ent_angle.get()):
            msg.create_errorbox(NONNUMERIC, NONNUM_ROTATION)
        else:
            msg.create_errorbox(EMPTY, EMPTY_ROTATION)
    else:
        home.rotate(phi, xc, yc)
        fishes.add(copy.deepcopy(home))
        window.btn_undo.configure(state=tk.NORMAL)
        window.btn_redo.configure(state=tk.DISABLED)
        window.funcs = home.full
        window.create_matplotlib()
        renew_label(window)

def reset(window, home, fishes):
    home.reset()
    window.funcs = home.full
    window.create_matplotlib()
    fishes.add(copy.deepcopy(home))
    window.btn_undo.configure(state=tk.NORMAL)
    window.btn_redo.configure(state=tk.DISABLED)
    renew_label(window)
def undo(window, home, fishes):
    if fishes.index:
        fishes.back(home)
        window.funcs = home.full
        window.create_matplotlib()
        window.btn_redo.configure(state=tk.NORMAL)
        renew_label(window)
    if not fishes.index:
        window.btn_undo.configure(state=tk.DISABLED)
def redo(window, home, fishes):
    if fishes.index < len(fishes.buf):
        fishes.forward(home)
        home = fishes.buf[fishes.index]
        window.funcs = home.full
        window.create_matplotlib()
        window.btn_undo.configure(state=tk.NORMAL)
        renew_label(window)
    if fishes.index == len(fishes.buf) - 1:
        window.btn_redo.configure(state=tk.DISABLED)
