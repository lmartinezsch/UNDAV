# -*- coding: utf-8 -*-

def main():
    ANIO_INFORME = 2021

    while True:
        anioInforme = int(input('Ingrese el año del informe: '))
        if anioInforme >= ANIO_INFORME:
            break
        else:
            print('El año ingresado no puede ser anterior al 2021')
            continue
        
    anioInforme2 = int(input('Vuelva a ingresar el año del informe: '))
    if anioInforme2 != anioInforme:
        print('Los años ingresados del informe no coinciden')
        
main()