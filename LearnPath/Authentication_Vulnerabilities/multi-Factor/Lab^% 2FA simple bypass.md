# Lab: 2FA simple bypass

## Lab

This lab's two-factor authentication can be bypassed. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, access Carlos's account page.

- Your credentials: `wiener:peter`
- Victim's credentials `carlos:montoya`

## Solution

In this application, after `/login` with credential we are redirected to `/login2`. Each time we post a request to the application, it returns a new cookie, which is used to authenticate that we successfully logged in in previous step.

What happening if we skip second factor authentication (`/login2` page), get the cookie is returned from first factor authentication (`/login` page) and add it to the request `/my-account`
![login victim's crendentials and get a new cookie](https://i.imgur.com/MhMdUzP.png)
And now our cookie is `XLleTNjqmUgmVGSRlKFCxnP6nrm5ZIux`, sending request to get `/my-account` page with this new cookie.
![sending request with new cookie](https://i.imgur.com/h7h9MwV.png)

So that we have logged in the carlos's account! Seem the application don't check whether we have finished all of authentication factor yet. That why we can login carlos's account and solve this lab.