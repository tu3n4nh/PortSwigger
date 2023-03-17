# Lab: Information disclosure on debug page

Link to lab: https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-on-debug-page

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Access that link to get SECRET_KEY:

url = 'https://0aee00e503fadbe0c0d59f7b00b30059.web-security-academy.net/cgi-bin/phpinfo.php'

# Change the SECRET_KEY:

key = ''

data = {
    'answer': key
}

response = requests.post(
    'https://0aee00e503fadbe0c0d59f7b00b30059.web-security-academy.net/submitSolution',
    data=data,
    verify=False,
)

print(response.text)
```