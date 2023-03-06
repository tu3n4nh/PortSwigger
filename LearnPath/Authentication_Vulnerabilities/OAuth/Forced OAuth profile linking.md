# Lab: Forced OAuth profile linking

This lab gives you the option to attach a social media profile to your account so that you can log in via OAuth instead of using the normal username and password. Due to the insecure implementation of the OAuth flow by the client application, an attacker can manipulate this functionality to obtain access to other users' accounts.

To solve the lab, use a [CSRF attack](https://portswigger.net/web-security/csrf) to attach your own social media profile to the admin user's account on the blog website, then access the admin panel and delete Carlos.

The admin user will open anything you send from the exploit server and they always have an active session on the blog website.

You can log in to your own accounts using the following credentials:

- Blog website account: `wiener:peter`
- Social media profile: `peter.wiener:hotdog`

## Analysis

After analyzing the functionalities of application we know that application allows us linked social media profile to our account.

![](https://i.imgur.com/E3i3cTa.png)

This functionality use Authorization code grant type

```http
https://oauth-0ac2005103e1983dc1be8df5026e00ba.oauth-server.net/auth?client_id=j99bj1f7u3r6t14alfnto&
redirect_uri=https://0afd0038030a986ac1518f5000570095.web-security-academy.net/oauth-linking&
response_type=code&
scope=openid profile email
```

But it don't have param `state` (Stores a unique, unguessable value that is tied to the current session on the client application. The OAuth service should return this exact value in the response, along with the authorization code. This parameter serves as a form of CSRF token for the client application by making sure that the request to its /callback endpoint is from the same person who initiated the OAuth flow.)

After sending the request we will be redirecting to the `/oauth-linking` page with parameter `code` like that:

`https://0afd0038030a986ac1518f5000570095.web-security-academy.net/oauth-linking?code=XKcSLuk-fN_Q9_NT_iRQLsfMcvT_JTNhGZbCfciKnXP`

Seem the the OAuth provider give us that `code` to link our social media account, which is authenticated by OAuth provider with account logged in with that session.

![](https://i.imgur.com/6c0z07M.png)

## Exploit

Based on that, to set up social media account of administration to our account. We must make admin access that page with his cookie but the code parameter is ours.

So that, we turn on intercept and forward request to OAuth provider to receive the code parameter, copy that code parameter and drop that request to make sure that the code is valid.

![](https://i.imgur.com/PEsrQsR.png)

`https://0a5c007903f7518cc11f7c1d003e0019.web-security-academy.net/oauth-linking?code=hL9JWzdSTX7NnhI9gtCjdwkkzCgcW-pn3vRQM0TcFPF`

Go to the exploit server and create payload:

```html
<script>
window.location.href ='https://0a5c007903f7518cc11f7c1d003e0019.web-security-academy.net/oauth-linking?code=hL9JWzdSTX7NnhI9gtCjdwkkzCgcW-pn3vRQM0TcFPF';
</script>
```

Storing the payload and delivering it to victim (administrator).

Back to my account and log out and then login back but this time we will login with social media account

![](https://i.imgur.com/Lqazt5z.png)

As seen above, our social media account has been linked to administrator account.

To solve this lab, access `/Admin panel` page and delete the user carlos.

