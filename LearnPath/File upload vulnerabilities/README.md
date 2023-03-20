# File upload vulnerabilities

## What are file upload vulnerabilities?

File upload vulnerabilities are when a web server allows users to upload files to its filesystem without sufficiently validating things like their name, type, contents, or size. Failing to properly enforce restrictions on these could mean thateven a basic image upload function can be used to upload arbitrary and potentially dangerous files instead. This could even include server-side script files that enable remote code execution.


## Some examples about file upload vulnerabilities at above :+1:

![](https://i.imgur.com/S1qNcga.png)

## The impact of file upload vulnerabilities

- Remote Code Execution: The most harmful outcome. If the web server configuration allows, an attacker can try to e.g. upload a web shell which enables him to pass on terminal commands to the server running the application. These commands can then be easily sent to the server via the browser.

- Denial of Service: If the application code is not validating file size or the number of files uploaded, an attacker could try to fill up the server’s storage capacity until a point is reached, where the application cannot be used anymore.

- Web Defacement: If the web root is not configured properly (allowing an attacker to overwrite existing files), an attacker could substitute existing web pages with his own content (potentially showing imagery which is conflicting to the original purpose of the application)

-Phishing Page: Similar to the example before, an attacker could also go ahead only slightly manipulate an existing page in order to e.g. extract sensitive data, sending it to a destination controlled by himself.


## How to prevent file upload vulnerabilities

Various techniques exist to prevent file upload vulnerabilities from causing harm to your system. Typically, it is recommend to use a defense-in-depth approach utilising multiple of the prevention strategies below:

- Implement allow-list containing only the file types which are really necessary for the proper functioning of the web app

- Restrict file size to a certain limit

- Create new file names for all uploaded files or remove all potentially dangerous characters (such as control characters, special characters and Unicode characters)

- Use existing well-tested validation frameworks for file uploads

-  Remove EXIF data from uploaded files

- Host uploaded files on a separate domain from the main application (in order to obtain protection through the same-origin-policy during potential Javascript execution)