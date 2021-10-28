# -*- coding: utf-8 -*-

def mediaSumaImpar(numeroA, numeroB):

    numeroMenor = 0
    numeroMayor = 0
    if (numeroA > numeroB):
        numeroMayor = numeroA
        numeroMenor = numeroB
    else:
        numeroMayor = numeroB
        numeroMenor = numeroA

    listado = []
    i = numeroMenor
    suma = 0
    while i <= numeroMayor:
        if (i%2!=0):
            suma = suma + i
        i = i+1

    return suma / 2


def main():
    numeroA = int(input('Ingrese un número: '))
    numeroB = int(input('Ingrese otro número: '))
    return mediaSumaImpar(numeroA, numeroB)

result = main()

print(result)