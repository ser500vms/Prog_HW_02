# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8

# num = int(input('Введите число: '))
num = 10
degree = [1]
i = 1
while num > 2 ** i:
    pow = 2 ** i
    degree.append(pow)
    i += 1
print(f'{num} -> {degree}')