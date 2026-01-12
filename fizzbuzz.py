'''
En esta kata, se solicita al usuario un numero, si este es:

- Divisible entre 3, el programa debe imprimir "Fizz"

- Divisible entre 5, el programa debe imprimit "Buzz"

- Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"

- Si no es divisible ni entre 3 ni entre 5, debe imprimir el número
'''

def div3(numero) {
    return (numero % 3) == 0 
}
def div5(numero) {
    return (numero % 3) == 0 
}
def div3y5(numero) {
    return (numero % 3) == 0 and (numero % 5) == 0
}

if __name__ == "__main__":
    inp = '' 
    while True:
        inp = int(input())
        if div3(inp):
            print("Fizz\n")
        elif div5(inp):
            print("Buzz\n")
        elif div3y5(inp):
            print("FizzBuzz\n")
        else:
            print(inp)    
