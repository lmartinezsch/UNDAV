def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i

    print("El factorial es: " + str(result))


def main():
    number = int(input("Escriba un número: "))
    factorial(number)


main()
