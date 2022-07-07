# 9.15. Анализ лотереи
from random import sample
from ex_9_14 import values, lucky_ticket


my_ticket = ''.join(sample(values, 5))
counter = 0

while my_ticket != lucky_ticket:
    my_ticket = ''.join(sample(values, 5))
    counter += 1

print(f'Вы вытянули выигрышный билет с {counter} попытки')
