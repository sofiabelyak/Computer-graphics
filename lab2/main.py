import seaborn as sns
import tkinter as tk
import tkinter.messagebox as box
import messages as msg
import copy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import home
import update

matplotlib.use('TkAgg')

AUTHOR_TITLE = 'Об авторе'
AUTHOR = 'Беляк Софья\nИУ7-42Б'


class RootWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("950x600+100+40")
        self.root.resizable(False, False)
        self.root.title("ЛР2")
        self.root.configure(bg="#F0FFFF")

    def crt_menu(self):
        self.menu = tk.Menu(self.root, font="TkMenuFont")
        self.menu.add_command(label=AUTHOR_TITLE, command=lambda: box.showinfo(AUTHOR_TITLE, AUTHOR))
        self.menu.add_command(label='Выход', command=self.root.destroy)
        self.root.configure(menu=self.menu)

    def crtwdg_figure_centre(self):
        self.lblfrm_figure_centre = tk.LabelFrame(self.root, bg="#E6E6FA")
        self.lblfrm_figure_centre.place(relx=0.72, rely=0.013, relheight=0.085, relwidth=0.25)
        self.lblfrm_figure_centre.configure(relief='ridge', font=('Arial', 12, 'bold'), text="Центр")
        self.lbl_figure_centre = tk.Label(self.lblfrm_figure_centre, bg="#E6E6FA")
        self.lbl_figure_centre.place(relx=0.007, rely=0.370, relheight=0.5, relwidth=0.98)
        self.lbl_figure_centre.configure(font=update.FONT_CONFIG,
                                         text="X:{:5.2f}; Y:{:5.2f}".format(self.funcs[9].x_list[0],
                                                                            self.funcs[9].y_list[0]))

    def crtwdg_transfer(self):
        self.lblfrm_transfer = tk.LabelFrame(self.root, bg="#E6E6FA")
        self.lblfrm_transfer.place(relx=0.72, rely=0.280, relheight=0.147, relwidth=0.25)
        self.lblfrm_transfer.configure(relief='ridge', font=('Arial', 12, 'bold'), text='Перемещение')
        self.lbl_dx = tk.Label(self.lblfrm_transfer, bg="#E6E6FA")
        self.lbl_dx.place(relx=0.007, rely=0.29, relheight=0.25, relwidth=0.2, bordermode='ignore')
        self.lbl_dx.configure(font=('Arial', 12), text="Dx:")
        self.ent_dx = tk.Entry(self.lblfrm_transfer)
        self.ent_dx.place(relx=0.16,
                          rely=0.29,
                          relheight=0.25,
                          relwidth=0.4,
                          bordermode='ignore'
                          )
        self.ent_dx.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
        )
        self.ent_dx.insert(0, "0.0")

        self.lbl_dy = tk.Label(self.lblfrm_transfer, bg="#E6E6FA")
        self.lbl_dy.place(
            relx=0.44,
            rely=0.29,
            relheight=0.25,
            relwidth=0.2,
            bordermode='ignore'
        )
        self.lbl_dy.configure(
            font=('Arial', 12),
            text="Dy:"
        )

        self.ent_dy = tk.Entry(self.lblfrm_transfer)
        self.ent_dy.place(
            relx=0.6,
            rely=0.29,
            relheight=0.25,
            relwidth=0.3,
            bordermode='ignore'
        )
        self.ent_dy.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
        )
        self.ent_dy.insert(0, "0.0")  # Установка значения по умолчанию "0.0"

        self.btn_transfer = tk.Button(self.lblfrm_transfer, bg="#F0FFFF")
        self.btn_transfer.place(
            relx=0.2,
            rely=0.65,
            relheight=0.25,
            relwidth=0.6,
            bordermode='ignore'
        )
        self.btn_transfer.configure(
            activebackground="#F0FFFF",
            text="Переместить",
            command=lambda: update.move(self, HOME, FISHES)
        )

    def mark_center(self, xc, yc):
        xc_pixel, yc_pixel = self.map_coordinates_to_pixels(xc, yc)
        self.subplt.plot(xc_pixel, yc_pixel, marker='o', markersize=8, color='pink', label='Center')
        self.pltcnv.draw()

    def map_coordinates_to_pixels(self, x, y):
        xlim = self.subplt.get_xlim()
        ylim = self.subplt.get_ylim()
        width, height = self.pltcnv.get_tk_widget().winfo_width(), self.pltcnv.get_tk_widget().winfo_height()

        x_pixel = (x - xlim[0]) / (xlim[1] - xlim[0]) * width
        y_pixel = height - (y - ylim[0]) / (ylim[1] - ylim[0]) * height

        return x_pixel, y_pixel

    def crtwdg_trans_centre(self):
        self.lblfrm_centre = tk.LabelFrame(self.root, bg="#E6E6FA")
        self.lblfrm_centre.place(
            relx=0.72,
            rely=0.110,
            relheight=0.157,
            relwidth=0.25
        )
        self.lblfrm_centre.configure(
            relief='ridge',
            font=('Arial', 11, 'bold'),
            text="Центр для масштаба,поворота"
        )

        self.lbl_xc = tk.Label(self.lblfrm_centre, bg="#E6E6FA")
        self.lbl_xc.place(
            relx=0.017,
            rely=0.259,
            relheight=0.3,
            relwidth=0.15,
            bordermode='ignore'
        )
        self.lbl_xc.configure(
            font=('Arial', 12),
            text="X:"
        )

        self.lbl_yc = tk.Label(self.lblfrm_centre, bg="#E6E6FA")
        self.lbl_yc.place(
            relx=0.02,
            rely=0.612,
            relheight=0.3,
            relwidth=0.15,
            bordermode='ignore'
        )
        self.lbl_yc.configure(
            activebackground="#f9f9f9",
            font=('DejaVu Sans', 12),
            text="Y:"
        )

        self.ent_xc = tk.Entry(self.lblfrm_centre)
        self.ent_xc.place(
            relx=0.208,
            rely=0.284,
            relheight=0.25,
            relwidth=0.75,
            bordermode='ignore'
        )
        self.ent_xc.configure(
            background="white",
            font="TkFixedFont"
        )

        self.ent_yc = tk.Entry(self.lblfrm_centre)
        self.ent_yc.place(
            relx=0.208,
            rely=0.638,
            relheight=0.25,
            relwidth=0.75,
            bordermode='ignore'
        )
        self.ent_yc.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
        )

    def crtwdg_scaling(self):
        self.lblfrm_scaling = tk.LabelFrame(self.root, bg="#E6E6FA")
        self.lblfrm_scaling.place(
            relx=0.72,
            rely=0.44,
            relheight=0.157,
            relwidth=0.25
        )
        self.lblfrm_scaling.configure(
            relief='groove',
            font=('Arial', 12, 'bold'),
            text="Масштабирование"
        )

        self.lbl_kx = tk.Label(self.lblfrm_scaling, bg="#E6E6FA")
        self.lbl_kx.place(
            relx=0.007,
            rely=0.29,
            relheight=0.25,
            width=53,
            bordermode='ignore'
        )
        self.lbl_kx.configure(
            activebackground="#f9f9f9",
            font=('Arial', 12),
            text="Kx:"
        )

        self.lbl_ky = tk.Label(self.lblfrm_scaling, bg="#E6E6FA")
        self.lbl_ky.place(
            relx=0.507,
            rely=0.29,
            relheight=0.25,
            width=53,
            bordermode='ignore'
        )
        self.lbl_ky.configure(
            activebackground="#f9f9f9",
            font=('Arial', 12),
            text="Ky:"
        )

        self.ent_kx = tk.Entry(self.lblfrm_scaling)
        self.ent_kx.place(
            relx=0.164,
            rely=0.27,
            relheight=0.25,
            relwidth=0.3,
            bordermode='ignore'
        )
        self.ent_kx.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
        )
        self.ent_kx.insert(0, "1.0")

        self.ent_ky = tk.Entry(self.lblfrm_scaling)
        self.ent_ky.place(
            relx=0.664,
            rely=0.27,
            relheight=0.25,
            relwidth=0.3,
            bordermode='ignore'
        )
        self.ent_ky.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
        )
        self.ent_ky.insert(0, "1.0")

        self.btn_scaling = tk.Button(self.lblfrm_scaling, bg="#F0FFFF")
        self.btn_scaling.place(
            relx=0.025,
            rely=0.6,
            relheight=0.3,
            relwidth=0.945,
            bordermode='ignore'
        )
        self.btn_scaling.configure(
            activebackground="#F0FFFF",
            text="Масштабировать",
            command=lambda: update.scale(self, HOME, FISHES)
        )

    def crtwdg_rotate(self):
        self.lblfrm_rotate = tk.LabelFrame(self.root, bg="#E6E6FA")
        self.lblfrm_rotate.place(
            relx=0.72,
            rely=0.600,
            relheight=0.157,
            relwidth=0.25
        )
        self.lblfrm_rotate.configure(
            relief='groove',
            font=('Arial', 12, 'bold'),
            text="Поворот"
        )

        self.lbl_angle = tk.Label(self.lblfrm_rotate, bg="#E6E6FA")
        self.lbl_angle.place(
            relx=0.025,
            rely=0.29,
            bordermode='ignore'
        )
        self.lbl_angle.configure(
            activebackground="#f9f9f9",
            font=('Arial', 12),
            justify=tk.CENTER,
            text="Угол°:"
        )

        self.ent_angle = tk.Entry(self.lblfrm_rotate)
        self.ent_angle.place(
            relx=0.20,
            rely=0.25,
            relheight=0.25,
            relwidth=0.65,
            bordermode='ignore'
        )
        self.ent_angle.configure(
            background="white",
            font="TkFixedFont",
            selectbackground="blue",
            selectforeground="white"
        )

        self.btn_rotate = tk.Button(self.lblfrm_rotate, bg="#F0FFFF")
        self.btn_rotate.place(
            relx=0.025,
            rely=0.582,
            relheight=0.32,
            relwidth=0.95,
            bordermode='ignore'
        )
        self.btn_rotate.configure(
            activebackground="#F0FFFF",
            text="Повернуть",
            command=lambda: update.rotate(self, HOME, FISHES)
        )

    def crtwdg_edit(self):
        self.btn_undo = tk.Button(self.root, bg="#E6E6FA")
        self.btn_undo.place(
            relx=0.716,
            rely=0.88,
            relheight=0.075,
            relwidth=0.12
        )
        self.btn_undo.configure(
            text="Шаг назад",
            state=tk.DISABLED,
            font=('Arial', 12, 'bold'),
            command=lambda: update.undo(ROOT, HOME, FISHES)
        )

        self.btn_redo = tk.Button(self.root, bg="#E6E6FA")
        self.btn_redo.place(
            relx=0.847,
            rely=0.88,
            relheight=0.075,
            relwidth=0.12
        )
        self.btn_redo.configure(
            activebackground="#F0FFFF",
            text="Шаг вперед",
            font=('Arial', 12, 'bold'),
            state=tk.DISABLED,
            command=lambda: update.redo(ROOT, HOME, FISHES)
        )

        self.btn_original = tk.Button(self.root, bg="#E6E6FA")
        self.btn_original.place(
            relx=0.716,
            rely=0.77,
            relheight=0.09,
            relwidth=0.251
        )
        self.btn_original.configure(
            text="Исходное изображение",
            font=('Arial', 12, 'bold'),
            command=lambda: update.reset(ROOT, HOME, FISHES)
        )

    def create_matplotlib(self):
        sns.set(style="dark")
        margins = {"left": 0.05,
                   "bottom": 0.05,
                   "right": 0.98,
                   "top": 0.98
                   }
        self.figure = plt.Figure(figsize=(8.5, 7.5))
        self.figure.subplots_adjust(**margins)
        self.figure.clear()
        self.subplt = self.figure.add_subplot(111)
        for func in self.funcs:
            self.subplt.plot(func.x_list, func.y_list, color='k', linewidth=2)
        self.subplt.set_xlim((-80, 80))
        self.subplt.set_ylim((-80, 80))
        self.subplt.set_aspect('equal')
        self.subplt.grid(True)
        self.pltcnv = FigureCanvasTkAgg(self.figure, self.root)
        self.pltcnv.get_tk_widget().place(
            relx=0.02,
            rely=0.02,
            relheight=0.96,
            relwidth=0.68
        )
        xc = self.funcs[9].x_list[0]
        yc = self.funcs[9].y_list[0]
        try:
            xc_scaling = float(self.ent_xc.get())
            yc_scaling = float(self.ent_yc.get())
            self.subplt.scatter(xc_scaling, yc_scaling, color='blue', marker='o', s=50,
                                label='Точка для масштабирования и поворота')
            self.subplt.text(xc_scaling, yc_scaling, f"[{xc_scaling:.2f}, {yc_scaling:.2f}]", color='black', fontsize=8)

        except ValueError:
            pass
        self.subplt.scatter(xc, yc, color='#8A2BE2', marker='o', s=50, label='Центральная точка')
        for i in range(len(self.funcs[9].x_list)):
            self.subplt.text(self.funcs[9].x_list[i], self.funcs[9].y_list[i],
                             f"[{self.funcs[9].x_list[i]:.2f}, {self.funcs[9].y_list[i]:.2f}]", color='black',
                             fontsize=8)

        self.subplt.legend()
        plt.show()

    def create_widgets(self):
        self.crt_menu()
        self.crtwdg_figure_centre()
        self.crtwdg_transfer()
        self.crtwdg_trans_centre()
        self.crtwdg_scaling()
        self.crtwdg_rotate()
        self.crtwdg_edit()
        self.create_matplotlib()

    def run(self):
        self.create_widgets()
        self.root.mainloop()


if __name__ == "__main__":
    ROOT = RootWindow()
    HOME = home.Home()
    ROOT.funcs = HOME.full
    FISHES = update.History(0, [copy.deepcopy(HOME)])
    ROOT.run()
