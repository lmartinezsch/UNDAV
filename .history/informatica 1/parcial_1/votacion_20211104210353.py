# -*- coding: utf-8 -*-

def main():

    listaA = 0
    listaB = 0
    listaC = 0
    listaD = 0

    while True:
        voto = str(input('Ingrese la lista a votar (A,B,C,D): '))
        voto = voto.lower()

        if voto == "*":
            break
        elif voto == "a":
            listaA = listaA + 1
        elif voto == "b":
            listaB = listaB + 1
        elif voto == "c":
            listaC = listaC + 1
        elif voto == "d":
            listaD = listaD + 1



main()