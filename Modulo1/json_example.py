import json

json_data = '{"nombre":"moises"}'

datos = json.loads(json_data)
print (datos)
print (type(datos))

with open("jsonfile.json",'r') as json_file:
    txt = json.loads(json_file.read())
    print(txt)

