# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Диапазон от 6 до 12

# Вывод: [1, 9, 13, 14, 19]

from random import randint

print('Введите количество чисел')
n = input()
n = int(n)

collection = []
for i in range(n):
    collection.append(randint(1, 10))
print(collection)

print('Введите нижний предел')
a = input()
a = int(a)

print('Введите количество чисел')
b = input()
b = int(b)

numCollection = []
for i in range(len(collection)):
    if collection[i]>=a and collection[i]<=b:
        numCollection.append(i)
print(numCollection)