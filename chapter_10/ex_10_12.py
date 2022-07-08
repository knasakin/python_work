# 10.12. Сохраненное любимое число
from json import dump, load


filename = 'favorite_number.txt'


def get_stored_number():  # выгружает число из файла и возвращает его если оно есть
    try:
        with open(filename) as f:
            favorite_number = load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def get_favorite_number():  # запрашивает число и загружает его в файл
    while True:
        try:
            favorite_number = int(input('введите любимое число: '))
        except ValueError:
            print('введите число')
        else:
            with open(filename, 'w') as file:
                dump(favorite_number, file)
            break

    return favorite_number


def load_favorite_number():
    favorite_number = get_stored_number()
    if favorite_number:
        with open(filename) as file:
            favorite_number = load(file)
            print(f'Выгружено число {favorite_number}')
    else:
        favorite_number = get_favorite_number()
        with open(filename, 'w') as f:
            dump(favorite_number, f)
        print(f'Выгружено число {favorite_number}')


load_favorite_number()
