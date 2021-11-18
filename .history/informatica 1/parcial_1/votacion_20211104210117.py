# -*- coding: utf-8 -*-

def main():

    while True:
        voto = str(input('Ingrese la lista a votar (A,B,C,D): '))
        voto = voto.lower()

        if voto == "*":
            break
        elif voto != "a" or voto != "b" or voto != "c" or voto != "d":
            print('El voto ingresado es incorrecto')

main()