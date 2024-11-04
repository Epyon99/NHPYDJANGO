class Empleado:
    caracteristica = "Hola"
    def __init__(self) -> None:
        pass
    def trabajar(self):
        pass

def factorial(numero):
    contador = 1
    while numero > 1:
        contador *= numero
        numero -= 1
    return contador

def mostrar_factorial(numero):
    print (f"El factorial es: {numero}")
    pass

print ("Ejemplo de una funcion de factorial \n")
mostrar_factorial(factorial(int(input("Ingresa un numero para el factorial\n"))))