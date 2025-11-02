# Ciphr Examples

## Basic Functions

### Hex Encoding/Decoding

The `hex` and `~hex` functions convert data between binary and hexadecimal representations.

1. Encoding to hex:
```shell-session
# String input to hex
ciphr '"Hello"' hex
# Output: 48656c6c6f

# File content to hex
ciphr @input.txt hex
# Output: (hex representation of file contents)

# Stdin to hex
echo -n "Hello" | ciphr - hex
# Output: 48656c6c6f
```

2. Decoding from hex:
```shell-session
# Hex string to original
ciphr '"48656c6c6f"' ~hex
# Output: Hello

# Decode hex file
ciphr @hexdata.txt ~hex > original.txt

# Decode hex from stdin
echo -n "48656c6c6f" | ciphr - ~hex
# Output: Hello
```

3. Chaining with other functions:
```shell-session
# Convert string to hex, then to base64
ciphr '"Hello"' hex base64
# Output: NDg2NTZjNmM2Zg==

# Decode base64, then decode hex
ciphr '"NDg2NTZjNmM2Zg=="' ~base64 ~hex
# Output: Hello
```

## Other Examples

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

- Stdin with custom output:
```shell-session
echo -n "abc" | ciphr - sha1 --output hex
# Output: a9993e364706816aba3e25717850c26c9cd0d89d
```