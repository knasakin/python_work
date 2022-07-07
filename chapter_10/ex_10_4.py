# 10.4. Гостевая книга
with open('guest_book.txt', 'a') as file:
    while True:
        msg = f'Hello, {input("Введите имя: ")}\n'
        file.write(msg)
        print(msg)
