# lista de opciones
lista_de_opciones = [
    "Calculadora",
    "Opción 2",
    "Opción 3",
    "Opción 4",
    "Opción 5",
    "Opción 6",
    "Opción 7",
    "Opción 8",
    "Opción 9",
    "Opción 10"
]

# Función
def cargar_opciones():
    print("-----------------------------")
    columna = 0
    for opcion in lista_de_opciones:
        indice = lista_de_opciones.index(opcion)+1
        if columna < 1:
            print(f"[{indice}]{opcion}     ",end="")
            columna +=1
        else:
            print(f"[{indice}]{opcion}    ")
            columna = 0
    print("\n----------------------------")