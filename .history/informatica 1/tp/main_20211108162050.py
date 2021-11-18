# -*- coding: utf-8 -*-
import datetime
import csv

ANIO_INFORME = 2021
GENERO_MASCULINO = "m"
GENERO_FEMENINO = "f"
GENERO_OTRE = "x"
CLAUSTRO_ESTUDIANTE = "e"
CLAUSTRO_NODOCENTE = "n"
CLAUSTRO_DOCENTE = "d"
CLAUSTRO_GRADUADO = "g"

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
        genero = str(input('Ingresar el genero autopercibido del denunciante (m,f,x): ')).lower()

        if genero == GENERO_MASCULINO or genero == GENERO_FEMENINO or genero == GENERO_OTRE:
            break
        else:
            print('El genero ingresado es inválido. Debe ingresar M, F o X')
            continue

    return genero

def getGeneroPersonaDenunciada():
    while True:
        genero = str(input('Ingresar el genero de la persona denunciada (m,v,x): ')).lower()

        if genero == GENERO_MASCULINO or genero == GENERO_FEMENINO or genero == GENERO_OTRE:
            break
        else:
            print('El genero ingresado es inválido. Debe ingresar M, V o X')
            continue

    return genero

def getClaustroDenunciante():
    while True:
        claustro = str(input('Ingresar el claustro del denunciante (E, N, D o G): ')).lower()

        if claustro == CLAUSTRO_ESTUDIANTE or claustro == CLAUSTRO_NODOCENTE or claustro == CLAUSTRO_DOCENTE or claustro == CLAUSTRO_GRADUADO:
            break
        else:
            print('El claustro ingresado es inválido. Debe ingresar: E, N, D o G')
            continue

    return claustro

def getClaustroPersonaDenunciada():
    while True:
        claustro = str(input('Ingresar el claustro de la persona denunciada (E, N, D o G): ')).lower()

        if claustro == CLAUSTRO_ESTUDIANTE or claustro == CLAUSTRO_NODOCENTE or claustro == CLAUSTRO_DOCENTE or claustro == CLAUSTRO_GRADUADO:
            break
        else:
            print('El claustro ingresado es inválido. Debe ingresar: E, N, D o G')
            continue

    return claustro

def saveData():
    with open('thefile.csv', 'rb') as f:
    data = list(csv.reader(f))

    import collections
    counter = collections.defaultdict(int)
    for row in data:
        counter[row[0]] += 1


    writer = csv.writer(open("/path/to/my/csv/file", 'w'))
    for row in data:
        if counter[row[0]] >= 4:
        writer.writerow(row)


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

    saveData()

        
main()