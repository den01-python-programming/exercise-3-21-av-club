# Exercise 3.21 AV Club

Write a program that reads user input until an empty line. For each non-empty string, the program splits the string by spaces ` ` and then prints the pieces that contain `av`, each on a new line.

```plaintext
**java is a programming language**
java
**navy blue shirt**
navy
```

```plaintext
**Do you have a favourite flavour**
have
favourite
flavour
**was it a cat?**
**bye**
```

Tip! Strings have an `in`-method, which tells if a string contains another string. It works like this:

```python
text = "physiotherapist"

if "other" in text:
    print("other was found")

if not "scott" in text:
    print("scott wasn't found")
```

```plaintext
other was found
scott wasn't found
```
