# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке 
# растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени
# сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
#  заданной во входном файле грядки.

import random

bushes = int(input("Введите колличество кустов: "))
berries_on_bushes = [random.randint(1, 20) for _ in range(bushes)]

print(berries_on_bushes)

sum_collected_berries = 0
robot_position = -1
max_berries = berries_on_bushes[-2] + berries_on_bushes[-1] + berries_on_bushes[0]

for i in range(len(berries_on_bushes) - 1):
    sum_collected_berries = berries_on_bushes[i - 1] + berries_on_bushes[i] + berries_on_bushes[i + 1]
    if max_berries < sum_collected_berries:
        max_berries = sum_collected_berries
        robot_position = i
    if robot_position == -1:
        robot_position = len(berries_on_bushes) - 1

print(f'Максимальное кол-во ягод собранных за один заход = {max_berries}')
print(f'Индекс собирающего модуля для выполнения задачи будет = {robot_position}')