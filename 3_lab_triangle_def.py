# Выполнил: Жижин Никита, ИУ7-11Б
# Задача: Написать программу, которая по введенным целочисленным
# координатам трех точек на плоскости вычисляет длины сторон
# образованного треугольника и длину высоты, проведенной из
# наибольшего угла.

# Защита: дан отрезок, между первой и второй точкой.
# Необходимо понять пересекает ли он хотя бы одну сторону треугольника
import math

EPS = 1e-4
vertical_k = 1e20

# Блок ввода
p1, p2, p3 = [
    tuple(
        map(
            int, input(f">>> Введите координаты {i + 1} вершины через пробел: ").split()
        )
    )
    for i in range(3)
]

# Блок вычислений
# Стороны в векторном виде
s1 = (p2[0] - p1[0], p2[1] - p1[1])
s2 = (p1[0] - p3[0], p1[1] - p3[1])
s3 = (p3[0] - p2[0], p3[1] - p2[1])

sides = (s1, s2, s3)
sides_opposite = {s1: (s2, s3), s2: (s1, s3), s3: (s1, s2)}
side_lens = {}

# Вычисление длин сторон треугольника
for i, side in enumerate(sides, 1):
    length = (side[0] ** 2 + side[1] ** 2) ** 0.5
    side_lens[side] = length
    print(f"Длина стороны {i}: {length:.6g}")

# Вычисление углов треугольника
angles = {}
for side in sides:
    op_side1, op_side2 = sides_opposite[side]
    side1_len = side_lens[op_side1]
    side2_len = side_lens[op_side2]
    angle = math.acos(
        (-op_side1[0] * op_side2[0] - op_side1[1] * op_side2[1])
        / (side1_len * side2_len)
    )
    angles[side] = angle

assert abs(sum(angles.values()) - math.pi) < EPS, sum(angles.values())

# Проверка, если треугольник является прямоугольным
is_right = False
for side, angle in angles.items():
    if abs(angle - math.pi / 2) < EPS:
        is_right = True
        break

if is_right:
    print("Треугольник является прямоугольным")
else:
    print("Треугольник не является прямоугольным")

# Вычисление высоты, проведенной из наибольшего угла
max_side, max_angle = max(angles.items(), key=lambda x: x[1])
max_side_opposite = sides_opposite[max_side][0]
max_side_opposite_len = side_lens[max_side_opposite]
max_side_len = side_lens[max_side]
angle = math.acos(
    (-max_side_opposite[0] * max_side[0] - max_side_opposite[1] * max_side[1])
    / (max_side_opposite_len * max_side_len)
)
altitude = max_side_opposite_len * math.sin(angle)
print(f"Длина высоты, опущенной из угла максимальной величины: {altitude:.6g}")

# Находится ли точка внутри треугольника
dx1, dy1 = map(int, input(">>> Введите координаты первой точки через пробел: ").split())
dx2, dy2 = map(int, input(">>> Введите координаты второй точки через пробел: ").split())
line_vec = dx2 - dx1, dy2 - dy1

v1, v2, v3 = (
    (p1[0] - dx1, p1[1] - dy1),
    (p2[0] - dx1, p2[1] - dy1),
    (p3[0] - dx1, p3[1] - dy1),
)  # Векторы от точки до вершин

groups = ((v1, v2, s1), (v2, v3, s3), (v3, v1, s2))
angle_sum = 0
min_dist = math.inf
for vec1, vec2, s_opposite in groups:
    # Вычисление угла между векторами от точки до вершин
    vec1_len = (vec1[0] ** 2 + vec1[1] ** 2) ** 0.5
    vec2_len = (vec2[0] ** 2 + vec2[1] ** 2) ** 0.5
    angle = 0
    if vec1_len > 0 and vec2_len > 0:
        cos = min(max((vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (vec1_len * vec2_len), -1), 1)
        angle = math.acos(cos)
    else:
        angle_sum = 2 * math.pi
        min_dist = 0
        break
    angle_sum += angle

    # Вычисление расстояния от точки до стороны
    s_opposite_len = side_lens[s_opposite]
    ang_side = 0
    if vec1_len > 0 and vec2_len > 0:
        ang_side = math.acos(
            (-vec1[0] * s_opposite[0] - vec1[1] * s_opposite[1])
            / (vec1_len * s_opposite_len)
        )
    dist = vec1_len * math.sin(ang_side)
    if min_dist > dist:
        min_dist = dist

# Сумма углов между получившимися векторами должна быть равна 2*pi или 360 градусам
is_point_inside = False
if abs(angle_sum - 2 * math.pi) < EPS:
    is_point_inside = True

if is_point_inside:
    print(f"Точка с координатами {dx1, dy1} находится внутри заданного треугольника")
    print(f"Расстояние от этой точки до ближайшей стороны: {min_dist:.6g}")
else:
    print(f"Точка с координатами {dx1, dy1} находится вне заданного треугольника")

# Защита лабораторки
# Стороны треугольника как отрезки
side_segments = ((p1, p2), (p1, p3), (p2, p3))

# Определение уравнения прямой для нового отрезка
if dx1 == dx2:
    line_seg_k = vertical_k
else:
    line_seg_k = (dy2 - dy1) / (dx2 - dx1)
line_seg_b = dy1 - line_seg_k * dx1

has_intersect = False

for side in side_segments:
    x1, y1, x2, y2 = *side[0], *side[1]

    # Уравнение прямой для стороны треугольника
    if x2 == x1:
        side_k = vertical_k
    else:
        side_k = (y2 - y1) / (x2 - x1)
    side_b = y1 - side_k * x1
    # Если коэффициенты К равны, то эти прямые параллельны и не пересекутся
    if abs(side_k - line_seg_k) < EPS:
        continue
    
    # Находим абсциссу точки пересечения прямых
    # Если она принадлежит промежуткам [x1, x2] и [dx1, dx2], 
    # то она является точкой пересечения отрезков
    x_intersect = (side_b - line_seg_b) / (line_seg_k - side_k)
    if min(x1, x2) - EPS <= x_intersect <= max(x1, x2) + EPS and \
        min(dx1, dx2) - EPS <= x_intersect <= max(dx1, dx2) + EPS:
        has_intersect = True
        # print(f"Точка пересечения: ({x_intersect:.6g}, {side_k*x_intersect+side_b:.6g})")
        break

if has_intersect:
    print("Заданный отрезок пересекает треугольник")
else:
    print("Заданный отрезок не пересекает треугольник")
