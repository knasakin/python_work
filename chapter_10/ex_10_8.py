# 10.8. Кошки и собаки

filenames = ['cats.txt', 'dogs.txt']


def read_file(filename):
    try:
        with open(filename) as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f'Файл {filename} не найден')


for f in filenames:
    read_file(f)
