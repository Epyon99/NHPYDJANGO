import requests
from requests.auth import HTTPBasicAuth
response = requests.post('https://google.com')

#print (response.status_code)
#for h in response.headers:
    #print (f"{h}")
#print (response.text)


url = "https://httpbin.org/post"
datos= {'key':'moises'}
response = requests.post(url, data=datos)

#print(response.status_code)
#print(response.text)


# GET + Params
url = "https://httpbin.org/get"
parametros = {
    'q':'query ? , . valor',
    'numero':10
}
response = requests.get(url,params=parametros)
#print(response.status_code)
#print (response.text)

my_headers = {'User-Agent':'mi-app'}
response = requests.get(url,headers=my_headers)
#print (response.status_code)
#print (response.text)


response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user','pass'))
#print (response.status_code)
#print (response.text)

#try:
response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user','pass'))
    #print (response.status_code)
    #print (response.text)
#response.raise_for_status()
#except requests.exceptions.HTTPError as err:
    #print (f'Error HTTP:{err}')
#except requests.exceptions.RequestException as err:
    #print(f'Error en la solicitud: {err}')


url = "https://httpbin.org/delete"
my_files = {'archivo': open('balenaEtcher.lnk','rb')}
response = requests.delete(url,files=my_files)
print (response.text)


# PUT

# DELETE