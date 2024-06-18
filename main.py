# modulos
import os
from lista_opciones import *
from calculadora import *
from conversor import * 
from frecuencias import *

# INICIO DEL PROGRAMA
os.system("cls")

lista_de_opciones = [
    "Calculadora",
    "Conversor de Monedas",
    "Graficar Frecuencias",
    "Opción 4",
    "Opción 5",
    "Opción 6",
    "Opción 7",
    "Opción 8",
    "Opción 9",
    "Salir"
]

while True:
    cargar_opciones(lista_de_opciones)

    # EJECUTO MI PROGRAMA ESPERANDO UN POSIBLE ERROR
    try: # SI NO HAY ERRORES
        respuesta = input("[?] ")

        if respuesta == "1":
            programa_calculadora()
        elif respuesta == "2":
            conversor_de_monedas()
        elif respuesta == "3":
                lista = [
                    {"producto":"Tomate  ","f":20},
                    {"producto":"Coliflor","f":30},
                    {"producto":"Espinaca","f":35},
                    {"producto":"Apio    ","f":20}
                ]
                grafica_frecuencias(lista)
        elif respuesta == '10':
            print("[Fin del Programa]")
            break

    except: #SI HAY ERROR
        print("valor nulo")