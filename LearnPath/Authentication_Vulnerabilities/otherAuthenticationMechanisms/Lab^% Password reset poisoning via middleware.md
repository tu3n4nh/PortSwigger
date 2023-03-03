# Lab: Password reset poisoning via middleware

This lab is vulnerable to password reset poisoning. The user carlos will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account. You can log in to your own account using the following credentials: `wiener:peter`. Any emails sent to this account can be read via the email client on the exploit server.

## Solution

According to the [previous lab](https://github.com/tu3n4nh/CTF/blob/main/PortSwigger/LearnPath/Authentication_Vulnerabilities/otherAuthenticationMechanisms/Lab:%20Basic%20password%20reset%20poisoning.md), we continue us password reset poisoning to get reset password token from user with our server.

In this time, Host header was filtered out. If we still modify Host header and send it, we will receive 403 Forbidden response.

![](https://i.imgur.com/kZcQYrB.png)

But we can still change [Host](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host) via [X-Forwarded-Host](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Host) header

> The X-Forwarded-Host (XFH) header is a de-facto standard header for identifying the original host requested by the client in the Host HTTP request header. 

![](https://i.imgur.com/b0aOzWA.png)

With this way, we implement change host request without 403 forbidden response. So user carlos will receive an URL to reset password, which contain reset password token, but domain name in url is our control, like that:

![](https://i.imgur.com/PAVzzbt.png)

If user carlos click on the url, we will be received carlos's reset password token

![](https://i.imgur.com/aP0fM0w.png)

Use this token to reset password user carlos

![](https://i.imgur.com/smneSNC.png)

Login with new password to solve this lab.