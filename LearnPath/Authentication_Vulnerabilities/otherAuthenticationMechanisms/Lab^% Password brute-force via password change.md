# Lab: Password brute-force via password change

This lab's password change functionality makes it vulnerable to brute-force attacks. To solve the lab, use the list of candidate passwords to brute-force Carlos's account and access his "My account" page.

- Your credentials: wiener:peter
- Victim's username: carlos
- [Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

## Solution

Start with trying functionality change password of application.

We login with wiener credentials and then try to change password 

![](https://i.imgur.com/2zhuNZp.png)

Observe the body of the request we see that the username variable is hidden, it seems to change the carlos password we just need to change the username variable from `wiener` to `carlos` 

Problem here is what's carlos's password? Following the title of the lab we trying send that request to Intruder, add marker into the curent password variable and then start attack. But it doesn't work, because if we submit wrong current password we have been redirected back to login page and the session will be changed. This makes the next brute-force password with old session useless.

After view some hints, we need check what happen if we submit different new password 1 with new password 2, twice when the current password is correct and when the current password is wrong.

With the current password is correct:

![](https://i.imgur.com/adS4aa9.png)

The response contain `New passwords do not match` message

With the current password is wrong:

![](https://i.imgur.com/ymm32KA.png)

The respones contain `Current password is incorrect` message and we aren't redirected back to login page ().

So based on entering two different new passwords we can brute force password until response is returned contain message `New passwords do not match`, which is the correct password of carlos.

![](https://i.imgur.com/EjnitL0.png)

Login with carlos's credentials to solve this lab