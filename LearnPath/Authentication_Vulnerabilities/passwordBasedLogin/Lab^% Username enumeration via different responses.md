# Lab: Username enumeration via different responses

## Lab

 This lab is vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

- [Candidate usernames](https://portswigger.net/web-security/authentication/auth-lab-usernames)
- [Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

## Solution

After fuzzing by brute force username, we determine that if we input invalid username, the response will return `Invalid username`, even if the username is valid, the response will return `Incorrect password` depending on that to confirm the username enumeration.

After have correct username `applications` we continue brute force password. Check the response, which returns different content length is the password of this user (`charlie`). 

login with username `applications` and password `charlie` to solve this lab.