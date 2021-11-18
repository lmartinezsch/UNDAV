# -*- coding: utf-8 -*-

def main():

    ''' Instancio variables'''
    cantidadVotantes = 0
    listaA = 0
    listaB = 0
    listaC = 0
    listaD = 0

    ''' 
    Mientras nadie ingrese un asterísco el while va a seguir preguntando a quien vota.
    Si el voto no coincide con las listas dadas, se vuelve a preguntar y no se contabiliza el voto ni el votante
    '''
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
        else:
            continue

        cantidadVotantes = cantidadVotantes + 1

    print('Se presentaron ' + str(cantidadVotantes) + ' votantes')

    ''' Imprimo la cantidad de votos recibidos en cada lista'''
    print('La lista A recibió ' + str(listaA) + ' votos')
    print('La lista B recibió ' + str(listaB) + ' votos')
    print('La lista C recibió ' + str(listaC) + ' votos')
    print('La lista D recibió ' + str(listaD) + ' votos')

    ''' Obtengo los porcentajes de cada lista '''
    avgListaA = listaA / cantidadVotantes * 100
    avgListaB = listaB / cantidadVotantes * 100
    avgListaC = listaC / cantidadVotantes * 100
    avgListaD = listaD / cantidadVotantes * 100

    ''' Imprimo los porcentajes de cada lista '''
    print('La lista A obtuvo un ' + str(avgListaA) + '% de los votos')
    print('La lista B obtuvo un ' + str(avgListaB) + '% de los votos')
    print('La lista C obtuvo un ' + str(avgListaC) + '% de los votos')
    print('La lista D obtuvo un ' + str(avgListaD) + '% de los votos')







main()