"""
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
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


A = int(check_input("Введите число A"))
B = int(check_input("Введите число B"))

def degree(a, b):
    if (b == 1):
        return a
    else:
        a = a * a
        return degree(a, b - 1)
    
print(degree(A, B))