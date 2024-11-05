import re

texto = "La casa es azul y el coche es azul."
patron = r"\w+"

coincidencias = re.findall(patron,texto)
print (coincidencias) # azul azul

separado = re.split(patron,texto)
print (separado) # la casa es, y el coche es , .

nuevo_texto = 'rojo'
substitucion = re.sub(patron,nuevo_texto,texto)
print (substitucion)

busqueda = re.search(patron,texto)
print (busqueda)

coincidencia = re.match(patron,texto)
if coincidencia:
    print (coincidencia.group())
else:
    print ("no encontrado")
