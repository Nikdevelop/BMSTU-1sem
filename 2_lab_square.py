# Автор: Жижин Никита. ИУ7-11Б
# Нахождение корней квадратного уравнения по заданным коэффициентам

# Блок ввода
a, b, c = map(
    float,
    input("Введите коэффициенты a, b, c через пробел: ").split(),
)

# Блок вычислений
equation = f"{a:.6g}x^2{b:+.6g}x{c:+.6g}=0"  # Уравнение

if a == 0:
    # Решение линейного уравнения
    if b == 0:
        if c == 0:
            print(f"У уравнения {equation} бесконечно много корней")
        else:
            print(f"У уравнения {equation} нет решений")
    else:
        x = -c / b  # Единственный корень
        print(f"Одно решение уравнения {equation}: {x=:.6g}")
else:
    # Решение квадратного уравнения
    d = b**2 - 4 * a * c  # Дискриминант
    if d > 0:
        x1, x2 = (-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)  # Два корня
        print(f"Два решения уравнения {equation}: {x1=:.6g}; {x2=:.6g}")
    elif d < 0:
        print(f"У уравнения {equation} нет решений")
    else:
        x = -b / (2 * a)  # Единственный корень
        print(f"Одно решение уравнения {equation}: {x=:.6g}")
