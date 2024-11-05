def EjecutarError():
    raise Exception("Hola Mundo")

try:
    EjecutarError()
    a = int(input("Valor 1:\n"))
    assert type(a) == type(1)
    b = int(input("Valor 2:\n"))
    print ("\n")
    t = a / b
    print (t)
except ZeroDivisionError:
    print ("El programa va a seguir")
except TypeError:
    print ("Error de tipos")
except AssertionError:
    print ("Assertion error")
except Exception:
    print ("My exception")
else:
    print ("Else de exito")
finally:
    print ("Fin del programa")

#x = "hola"
#assert x != "hola"
#print ("fin")