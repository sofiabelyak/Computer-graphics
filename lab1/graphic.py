from math import atan2
import task

BLACK = "#000000"
GREEN = "#32CD32"
RED = "#6495ED"
BLUE = "#6A5ACD"
# Функция для сортировки точек четырехугольника по часовой стрелке
def sort_points_clockwise(points):
    # Найдем центр масс
    cx = sum(x for x, y in points) / len(points)
    cy = sum(y for x, y in points) / len(points)

    # Вычислим углы и отсортируем точки
    points = sorted(points, key=lambda p: atan2(p[1] - cy, p[0] - cx))
    return points
# Функция для создания четырехугольника на холсте
def create_quadrilateral(canvas, points):
    """
    Создание четырехугольника на холсте
    """
    points = sort_points_clockwise(points)
    scaled_points = full_scale(canvas, points)

    # Рисование четырехугольника
    canvas.create_polygon(scaled_points, outline='black', fill='light gray', width=2)
    # Находим минимальную и максимальную площади и соответствующие треугольники
    min_area, max_area, min_triangle_points, max_triangle_points = task.find_min_max(scaled_points)

    # Рисование минимального треугольника
    canvas.create_polygon(min_triangle_points, fill='#6495ED', width=2)

    # Рисование максимального треугольника
    canvas.create_polygon(max_triangle_points, fill='#6A5ACD', width=2)

    # Рисование диагоналей
    canvas.create_line(scaled_points[0][0], scaled_points[0][1], scaled_points[2][0], scaled_points[2][1],
                       fill="#000080", width=4)
    canvas.create_line(scaled_points[1][0], scaled_points[1][1], scaled_points[3][0], scaled_points[3][1],
                       fill="#FF00FF", width=4)

    # Найти и нарисовать точку пересечения диагоналей
    intersection_point = task.find_intersection(scaled_points[0], scaled_points[2], scaled_points[1], scaled_points[3])
    canvas.create_oval(intersection_point[0] - 5, intersection_point[1] - 5, intersection_point[0] + 5,
                       intersection_point[1] + 5, fill='#40E0D0')
    intersection_point_text = task.find_intersection(points[0], points[2], points[1], points[3])
    canvas.create_text(intersection_point[0], intersection_point[1] - 5, text=f"[{intersection_point_text[0]:.2f}, {intersection_point_text[1]:.2f}]", font=("Arial", 12),
                           fill="black")

# Функция для масштабирования координат точек для вывода изображения в максимально возможном масштабе
def full_scale(canvas, points):
    if not points:
        return []
    # Находим максимальные и минимальные значения по осям x и y
    max_x = max(point[0] for point in points)
    min_x = min(point[0] for point in points)
    max_y = max(point[1] for point in points)
    min_y = min(point[1] for point in points)

    # Получаем размеры холста
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()

    # Обработка случая, когда все точки имеют одинаковые координаты по одной из осей
    if max_x == min_x:
        max_x += 1
    if max_y == min_y:
        max_y += 1

    # Вычисляем коэффициенты масштабирования для осей x и y
    x_coef = (width - width / 5) / (max_x - min_x)
    y_coef = (height - height / 5) / (max_y - min_y)

    # Масштабирование координат точек
    scaled_points = [
        [(point[0] - min_x) * x_coef + width / 10, height - ((point[1] - min_y) * y_coef + height / 10)]
        for point in points
    ]

    return scaled_points

# Функция для вывода информации о точках на холсте
def print_point_info(canvas, nums, points):
    # Масштабирование координат точек
    scaled_points = full_scale(canvas, points)
    # Вывод информации о каждой точке
    for i, point in enumerate(scaled_points):
        x, y = points[i]
        canvas.create_text(point[0], point[1], text=f"{nums[i] + 1}\n[{x:.2f}, {y:.2f}]", font=("Arial", 12), fill="black")

# Функция для создания точек на холсте
def create_point(canvas, points):
    size = 5
    # Создание овалов для каждой точки
    for point in points:
        x, y = point[0], point[1]
        canvas.create_oval(x - size, y - size, x + size, y + size, fill='#40E0D0')








