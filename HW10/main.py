import random
import pandas as pd

# Вариант с без get_dummies:


def one_hot(list, key):
    lst = []
    for value in list:
        if value == key:
            lst.append(1)
        else:
            lst.append(0)
    return lst


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

d = {'robot': one_hot(lst, 'robot'), 'human': one_hot(lst, 'human')}

data = pd.DataFrame(data=d)
data.head()

print(data)

# Вариант с get_dummies:

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})

# d = pd.get_dummies(data['whoAmI'], dtype=int)

# print(d)
