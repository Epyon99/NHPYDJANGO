import requests
response = requests.post('https://google.com')

print (response.status_code)
for h in response.headers:
    print (f"{h}")
print (response.text)


url = "https://httpbin.org/post"
datos= {'key':'moises'}
response = requests.post(url, data=datos)

print(response.status_code)
print(response.text)
