from random import *

random_list = sample(range(1, 21), randint(3, 10))

print(', '.join(map(str, sorted(random_list))))
