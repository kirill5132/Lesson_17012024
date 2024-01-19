import random
numbers = []
for i in range(10):
    numbers.append(random.randint(10000,100000000))
# print('Есть машина bmw f90 за 13610827') if 13610827 in numbers else print('Нету машины bmw f90 за 13610827')

result = None
if 4 in numbers:
    result = 'Есть китайское несчастливое число'
else:
    result = 'Все окей'

python = []
for i in range(10):
    python.append(random.randint(1000, 100000))

