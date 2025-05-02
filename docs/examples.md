### Input/Output Examples

- String input:
```shell-session
ciphr '"abc"' hex
# Output: 616263
```

- File input:
```shell-session
ciphr @input.txt base64
```

- Stdin with custome output:
```shell-session
echo -n "abc" | ciphr - sha1 --output hex
# Output: a9993e364706816aba3e25717850c26c9cd0d89d
```