# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
N = int(input('Введите длинну массива: '))
min = 1
max = 1
t = []
for i in range(N):
     t.append(random.randint(0,10))
print(t)
X = int(input('Задайте число Х: '))
for i in range(N):
    if t[i] > max: max = t[i]
for i in range(N):
    if t[i] < X and t[i] >= min: min = t[i]
    if t[i] > X and t[i] <= max: max = t[i]
if min == max:
    print(max)
elif max == X: print(f'Ближайшее число {min}')
elif min == X: print(f'Ближайшее число {max}')
else: print(f'Ближайшие числа {min} и {max}.')
