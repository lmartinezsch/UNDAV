# -*- coding: utf-8 -*-

def main():
    suma = 0
    while True:
        number = int(input('Ingrese un número: '))
        if (number == 0):
            suma = suma + 10
            break
        elif (number > 0):
            suma = suma + number**3
        elif (number < 0):
            suma = suma + number**2

    return suma

result = main()
print(result)