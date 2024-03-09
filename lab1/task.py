import copy
import message as msg
import graphic
import itertools
EPS = 1e-6
def create_arr(points_table):
    points = []
    for i in points_table.get_children():
        points.append([float(x) for x in points_table.item(i)["values"]])
    return points

# Функция для вычисления площади четырехугольника по его вершинам
def quadrilateral_area(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    x4, y4 = points[3]
    # Вычисляет площадь четырехугольника по формуле Гаусса и возвращает абсолютное значение.
    return abs((x1 - x2) * (y1 + y2) + (x2 - x3) * (y2 + y3) + (x3 - x4) * (y3 + y4) + (x4 - x1) * (y4 + y1)) / 2

# Функция для вычисления площади треугольника по координатам его вершин
def area(x1, y1, x2, y2, x3, y3):
    # Вычисляет площадь треугольника по формуле Герона и возвращает абсолютное значение.
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
def are_points_collinear(points):
    # Проверяем, лежат ли любые три точки на одной прямой
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if abs((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) < EPS:
                    return True  # Любые три точки лежат на одной прямой
    return False
# Функция для проверки выпуклости четырехугольника по его вершинам
def is_convex(points):
    n = len(points)
    # Если точек меньше четырех, то четырехугольник не существует и не является выпуклым
    if n < 4:
        return False
    orientation = 0
    # Проход по каждой вершине четырехугольника
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        x3, y3 = points[(i + 2) % n]
        # Вычисление векторного произведения для определения ориентации вершин
        cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
        # Если векторное произведение равно нулю, вершины коллинеарны, пропускаем
        if cross_product == 0:
            continue
        # Если это первая итерация, устанавливаем ориентацию
        if orientation == 0:
            orientation = 1 if cross_product > 0 else -1
        # Если ориентация меняется, четырехугольник не выпуклый
        elif orientation * cross_product < 0:
            return False
    # Если вершины коллинеарны, четырехугольник не выпуклый
    if are_points_collinear(points):
        return False
    # Если все проверки пройдены, четырехугольник выпуклый
    return True

# Функция для нахождения точки пересечения двух отрезков по их конечным точкам
def find_intersection(point1, point2, point3, point4):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    x4, y4 = point4

    # Формула пересечения двух прямых
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    return x, y


# Функция для нахождения минимальной и максимальной площади четырехугольника,
# а также точек минимального и максимального треугольников после разбиения четырехугольника на четыре треугольника
def find_min_max(points):
    n = len(points)
    # Инициализация переменных для минимальной и максимальной площади
    min_area = float('inf')
    max_area = float('-inf')
    # Инициализация переменных для точек минимального и максимального треугольников
    min_triangle_points = []
    max_triangle_points = []
    # Находим точку пересечения диагоналей четырехугольника
    intersection_point = find_intersection(points[0], points[2], points[1], points[3])

    # Разбиваем четырехугольник на четыре треугольника
    for i in range(n):
        # Формируем треугольник с вершинами текущей вершиной четырехугольника и точкой пересечения диагоналей
        triangle_points = [points[i], points[(i + 1) % n], intersection_point]
        # Вычисляем площадь треугольника
        triangle_area_value = area(triangle_points[0][0], triangle_points[0][1],
                                   triangle_points[1][0], triangle_points[1][1],
                                   triangle_points[2][0], triangle_points[2][1])
        # Обновляем минимальную площадь и соответствующие точки
        if triangle_area_value < min_area:
            min_area = triangle_area_value
            min_triangle_points = triangle_points
        # Обновляем максимальную площадь и соответствующие точки
        if triangle_area_value > max_area:
            max_area = triangle_area_value
            max_triangle_points = triangle_points

    # Возвращаем минимальную и максимальную площадь, а также точки минимального и максимального треугольников
    return min_area, max_area, min_triangle_points, max_triangle_points

# Функция для вычисления разности между максимальной и минимальной площадью треугольников, образованных диагоналями четырехугольника
def find_diff(points):
    # Вычисление минимальной и максимальной площади треугольников
    min_area, max_area, min_triangle_points, max_triangle_points = find_min_max(points)
    # Возвращение разности между максимальной и минимальной площадью
    return max_area - min_area

# Функция для решения задачи на нахождение четырехугольника с минимальной разностью площадей треугольников, образованных диагоналями
def solve(points):
    unique_points = list(set(map(tuple, points)))  # Преобразуем в множество, чтобы убрать дубликаты
    length = len(unique_points)
    # Инициализация переменных для ответа
    answer = {'min_diff': float('inf'), 'max_min': (0, 1), 'in_points': [],
              'nums': (), 'quadrilateral': (),
              'quadrilateral_area': 0.0, 'min_triangle_area': 0.0, 'max_triangle_area': 0.0}
    # Перебор всех возможных комбинаций четырех уникальных точек
    for points_combination in itertools.permutations(unique_points, 4):
        # Проверка выпуклости четырехугольника
        if is_convex(points_combination):
            # Вычисление разности площадей треугольников, образованных диагоналями
            cur_diff = find_diff(points_combination)
            # Вычисление площади четырехугольника
            quadrilateral_area_value = quadrilateral_area(points_combination)
            # Вычисление площадей минимального и максимального треугольников
            min_triangle_area, max_triangle_area, min_triangle_points, max_triangle_points = find_min_max(points_combination)
            # Обновление ответа в случае нахождения четырехугольника с меньшей разностью площадей
            if cur_diff < answer['min_diff'] and quadrilateral_area_value > 0:
                answer['min_diff'] = cur_diff
                answer['nums'] = tuple(range(length))
                answer['quadrilateral'] = points_combination
                answer['max_min'] = (0, 1)
                answer['quadrilateral_area'] = quadrilateral_area_value
                answer['min_triangle_area'], answer['max_triangle_area'] = min_triangle_area, max_triangle_area
    # Возвращение ответа, либо None, если не удалось построить ни одного четырехугольника
    if answer['min_diff'] == float('inf'):
        return None
    return answer

# Функция для проверки корректности количества точек
def is_correct(points_arr):
    # Если количество точек меньше 4, выводим сообщение об ошибке и возвращаем False
    if len(points_arr) < 4:
        msg.create_infobox('Недостаточное количество',' Минимальное количество для построения: 4 точки.')
        return False
    # В противном случае возвращаем True
    return True

# Функция для формирования текста с информацией о минимальном четырехугольнике
def form_optimal_quadrilateral_text(answer):
    # Формирование текста с результатами расчетов
    text = ('Четырехугольник с минимальной разностью,\n'
            + 'равной {:3f}, построен на точках:\n'.format(answer["min_diff"]))
    # Добавление информации о каждой точке четырехугольника
    for i, point in enumerate(answer["quadrilateral"]):
        text += '     %3d[' % (answer["nums"][i] + 1)
        text += '%6.2f, ' % (point[0])
        text += '%6.2f]\n' % (point[1])
    # Добавление информации о площади четырехугольника и треугольников
    text += f'Площадь четырехугольника: {answer["quadrilateral_area"]:.2f}\n'
    text += f'Площадь максимального треугольника: {answer["max_triangle_area"]:.2f}\n'
    text += f'Площадь минимального треугольника: {answer["min_triangle_area"]:.2f}\n'
    # Возвращение сформированного текста
    return text

# Функция для вызова решения и отображения результатов на холсте
def call_solve(points_table, canvas):
    # Создание массива точек из таблицы точек
    points_arr = create_arr(points_table)
    # Проверка наличия достаточного количества точек для построения четырехугольника
    if not is_correct(points_arr):
        # Вывод сообщения об ошибке в случае недостаточного количества точек
        msg.create_infobox('Недостаточное количество', ' Минимальное количество для построения: 4 точки.')
        return

    # Вызов функции решения
    answer = solve(points_arr)

    # Проверка наличия решения и того, что построенный четырехугольник является выпуклым
    if answer is None or not is_convex(answer.get("quadrilateral", [])):
        # Вывод сообщения об ошибке в случае невозможности построить выпуклый четырехугольник
        msg.create_infobox('Ошибка', 'На заданных точках невозможно построить выпуклый четырехугольник!')
        return
    else:
        # Очистка холста
        canvas.delete('all')
        # Вывод информационного окна с результатами
        msg.create_infobox('Решение', form_optimal_quadrilateral_text(answer))
        # Создание копии четырехугольника
        quadrilateral_copy = copy.deepcopy(answer["quadrilateral"])
        # Масштабирование точек четырехугольника и отображение на холсте
        scaled_in_points = graphic.full_scale(canvas, answer["quadrilateral"])
        graphic.create_quadrilateral(canvas, answer["quadrilateral"])
        # Вывод информации о точках на холсте
        graphic.print_point_info(canvas, answer["nums"], quadrilateral_copy)
        # Отображение точек на холсте
        graphic.create_point(canvas, scaled_in_points)



