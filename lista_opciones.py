# lista de opciones


# Función
def cargar_opciones(lista_de_opciones):
    imprimirLinea()
    
    for opcion in lista_de_opciones:
        indice = lista_de_opciones.index(opcion)+1
        if indice%2 == 0:
            print(f"[{indice}]{opcion}")
        else:
            mensaje = f"[{indice}]{opcion} " 
            print(mensaje," "*(15-len(mensaje)),end="")
    print("\n","─"*30)
    
def imprimirLinea():
    print("─"*30)