# 10.7. Калькулятор

while True:
    try:
        a = int(input("введите первое число: "))
        b = int(input("введите второе число: "))
    except ValueError:
        print("нужно ввести число")
    else:
        print(a+b)
        break
