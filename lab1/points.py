import tkinter as tk
import message as msg

# Функция добавления точки в список.
# В случае неудачи проверяет на пустой ввод и выводит соответствующие сообщения об ошибке.
# В случае успешного получения значений добавляет точку в список.
def add_point(points, entries):
    try:
        x = float(entries[0].get())
        y = float(entries[1].get())
    except ValueError:
        if not entries[0].get() or not entries[1].get():
            msg.create_infobox('Пустой ввод координаты', 'Пустой ввод, введите корректное значение.')
        else:
            msg.create_infobox('Некорректные данные', 'Некорректные данные. Введите числовые значения.')
    except Exception:
        msg.create_infobox('Неизвестная ошибка', 'Неизвестная ошибка.')
    else:
        cur_index = len(points.get_children('')) + 1
        points.insert('', index='end', text=cur_index,
                      values=("{:.2f}".format(x), "{:.2f}".format(y)))

# Функция обновления индексов точек в списке.
# Перебирает все точки в списке и назначает им индексы, начиная с 1.
def index_update(points):
    for i, point in enumerate(points.get_children()):
        points.item(point, text=i + 1)

# Функция удаления выбранной точки из списка.
# Если точка не выбрана или происходит другая ошибка, выводит соответствующее сообщение.
def del_point(points):
    try:
        points.delete(points.selection()[0])
        index_update(points)
    except IndexError:
        if not points:
            msg.create_infobox('Отсутствие точек', 'Нет точек для удаления.')
        else:
            msg.create_infobox('Некорректные данные', 'Не выбрана точка. Выберите необходимую точку.')
    except Exception:
        msg.create_infobox('Неизвестная ошибка', 'Неизвестная ошибка.')

# Функция удаления всех точек из списка.
# Если точек нет или происходит ошибка, выводит соответствующее сообщение.
def all_del_point(points, canvas):
    try:
        points.delete(*points.get_children())
        canvas.delete('all')
    except IndexError:
        msg.create_infobox('Отсутствие точек', 'Нет точек для удаления. Выберите необходимую точку.')
    except Exception:
         msg.create_infobox('Неизвестная ошибка', 'Неизвестная ошибка.')

# Функция редактирования выбранной точки.
def edit_point(points, entries, buttons, btn_app):
    try:
        selected_item = points.selection()[0]
        point = points.item(selected_item)["values"]
        for i in range(2):
            entries[i].delete(0, 'end')
            entries[i].insert(0, point[i])
        for button in buttons:
            button.configure(state=tk.DISABLED)
        btn_app.configure(state=tk.NORMAL)
        points.configure(selectmode='none')
    except IndexError:
        msg.create_infobox('Отсутствие точек', 'Не выбрана точка. Выберите необходимую точку.')
    except Exception:
        msg.create_infobox('Неизвестная ошибка', 'Неизвестная ошибка.')

# Функция применения изменений в редактировании точки. Пытается применить изменения координат выбранной точки.
# Если ввод пуст или некорректен, выводит соответствующее сообщение об ошибке.
# Если точка не выбрана или происходит ошибка, также выводит сообщение.
def apply(points, entries, buttons, btn_app):
    try:
        x, y = map(float, (entries[0].get(), entries[1].get()))
        selected_point = points.selection()[0]
        points.item(selected_point, values=("{:.2f}".format(x), "{:.2f}".format(y)))
        for entry in entries:
            entry.delete(0, 'end')
        for button in buttons:
            button.configure(state=tk.NORMAL)
        btn_app.configure(state=tk.DISABLED)
        points.configure(selectmode='browse')
    except ValueError:
        msg.create_infobox('Пустой ввод', 'Пустой ввод, введите корректное значение.' if not entries[0].get() or not entries[1].get() else 'Некорректные данные. Введите числовые значения.')
    except IndexError:
        msg.create_infobox('Отсутствие точек', 'Не выбрана точка. Выберите необходимую точку.')
    except Exception:
        msg.create_infobox('Неизвестная ошибка','Неизвестная ошибка.')