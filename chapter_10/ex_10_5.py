# 10.5. Опрос
with open('reasons_for_program.txt', 'a') as file:
    while True:
        msg = f'Hello, {input("Почему вам нравится программировать?: ")}\n'
        file.write(msg)
