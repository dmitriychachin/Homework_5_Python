"""
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
"""

def check_input(massege):

    num = input(massege)

    is_correct = False
    while(is_correct == False):
        if (num.isdigit()):
            if(0 < int(num)):
                is_correct = True
            else:
                print('Похоже вы ввели не число\n')
                num = input(massege)
        else:
            print('Упс :(\n Вы ввели не число, а что-то другое\n')
            num = input(massege)
    return num


def summa(a, b):
    if(b == 1):
        a = a + 1
        return a
    else:
        a = a + 1
        b = b - 1
        return summa(a, b)

a = int(check_input("Введите первое число\n"))
b = int(check_input("Введите второе число\n"))

print(summa(a, b))