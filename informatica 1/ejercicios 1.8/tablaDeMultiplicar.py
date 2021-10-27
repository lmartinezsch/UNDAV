def multiplicacion(n):
    for i in range(0, n):
        result = n*i
        print(str(n) + " * " + str(i) + ": " + str(result))


def suma(n):
    result = 0
    for i in range(1, n+1):
        result = result+i

    print("la suma de los nros naturales es: " + str(result))


def main():
    number = int(input("Escriba un número: "))
    multiplicacion(number)
    suma(number)


main()
