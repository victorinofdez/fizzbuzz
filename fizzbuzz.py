'''
En esta kata, se solicita al usuario un numero, si este es:

- Divisible entre 3, el programa debe imprimir "Fizz"

- Divisible entre 5, el programa debe imprimit "Buzz"

- Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"

- Si no es divisible ni entre 3 ni entre 5, debe imprimir el número
'''

def fizzbuzz():
    continuar = True

    while continuar:
        try:
            entrada = input("Introduce un número del 1 al 100 (o 'q' para salir): ")

            if entrada.lower() == "q":
                print("Hasta luego 👋")
                continuar = False
            else:
                numero = int(entrada)

                if numero < 1 or numero > 100:
                    print("El número debe estar entre 1 y 100\n")
                elif numero % 3 == 0 and numero % 5 == 0:
                    print("FizzBuzz\n")
                elif numero % 3 == 0:
                    print("Fizz\n")
                elif numero % 5 == 0:
                    print("Buzz\n")
                else:
                    print(f"{numero}\n")

        except Exception:
            print("Error en la entrada. Introduce un número válido.\n")


if __name__ == "__main__":
    fizzbuzz()

