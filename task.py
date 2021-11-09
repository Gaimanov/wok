# функция, которая принимает числа, удаляет из него числа, которые меньше 10, умножает на 2 числа, которые больше 10
def calculate(x, y):
    for i in range(x, y):
        if i <= 10:
            return i - 5
    for i in range(x, y):
        if i > 10:
            return i * 2




