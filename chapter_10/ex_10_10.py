# 10.10. Частые слова
filenames = ['salton_sea.txt', 'slave_auction.txt']
key_word = 'the '


def count_key(filename):
    try:
        with open(filename) as file:
            content = file.read()
            print(content.count(key_word))
    except FileNotFoundError:
        print(f'Файл {filename} не найден')


for f in filenames:
    count_key(f)
