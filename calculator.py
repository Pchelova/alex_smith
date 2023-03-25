print("Добро пожаловать в калькулятор от Екатерины. Калькулятор от Екатерины - легко как дважды два четыре")

con=1
while con == 1:
    print("Введите первое значение: ")
    try:
        a = float(input())
    except ValueError:
        a = 0
        print("Это же калькулятор, можно вводить только числовые значения")
        print("Введите первое значение: ")
        a = float(input())
    print("Введите второе значение: ")
    try:
        b = float(input())
    except ValueError:
        b = 0
        print("Это же калькулятор, можно вводить только числовые значения")
        print("Введите второе значение: ")
        b = float(input())



    print("Выберите операцию, которую хотите произвести над числами:\n 1.сложение\n 2.вычитание\n 3.умножение\n 4.деление")
    try:
        c = int(input())
    except ValueError:
        c = 0
        print("Это же калькулятор, можно вводить только числовые значения")
        print("Выберите операцию, которую хотите произвести над числами:\n 1.сложение\n 2.вычитание\n 3.умножение\n 4.деление")
        c = int(input())

    def plus(a,b):
        result = a + b
        return result

    def minus(a,b):
        result = a - b
        return result

    def multiply(a,b):
        result = a * b
        return result

    def divide(a,b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            return "Деление на ноль невозможно"

    if c == 1:
        print(plus(a,b))
    elif c == 2:
        print(minus(a,b))
    elif c == 3:
        print(multiply(a,b))
    elif c == 4:
        print(divide(a,b))
    else:
        print("Есть только 4 варианта. Выберите один из них")


    con = int(input("Продолжить? 1 - да, 0 - нет \n"))