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
    print("────────────────────────────")
    print("[1] Multiplicar [2] Dividir")
    print("[3] Sumar       [4] Restar \n")

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

    print("────────────────────────────")