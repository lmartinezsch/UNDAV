# -*- coding: utf-8 -*-
def main():
    suma = 0
    cantidad = 0

    while True:
        numero = int(input('Ingrese un número: '))
        if (numero == -100):
            break
        elif (numero >= 8):
            print('Mayor o igual a 8')
        elif(numero <= 2):
            print('Menor o igual a 2')
        else:
            suma = suma + numero
            cantidad = cantidad + 1
            
    print('Suma total: ' + str(suma))
    print('Cantidad de números: ' + str(cantidad))

main()
