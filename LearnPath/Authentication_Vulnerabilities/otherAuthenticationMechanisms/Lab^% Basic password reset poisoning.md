# Lab: Basic password reset poisoning

This lab is vulnerable to password reset poisoning. The user `carlos` will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account.

You can log in to your own account using the following credentials: `wiener:peter`. Any emails sent to this account can be read via the email client on the exploit server. 

## Solution

Same previous lab, the application has functionality to reset password. To reset password you need to submit a username or email address to determine, what user want to reset password and then the application will send an email containing reset password token to the user that allowed to reset password of the user.

To solve this lab we need steal that reset password token, which allows the user (`carlos`) to reset password and get this reset password token reset password according to our will.

According to the description, user carlos carelessly clicked on any link in the email he received. So we'll send him a fake email, which can steal his reset password token.

Because the URL that is sent to the user is dynamically generated based on controllable input, such as the Host header, it may be possible to construct a password reset poisoning attack:

- Turn on Intercept and send a forgot password request with username carlos, change Host header to our IP address, which under our control and then forward that request.

    ![](https://i.imgur.com/9WUjfM2.png)

- At this time, the user carlos is receiving an url to reset password contain the valid reset password token that is associated with their account. However, the domain name in the URL points to the our server: `https://our-server.net/reset?token=0a1b2c3d4e5f6g7h8i9j`

    ![](https://i.imgur.com/6bpgZSX.png)

- If the user carlos clicks this link (or it is fetched in some other way, for example, by an antivirus scanner) the reset password token will be delivered to the our server. 

    ![](https://i.imgur.com/HJoPaBz.png)

- Now we can use that reset password token to reset the carlos's password according to our will.

    ![](https://i.imgur.com/GlqLjoY.png)

Login with new password to solve this lab.