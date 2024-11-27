from sumar import sumar
from restar import restar


def main():
    print("Bienvenido a la calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Elevar al cuadrado")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", sumar(a, b))
    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", restar(a, b))
    elif opcion == 3:
        a = float(input("Ingresa el dividendo: "))
        b = float(input("Ingresa el divisor: "))
        print("Resultado:", dividir(a, b))
    elif opcion == 4:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", multiplicar(a, b))
    elif opcion == 5:
        a = float(input("Ingresa el número: "))
        print("Resultado:", elevar(a))
    else:
        print("Opción no válida")


if __name__ == "__main__":
    main()
