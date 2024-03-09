from math import sin, cos
import numpy as np
class Func:
    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list
class Home:
    def __init__(self):
        self.roof = self.create_roof()
        self.walls = self.create_walls()
        self.door = self.create_door()
        self.window = self.create_window()
        self.cross_1 = self.create_cross_1()
        self.cross_2 = self.create_cross_2()
        self.diagonal_1 = self.create_diagonal_1()
        self.diagonal_2 = self.create_diagonal_2()
        self.handle = self.create_handle()
        self.full = [self.roof, self.walls, self.door, self.window,self.cross_1, self.cross_2, self.diagonal_1, self.diagonal_2, self.handle]
        self.move(0, 0)
        self.centre = Func([0], [0])
        self.full.append(self.centre)
    def reset(self):
        self.__init__()
    def create_roof(self):
        roof = Func([], [])
        roof.x_list = [-35, 35, 30, -30, -35]
        roof.y_list = [30, 30, 45, 45, 30]
        return roof
    def create_walls(self):
        walls = Func([], [])
        walls.x_list = [-30, 30, 30, -30, -30, -45, 45]
        walls.y_list = [0, 0, 30, 30, 0, 0, 0]
        return walls
    def create_door(self):
        door = Func([], [])
        door.x_list = [-20, -20, -20, -10, -10]
        door.y_list = [0, 0, 20, 20, 0]
        return door
    def create_diagonal_1(self):
        diagonal_1 = Func([], [])
        diagonal_1.x_list = [-20, -10]
        diagonal_1.y_list = [0, 20]
        return diagonal_1
    def create_diagonal_2(self):
        diagonal_2 = Func([], [])
        diagonal_2.x_list = [-20, -10]
        diagonal_2.y_list = [20, 0]
        return diagonal_2
    def create_handle(self):
        handle = Func([], [])
        handle.x_list = [-12, -11, -11, -12, -12]
        handle.y_list = [9, 9, 13, 13, 9]
        return handle
    def create_window(self):
        window = Func([], [])
        num_points = 100
        radius = 5
        center_x, center_y = 10, 15
        angles = np.linspace(0, 2 * np.pi, num_points)
        window.x_list = [center_x + radius * np.cos(angle) for angle in angles]
        window.y_list = [center_y + radius * np.sin(angle) for angle in angles]
        return window
    def create_cross_1(self):
        cross_1 = Func([], [])
        cross_size = 5
        center_x, center_y = 10, 15
        cross_1.x_list.extend([center_x - cross_size, center_x + cross_size])
        cross_1.y_list.extend([center_y, center_y])
        return cross_1
    def create_cross_2(self):
        cross_2 = Func([], [])
        cross_size = 5
        center_x, center_y = 10, 15
        cross_2.x_list.extend([center_x, center_x])
        cross_2.y_list.extend([center_y - cross_size, center_y + cross_size])
        return cross_2

    def move(self, dx, dy):
        for element in self.full:
            element.x_list = [x + dx for x in element.x_list]
            element.y_list = [y + dy for y in element.y_list]
    def scaling(self, kx, ky, xc, yc):
        for element in self.full:
            element.x_list = [x * kx + (1 - kx) * xc for x in element.x_list]
            element.y_list = [y * ky + (1 - ky) * yc for y in element.y_list]
    def rotate(self, phi, xc, yc):
        phi = -phi
        for element in self.full:
            tmp_x = [x for x in element.x_list]
            element.x_list = [xc + (x - xc) * cos(np.radians(phi))
                              + (element.y_list[i] - yc) * sin(np.radians(phi))
                              for i, x in enumerate(element.x_list)]
            element.y_list = [yc - (tmp_x[i] - xc) * sin(np.radians(phi))
                              + (y - yc) * cos(np.radians(phi))
                              for i, y in enumerate(element.y_list)]
