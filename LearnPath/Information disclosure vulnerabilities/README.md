# Information disclosure vulnerabilities

## What is information disclosure?

Also known as information leakage, the vulnerabilities occur when developers, designer failure to remove, config, design the sensitive data like:
- Data about other users, such as usernames or financial information
- Sensitive commercial or business data
- Technical details about the website and its infrastructure

Depending on that, the attacker can potentially be a starting point for exposing an additional attack surface

## Some examples about information disclosure vulnerabilities at above :+1:

![](https://i.imgur.com/rfu7Ps5.png)

## How to prevent information disclosure vulnerabilities

- Make sure that everyone involved in producing the website is fully aware of what information is considered sensitive
- Audit any code for potential information disclosure as part of your QA or build processes. It should be relatively easy to automate some of the associated tasks, such as stripping developer comments.
- Use generic error messages as much as possible. Don't provide attackers with clues about application behavior unnecessarily.
- Double-check that any debugging or diagnostic features are disabled in the production environment.
- Make sure you fully understand the configuration settings, and security implications, of any third-party technology that you implement. Take the time to investigate and disable any features and settings that you don't actually need.