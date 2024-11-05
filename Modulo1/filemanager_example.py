#with open("textdump.txt", 'r') as archivo:
#    contenido = archivo.read()
#    #print (contenido)
#    print(type(contenido))

#with open("archivonuevo.txt", 'a') as archivo:
#    archivo.write("texto nuevo2\n")

#with open("balenaEtcher.lnk",'rb') as fbinary:
#    print (fbinary.read())

#lista = []
#with open("textdump.txt", 'rb') as fbinary:
#    while True:
#        bloque = fbinary.read(1000)
#        if not bloque:
#            break
#        lista.append(bloque)
#print(len(lista))
#print (lista[2])

datos = [25,31,255,2,140]
with open("archivo.bin", 'wb') as fbinary:
    fbinary.write(bytes(datos))
