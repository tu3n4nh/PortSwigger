# Directory traversal

## What is Directory traversal

Also know as path traversal, that vulnerability allows attacker to access arbitrary files on the web server to read, write, modify and delete ones. In some cases, the attacker can take full control of the server.

## Some examples about directory traversal at above

## Prevent directory traversal

```java
File file = new File(BASE_DIRECTORY, userInput);
if (file.getCanonicalPath().startsWith(BASE_DIRECTORY)) {
    // process file
}
```


