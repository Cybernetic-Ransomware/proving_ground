import requests

"""
  site to testing responses
https://httpbin.org/


  to hide your ip adress
res_details = response.json()
del res_details['origin]

"""

response = requests.get('https://httpbin.org/get')
print(response.status_code)
# print(response.text)
# print(response.json())


response = requests.get('https://httpbin.org/get?name=Theodore&age=31')
print(response.status_code)
# print(response.text)


parameters_01 = {
    'name': 'Julia',
    'age': 25
}
response = requests.get('https://httpbin.org/get', params=parameters_01)
print(response.status_code)
# print(response.url)
# print(response.text)


parameters_02 = {
    'name': 'Bobby',
    'age': 13
}
response = requests.post('https://httpbin.org/post', data=parameters_02)
print(response.status_code)
# print(response.json())


response = requests.get('https://httpbin.org/status/404')
print(response.status_code)
# if response.status_code == requests.codes.not_found:
#     print('succesfull test, connection lost')
# else:
#     print('this should not happen')


response = requests.get('https://httpbin.org/user-agent')
print(response.status_code)
# print(response.text)


headers = {
    'User-Agent': 'MarioPizza/2.0'
}
response = requests.get('https://httpbin.org/user-agent', headers=headers)
print(response.status_code)
# print(response.text)


headers = {
    'User-Agent': 'MarioPizza/2.0',
    'Accept': 'image/png'
}
response = requests.get('https://httpbin.org/image', headers=headers)
print(response.status_code)
# with open('my_image.png', 'wb') as f:
#     f.write(response.content)


response = requests.get('https://httpbin.org/delay/3')
print(response.status_code)


for i in range(4, 0, -1):
    try:
        response = requests.get('https://httpbin.org/delay/3', timeout=i)
        print('timeout testing')
        print(response.status_code)
    except:
        print('succes, at least failed')
        continue


proxies = {
    'http': '139.99.237.62:80',
    'https': '139.99.237.62:80'
}
response = requests.get('http://httpbin.org/get', proxies=proxies)
print(response.status_code)
print(response.text)
