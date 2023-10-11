# Выполнил Жижин Никита. ИУ7-11Б
# Задача: написать программу для вычисления суммы ряда
# с точностью до члена ряда eps.

# Блок ввода
x, accuracy = map(
    float, input(">>> Введите аргумент х и точность eps через пробел: ").split()
)
step, iter_cnt = map(
    int,
    input(
        ">>> Введите шаг печати и максимальное количество итераций через пробел: "
    ).split()
)

# Блок вычислений
print(" " + "-" * 37)
print(f"|{'№ итерации':^15}|{'t':^10}|{'s':^10}|")
print(" " + "-" * 37)

i = 0
res = x
is_done = False
while True:
    cur = 1 / ((2 * i + 1) * x ** (2 * i + 1))
    res += cur
    i += 1
    if (i - 1) % step == 0:
        print(f"|{i:<15}|{cur:^10.5g}|{res:^10.5g}|")
    if cur <= accuracy:
        is_done = True
        break
    if i >= iter_cnt:
        break
print(" " + "-" * 37)

# Блок вывода
if not is_done:
    print(f"За {iter_cnt} итераций достичь необходимой точности не удалось!")
else:
    print(f"Сумма бесконечного ряда - {res:.5g}, вычислена за {i} итераций.")