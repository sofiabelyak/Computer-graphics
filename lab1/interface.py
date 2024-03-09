import tkinter as tk
import tkinter.ttk as ttk
import message as msg
import points as pnt
import task as task
COLUMNS = ('1', '2')
COLOR = "#F0FFFF"


# Создание меню с командами "Информация об авторе" и "Выход"
def create_menu(window):
    menu = tk.Menu(window)
    menu.add_command(label="Информация об авторе", command=msg.author)
    menu.add_command(label='Выход', command=window.destroy)
    window.config(menu=menu)

# Создание надписей для отображения информации о точках
def create_lables(window):
    lbl_points = tk.Label(window)
    lbl_points.place(relx=0.725, rely=0.0, relwidth=0.25, relheight=0.047)
    lbl_points.configure(background=COLOR)
    lbl_points.configure(font=("Arial", 12))
    lbl_points.configure(text='Таблица точек')
    lbl_x = tk.Label(window)

    lbl_x.place(relx=0.725, rely=0.4, relwidth=0.02, relheight=0.047)
    lbl_x.configure(background=COLOR)
    lbl_x.configure(text='X:')
    lbl_y = tk.Label(window)

    lbl_y.place(relx=0.725, rely=0.46, relwidth=0.02, relheight=0.047)
    lbl_y.configure(background=COLOR)
    lbl_y.configure(text='Y:')

# Создание таблицы для отображения точек
def create_table(window):
    tr_points = ttk.Treeview(window, columns=COLUMNS)
    tr_points.configure(selectmode='browse')
    tr_points.heading('#0', text='№')
    tr_points.heading('#1', text='X')
    tr_points.heading('#2', text='Y')

    tr_points.column('#0', minwidth=30, width=40, stretch=True)
    tr_points.column('#1', minwidth=30, width=108, stretch=True)
    tr_points.column('#2', minwidth=30, width=108, stretch=True)

    tr_points.place(relx=0.725, rely=0.057, relheight=0.337, relwidth=0.25)

    scr_points = ttk.Scrollbar(tr_points, orient='vertical',
                               command=tr_points.yview)
    tr_points.configure(yscrollcommand=scr_points.set)
    scr_points.pack(side='right', fill='y')

    return tr_points

# Создание кнопок для управления точками и задачами
def create_buttons(window, points, entries, canvas):
    btn_add = tk.Button(window)
    btn_add.place(relx=0.725, rely=0.53, relwidth=0.121, relheight=0.05)
    btn_add.configure(activebackground=COLOR, bg=COLOR)
    btn_add.configure(text='Добавить точку')
    btn_add.configure(command=lambda: pnt.add_point(points, entries))

    btn_delete = tk.Button(window)
    btn_delete.place(relx=0.849, rely=0.53, relwidth=0.121, relheight=0.05)
    btn_delete.configure(activebackground=COLOR, bg=COLOR)
    btn_delete.configure(text='Удалить точку')
    btn_delete.configure(command=lambda: pnt.del_point(points))

    btn_clean = tk.Button(window)
    btn_clean.place(relx=0.725, rely=0.615, relwidth=0.250, relheight=0.05)
    btn_clean.configure(activebackground=COLOR, bg=COLOR)
    btn_clean.configure(text='Очистить вcе поля')
    btn_clean.configure(command=lambda: pnt.all_del_point(points, canvas))

    btn_solve = tk.Button(window)
    btn_solve.place(relx=0.725, rely=0.785, relwidth=0.250, relheight=0.05)
    btn_solve.configure(activebackground=COLOR, bg=COLOR)
    btn_solve.configure(text='Вывести результаты')
    btn_solve.configure(command=lambda: task.call_solve(points, canvas))

    btn_problem = tk.Button(window)
    btn_problem.place(relx=0.725, rely=0.87, relwidth=0.250, relheight=0.05)
    btn_problem.configure(activebackground=COLOR, bg=COLOR)
    btn_problem.configure(text='Условие задачи')
    btn_problem.configure(command=msg.info)

    btn_edit = tk.Button(window)
    btn_apply = tk.Button(window)

    btns = [btn_add, btn_delete, btn_edit, btn_clean, btn_solve]

    btn_edit.place(relx=0.725, rely=0.7, relwidth=0.121, relheight=0.05)
    btn_edit.configure(activebackground=COLOR, bg=COLOR)
    btn_edit.configure(text='Редактировать точку')
    btn_edit.configure(command=lambda: pnt.edit_point(points, entries,  btns, btn_apply))

    btn_apply.place(relx=0.849, rely=0.7, relwidth=0.121, relheight=0.05)
    btn_apply.configure(activebackground=COLOR, bg=COLOR)
    btn_apply.configure(text='Применить\nредактирование')
    btn_apply.configure(state=tk.DISABLED)
    btn_apply.configure(command=lambda: pnt.apply(points, entries,  btns, btn_apply))

# Создание полей ввода для координат точек
def create_entry(window):
    ent_x = tk.Entry(window)
    ent_x.place(relx=0.760, rely=0.41, relwidth=0.215, relheight=0.036)
    ent_x.configure(background="white")
    ent_x.configure(font="TkFixedFont")
    ent_x.configure(selectbackground="blue")
    ent_x.configure(selectforeground="white")

    ent_y = tk.Entry(window)
    ent_y.place(relx=0.760, rely=0.46, relwidth=0.215, relheight=0.036)
    ent_y.configure(background="white")
    ent_y.configure(font="TkFixedFont")
    ent_y.configure(selectbackground="blue")
    ent_y.configure(selectforeground="white")

    return [ent_x, ent_y]

# Функция обновления размеров холста при изменении размеров окна
def on_resize(event, sizes, canvas):
    wscale = float(event.width) / sizes[0]
    hscale = float(event.height) / sizes[1]

    sizes[0] = event.width
    sizes[1] = event.height

    canvas.configure(width=sizes[0], height=sizes[1])
    canvas.scale("all", 0, 0, wscale, hscale)

# Создание холста для отображения графических результатов
def create_canvas(window):
    cnv_solution = tk.Canvas(window)
    cnv_solution.place(relx=0.0, y=0.2, relheight=1.0, relwidth=0.7)
    cnv_solution.configure(background="#F0FFFF")
    cnv_solution.configure(borderwidth="2")
    cnv_solution.configure(highlightbackground="#708090")
    cnv_solution.configure(insertbackground="#708090")
    cnv_solution.configure(relief="raised")
    cnv_solution.configure(selectbackground="#708090")
    cnv_solution.configure(selectforeground="#708090")
    cnv_solution.addtag_all("all")

    cnv_sizes = [cnv_solution.winfo_reqwidth(), cnv_solution.winfo_reqheight()]
    cnv_solution.bind("<Configure>", lambda event: on_resize(event, cnv_sizes, cnv_solution))
    return cnv_solution

# Создание окна
def create_window():
    window = tk.Tk()
    window.title('Лабораторная работа №1')
    window.geometry('1000x500+100+100')
    window.minsize(939, 676)
    window.configure(background="#708090")
    create_menu(window)
    create_lables(window)
    points = create_table(window)
    entries = create_entry(window)
    canvas = create_canvas(window)
    create_buttons(window, points, entries, canvas)
    window.mainloop()

if __name__ == '__main__':
    create_window()