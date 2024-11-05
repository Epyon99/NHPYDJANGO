def filterx2(x):
    return x%2 != 0
numeros = {1,2,3,4,5,6,7,8,9,10}

impares = set(filter(lambda x: x%2 != 0,numeros))
impares = set(filter(filterx2,numeros))
# filter devuelve los elementos que cumplen la funcion
print (impares)