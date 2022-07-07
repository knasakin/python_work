# 10.1. Изучение Python
filename = 'learning_python.txt'

# чтение всего файла
with open(filename) as file:
    content = file.read()

print(content)
print()

# считывание построчно
with open(filename) as file:
    for line in file:
        print(line.strip())
    print()

# сохранение строк в списке
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
