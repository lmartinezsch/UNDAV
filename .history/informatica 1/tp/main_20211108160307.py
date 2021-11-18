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
            print('La fecha ingresada es inválida.')
            continue

        return fecha

def getGeneroDenunciante():
    while True:
        genero = str(input('Ingresar el genero autopercibido del denunciante (m,v,x): ')).lower()

        if genero == 'm' or genero == 'v' or genero == 'x':
            break
        else:
            print('El genero ingresado es inválido. Debe ingresar M, V o X')
            continue

    return genero

def getGeneroPersonaDenunciada():
    while True:
        genero = str(input('Ingresar el genero de la persona denunciada (m,v,x): ')).lower()

        if genero == 'm' or genero == 'v' or genero == 'x':
            break
        else:
            print('El genero ingresado es inválido. Debe ingresar M, V o X')
            continue

    return genero

def getClaustroDenunciante():
    while True:
        claustro = str(input('Ingresar el claustro del denunciante (E, N, D o G): ')).lower()

        if claustro == 'e' or claustro == 'n' or claustro == 'd' or claustro == 'g':
            break
        else:
            print('El claustro ingresado es inválido. Debe ingresar: E, N, D o G')
            continue

    return claustro

def getClaustroPersonaDenunciada():
    while True:
        claustro = str(input('Ingresar el claustro de la persona denunciada (E, N, D o G): ')).lower()

        if claustro == 'e' or claustro == 'n' or claustro == 'd' or claustro == 'g':
            break
        else:
            print('El claustro ingresado es inválido. Debe ingresar: E, N, D o G')
            continue

    return claustro


def main():

    anioInforme = getAnioInforme()
    semestre = getSemestre()
    numeroExpediente = int(input('Ingresar número de expediente:'))
    fechaDenuncia = getFechaDenuncia()
    generoDenunciante = getGeneroDenunciante()
    claustroDenunciante = getClaustroDenunciante()
    tipoSituacionVivenciada = str(input('Ingresar el tipo de situación vivenciada: '))
    generoPersonaDenunciada = getGeneroPersonaDenunciada()
    claustroPersonaDenunciada = getClaustroPersonaDenunciada()


    print('Año de informe: ' + str(anioInforme))
    print('Semestre de informe: ' + str(semestre))
    print('Nro de expediente: ' + str(numeroExpediente))
    print('Fecha de denuncia: ' + str(fechaDenuncia))
    print('Genero denunciante: ' + str(generoDenunciante))
    print('Claustro denunciante: ' + str(claustroDenunciante))
    print('Tipo de situación vivenciada: ' + str(tipoSituacionVivenciada))
    print('Genero de persona denunciada: ' + str(generoPersonaDenunciada))
    print('Claustro persona denunciada: ' + str(claustroPersonaDenunciada))

        
main()