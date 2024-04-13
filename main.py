def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def main():
    try:
        num1 = int(input("Ingresa el primer número entero: "))
        num2 = int(input("Ingresa el segundo número entero: "))

        if num1 < 0 or num2 < 0:
            print("Por favor ingresa números enteros positivos.")
            return

        resultado = mcd(num1, num2)
        print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")

    except ValueError:
        print("Por favor ingresa números enteros válidos.")


if __name__ == "__main__":
    main()
