def slicex2(val):
    text=str(val)
    return text[::-1]

lista = ["hola", "mundo"]
mapper = map(slicex2,lista)
mayusculas = set(mapper)

print(mayusculas)
print(type(mapper))
