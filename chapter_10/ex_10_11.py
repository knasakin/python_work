# 10.11. Любимое число
from json import dump


def dump_favorite_number():
    while True:
        try:
            favorite_number = int(input('Введите ваше любимое число: '))
        except ValueError:
            print('Нужно ввести число')
        else:
            filename = 'favorite_number.txt'
            with open(filename, 'w') as file:
                dump(favorite_number, file)
            break


def print_favorite_number():
    while True:
        try:
            favorite_number = int(input('Введите ваше любимое число: '))
        except ValueError:
            print('Нужно ввести число')
        else:
            print(f'Я знаю ваше любимое число! Это {favorite_number}')
            break


dump_favorite_number()
print_favorite_number()
