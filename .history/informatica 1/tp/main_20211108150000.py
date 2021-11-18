# -*- coding: utf-8 -*-
import datetime

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

def getSemestre():
    while True:
        semestre = int(input('Ingrese el semestre que corresponda: '))
        if semestre == 1 or semestre == 2:
            break
        else:
            print('El semestre ingresado no corresponde')
            continue
    
    return semestre

def getFechaDenuncia():
    while True:
        fecha = str(input('Ingresar fecha de denuncia (01/07/2021): '))
        format = "%Y-%m-d"
        format = "%d/%m/%Y"
        try:
            datetime.datetime.strptime(fecha, format)
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    return fecha



def main():

    anioInforme = getAnioInforme()
    semestre = getSemestre()
    numeroExpediente = int(input('Ingresar número de expediente:'))
    fechaDenuncia = getFechaDenuncia()
    generoDenunciante = str(input('Ingresar el genero autopercibido del denunciante (m,v,x): '))
    claustroDenunciante = str(input('Ingresar el claustro del denunciante: '))
    tipoSituacionVivenciada = str(input('Ingresar el tipo de situación vivenciada: '))
    generoPersonaDenunciada = str(input('Ingresar el genero de la persona denunciada (m,v,x): '))
    claustroPersonaDenunciada = str(input('Ingresar el claustro de la persona denunciada: '))


    print(anioInforme)
    print(semestre)
        
    
        
main()