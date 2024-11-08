import requests
url = 'https://httpbin.org/cookies/set/nombre_cookie/valor_cookie'
my_cookies = {'a':'10','b':"Alicia"}

response = requests.get(url,cookies=my_cookies)

print(response.status_code)
print(response.text)
for c in response.cookies:
    print (f'{c.name},{c.value}')
