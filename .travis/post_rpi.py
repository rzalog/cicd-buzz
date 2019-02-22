import requests
import os

data = {'image': os.getenv('TRAVIS_REPO_SLUG', '')}
ip = os.getenv('DEPLOYINATOR_ENDPOINT', '128.97.89.42')
port = os.getenv('DEPLOYINATOR_PORT', 5050)

url = 'http://{}:{}/run'.format(ip, port)
res = requests.post(url, json=data)
print('Posted RPi:')
print(res.json())