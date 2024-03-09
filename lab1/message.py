import tkinter as tk
AUTHOR = 'Беляк Софья ИУ7-42Б'
INFO = ('Лабораторная работа №1.\n'
        'Условие задачи:\n'
        'На плоскости дано множество точек, найти такой выпуклый четырехугольник, вершины которого лежат в точках заданного множества,\n'
        'у которого разность площадей наибольшего и наименьшего треугольников, образованных пересечением диагоналей, минимальна.')


# Создание окна с кнопкой OK.
def create_okbox(title, text, shift):
    infobox = tk.Toplevel()
    infobox.title(title)
    infobox.geometry(shift)
    infobox.resizable(False, False)
    lbl_text = tk.Label(infobox, text=text, justify=tk.LEFT, font=('Arial', 10))
    lbl_text.grid(row=1, column=1, columnspan=3)
    btn_ok = tk.Button(infobox, text='OK', command=infobox.destroy)
    btn_ok.grid(row=2, column=1, columnspan=3)

# Создание информационного окна с кнопкой OK.
def create_infobox(title, text):
    create_okbox(title, text, '+700+450')

# Отображение окна с информацией об авторе.
def author():
    create_infobox('Об авторе', AUTHOR)

# Отображение окна с информацией о лабораторной работе.
def info():
    create_infobox('Информация о лабораторной', INFO)

