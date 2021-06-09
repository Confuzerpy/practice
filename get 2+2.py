import requests

server, port, a, b = input(), input(), int(input()), int(input())
params = {'a': a, 'b': b}
response = requests.get(f'{server}:{port}', params=params)
response_json = response.json()
print(*sorted(response_json['result']))
print(response_json['check'])
