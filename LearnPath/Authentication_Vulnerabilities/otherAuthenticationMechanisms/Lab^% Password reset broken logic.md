# Lab: Password reset broken logic

This lab's password reset functionality is vulnerable. To solve the lab, reset Carlos's password then log in and access his "My account" page.

- Your credentials: wiener:peter
- Victim's username: carlos

## Solution

According to the title of lab we test feature reset password with user `wiener`, which was owned the credentials by us.

When we click `Forgot password` button, we are redirected to `forgot password` page.

![](https://i.imgur.com/FDF0LFC.png)

After submit with username `wiener`, check email we received an link access to `forgot password` page with token `temp-forgot-password-token`, which should expire after a short period of time and be destroyed immediately after the password has been reset.

![](https://i.imgur.com/ljsAux3.png)

Fill in your password and before submit let turn on `intercept` in burp suite:

![](https://i.imgur.com/0OyJGue.png)

Modify param `username` from `wiener` to `carlos` then forward this request.

Now we trying login with credentials: `carlos:123`

And then we solve this lab