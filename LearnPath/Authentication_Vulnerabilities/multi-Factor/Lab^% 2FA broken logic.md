# Lab: 2FA broken logic

## Lab

This lab's two-factor authentication is vulnerable due to its flawed logic. To solve the lab, access Carlos's account page.

- Your credentials: `wiener:peter`
- Victim's username: `carlos`

You also have access to the email server to receive your 2FA verification code. 

## Hint

Carlos will not attempt to log in to the website himself. 

## Solution

After fuzzing we know that if we login with credentials of `wiener`, application will redirect we to `/login2` page also set for us a new cookie, which is used to create and authenticate `security code` of user `wiener`.

To get `security code` of user `wiener` we just click 'Email client' button.

![Get wiener's security code](https://i.imgur.com/vUCf6m8.png)

Authenticate login2 with security code just received, after that application set for we a one more new cookie, which is used to authenticate that we have passed two-factor authentication and then we can access `/my-account` page without any login or authentication anymore

![Authenticate login2 with security code just received](https://i.imgur.com/MbwJQdD.png)

This lab is more difficult than the previous one in that it confirms whether the user has completed the two steps of authentication and then allows the user access to `/my-account` page. So that we can't authenticate in `/login` then redirect straight to 'my-account' page.

One more thing, we can't use `session` of `wiener` for `carlos`, because each user has a different `security code`. And the `security code` will be change with each `session`.

To login carlos's account first steps is get a `session cookie` of carlos, which is used to create a `security code` for carlos in that `session cookie`. 

As noted above, we have to login successful in `/login` page then application will redirect us to `/login2` page to create `security code`. Besides we don't have password of carlos so that way login valid credentials of carlos is impossible.

But there's still a way, we can use back old get request `/login2` of user `wiener` and modify variable `verify` from `wiener` to `carlos` then send this request to create `security code` of user `carlos` for this `session`.

Next steps is brute force `security code` of user `carlos`. Still use back old post request `/login2` of user `wiener` send it to Intruder, keep attack type intact, clear all payload markers, modify variable `verify` from `wiener` to `carlos` and add a payload marker to value of `mfa-code`
![Modifying in Intruder](https://i.imgur.com/2vIgDem.png)
In Payloads tab, set payload type is `Brute forcer`, modify character set: `0123456789` and min, max length are `4` then start attack.
![Modifying in Payloads tab](https://i.imgur.com/mJQvfwy.png)
Send which request returns status code 302 to browser to solve this lab