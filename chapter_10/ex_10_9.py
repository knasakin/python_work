# 10.9. Ошибки без уведомления

filenames = ['cats.txt', 'dogs.txt']


def read_file(filename):
    try:
        with open(filename) as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        pass


for f in filenames:
    read_file(f)
