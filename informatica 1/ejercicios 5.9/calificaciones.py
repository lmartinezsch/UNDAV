# -*- coding: utf-8 -*-

def getCalificacionMasAlta():
    print("hola")


def main():

    calificaciones = []
    while True:
        legajo = int(input('Ingrese el legajo: '))
        if legajo == -1:
            break

        calificacion = int(input('Ingrese la calificación: '))
        calificaciones.append(calificacion)

    cantidadCalificacionesIngresadas = str(len(calificaciones))
    maximaCalificacion = str(max(calificaciones))
    sumaTotal = str(sum(calificaciones))
    promedio = str(sum(calificaciones) / len(calificaciones))
    print('Cantidad de calificaciones ingresadas: ' +
          cantidadCalificacionesIngresadas)
    print('Calificación máxima: ' + maximaCalificacion)
    print('Suma total de calificaciones: ' + sumaTotal)
    print('Promedio de calificaciones: ' + promedio)


main()
