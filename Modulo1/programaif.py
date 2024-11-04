continuar = True

while continuar:
    accion = input ("Escribe cualquier palabra para continuar y quit para salir")
    if (accion == "quit"):
        break
    x = input ("Valor de x \n")
    y = input ("Valor de y \n")
    if int(x) > int(y):
        print ("X es mayor")
    else: 
        print ("Y es mayor")
