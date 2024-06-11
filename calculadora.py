from lista_opciones import *

# @multiplicar: función que requiere 2 parametros
# @return retorna el resultado de la operación
# a*b

def multiplicar(a,b):
    return a*b

# @dividir función que requiere de dos parametros
# @return retorna el resultado de la operación
# a/b

def dividir(a,b):
    return a/b

# @sumar función que requiere 2 parametros
# @return retorna el resultado de la operación
# a+b

def sumar(a,b):
    return a+b

# @restar función que requiere de dos parametros
# @return retorna el resultado de la operación
# a-b

def restar(a,b):
    return a-b


# --------------------
# PROGRAMA CALCULADORA
# --------------------

def programa_calculadora():
    opciones_calculadora = ["Multiplicar", "Dividir", "Sumar", "Restar"]
    cargar_opciones(opciones_calculadora)

    opcion = input("[?]: ")

    num1 = int(input("[Num 1]: "))
    num2 = int(input("[Num 2]: "))

    if opcion == '1':
        print("[R >]:", multiplicar(num1, num2))
    elif opcion == '2':
        print("[R >]:", dividir(num1, num2))
    elif opcion == '3':
        print("[R >]:", sumar(num1, num2))
    elif opcion == '4':
        print("[R >]:", restar(num1, num2))

    imprimirLinea()