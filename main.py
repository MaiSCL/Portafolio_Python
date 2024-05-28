# modulos
import os
from lista_opciones import cargar_opciones
from calculadora import programa_calculadora

# INICIO DEL PROGRAMA
os.system("cls")

while True:
    cargar_opciones()

    # EJECUTO MI PROGRAMA ESPERANDO UN POSIBLE ERROR
    try: # SI NO HAY ERRORES
        respuesta = input("[?] ")

        if respuesta == "1":
            programa_calculadora()
        elif respuesta == '10':
            print("[Fin del Programa]")
            break

    except: #SI HAY ERROR
        print("valor nulo")