from fizzbuzz.fizzbuzz import fizzbuzz
import pytest 

def test_numero_divisible_entre_3_imprime_fizz():
# Divisible entre 3, el programa debe imprimir "Fizz"
    assert fizzbuzz(3) == "Fizz"
    pass


def test_numero_divisible_entre_5_imprime_buzz():
# Divisible entre 5, el programa debe imprimit "Buzz"
    assert fizzbuzz(5) == "Buzz"
    pass


def test_numero_divisible_entre_3_y_5_imprime_fizzbuzz():
# Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"
    assert fizzbuzz(15) == "FizzBuzz"
    pass

def test_input_numero_negativo_lanza_error():
# input de número negativo
    with pytest.raises(ValueError):
        fizzbuzz(-3)
    pass


def test_input_cero_lanza_error():
# input de número cero
    with pytest.raises(ValueError):
        fizzbuzz(0)
    pass


def test_input_numero_decimal_lanza_error():
# input de numero decimal
    with pytest.raises(TypeError):
        fizzbuzz(3.5)
    pass


def test_input_caracter_no_numerico_lanza_error():
# input de un carácter no numérico
    with pytest.raises(TypeError):
        fizzbuzz("@")
    pass


def test_input_cadena_texto_lanza_error():
# input de una candena de texto
    with pytest.raises(TypeError):
        fizzbuzz("hola")
    pass


def test_input_numero_mayor_a_100_lanza_error():
# input de número por encima de 100
    with pytest.raises(ValueError):
        fizzbuzz(101)
    pass

def test_input_numero_menor_a_1_lanza_error():
# input de número por debajo de 1
    with pytest.raises(ValueError):
        fizzbuzz(-1)
    pass
