# -*- coding: utf-8 -*-
from math import log, floor


def esPotenciaDeDos(numero):
    if numero < 1:
        return False
    i = log(numero, 2)
    return 0 == (i - floor(i))


def main():
    numero = int(input('Ingrese un número: '))
    if esPotenciaDeDos(numero):
        print('El número ingresado ' + str(numero) + ' es potencia de 2')
    else:
        print('El número ingresado ' + str(numero) + ' no es potencia de 2')


main()
