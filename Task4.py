# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

from random import randint

print("Введите номер четверти")
quad = int(input())
if (quad < 1 or quad > 4):
    print("Вы ввели некорректные входные данные")
else:
    if (quad == 1):
        print("X ∈ [0, +∞); Y ∈ [0, +∞). Например, точки: ")
        for i in range(10):
            x = randint(1, 10) * i
            y = randint(1, 10) * i
            print("(",x,";",y,")")
    if (quad == 2):
        print("X ∈ [-∞, 0); Y ∈ [0, +∞). Например, точки: ")
        for i in range(10):
            x = -1 * randint(1, 10) * i
            y = randint(1, 10) * i
            print("(",x,";",y,")")
    if (quad == 3):
        print("X ∈ [-∞, 0); Y ∈ [-∞, 0). Например, точки: ")
        for i in range(10):
            x = -1 * randint(1, 10) * i
            y = -1 * randint(1, 10) * i
            print("(",x,";",y,")")
    if (quad == 4):
        print("X ∈ [0, +∞); Y ∈ [-∞, 0). Например, точки: ")
        for i in range(10):
            x = randint(1, 10) * i
            y = -1 * randint(1, 10) * i
            print("(",x,";",y,")")