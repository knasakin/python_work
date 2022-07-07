# 10.2. Изучение C
filename = 'learning_python.txt'
key_word = 'Python'
new_word = 'C'

with open(filename) as file:
    for line in file:
        while key_word in line:
            line = line.replace(key_word, new_word)
        print(line.strip())
