# 9.14. Лотерея
from random import sample


values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E']

lucky_ticket = ''.join(sample(values, 5))


if __name__ == '__main__':
    print(f'Билет {lucky_ticket} является выигрышным')
