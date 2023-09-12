# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 - > 1 0 1 1 0
# 2

import random

n = 5
coins = []
eagle = 1
count_eagle = 0

for _ in range(n):
    coins.append(random.randint(0, 1))
print(f'{n} -> {coins}')

for i in range(len(coins)):
    if coins[i] == eagle:
        count_eagle += 1

if count_eagle < n - count_eagle:
    print(count_eagle)
else:
    print(n - count_eagle)


