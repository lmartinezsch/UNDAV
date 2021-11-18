# -*- coding: utf-8 -*-

ANIO_INFORME = 2021


def getAnioInforme():
    while True:
        anioInforme = int(input('Ingrese el año del informe: '))
        if anioInforme >= ANIO_INFORME:
            break
        else:
            print('El año ingresado no puede ser anterior al 2021')
            continue

    while True:    
        anioInforme2 = int(input('Vuelva a ingresar el año del informe: '))
        if anioInforme2 == anioInforme:
            break
        else:
            print('Los años ingresados del informe no coinciden')
            continue

    return anioInforme

def main():

    anioInforme = getAnioInforme()

    print(anioInforme)
        
    
        
main()