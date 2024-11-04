def test_recursividad(numero):
    if (numero < 999):
        return numero + test_recursividad(numero+1)
    else:
        return 0
    
print (test_recursividad(0))
