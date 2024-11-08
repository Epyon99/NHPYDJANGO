import requests

session = requests.Session()

session.get('https://httpbin.org/cookies/set/nombre_cookie/valor_cookie')
session.get('https://httpbin.org/cookies/set/nombre/alice')
session.get('https://httpbin.org/cookies/set/sitio/wonderland')
response = session.get('https://httpbin.org/cookies')
print (f"Primer ejemplo: {response.text}")

print ("\n")

requests.get('https://httpbin.org/cookies/set/nombre_cookie/valor_cookie')
requests.get('https://httpbin.org/cookies/set/nombre/alice')
requests.get('https://httpbin.org/cookies/set/sitio/wonderland')
response = requests.get('https://httpbin.org/cookies')
print (f"Segundo ejemplo: {response.text}")
