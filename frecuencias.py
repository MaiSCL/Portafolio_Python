#definición de función
def grafica_frecuencias(lista):
    #Bucle para la lista
    for p in lista:
        #impresión del producto
        print(p["producto"]," ",end="")
        #Bucle para frecuencia
        for n in range(p["f"]):
            #Impresión de 0
            print("0",end="")
        #Espacio vacío    
        print("")