# -*- coding: utf-8 -*-

def promediarPotencias(n1, n2, n3):

    numeroMenor = 0
    numeroMayor = 0
    if (n1 > n2):
        numeroMayor = n1
        numeroMenor = n2
    else:
        numeroMayor = n2
        numeroMenor = n1

    sumaDePotencias = 0
    cantidad = 0
    i = numeroMenor
    while i <= numeroMayor:
        cantidad = cantidad + 1
        sumaDePotencias = sumaDePotencias + i**n3
        i = i + 1

    avg = sumaDePotencias / cantidad

    return round(avg)

def main():
    n1 = int(input('Ingrese un primer número: '))
    n2 = int(input('Ingrese un segundo número: '))
    n3 = int(input('Ingrese un tercer número: '))
    return promediarPotencias(n1, n2, n3)

result = main()

print(result)