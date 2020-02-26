# Font-Cipher
This is a PoC that generates a randomized substitution cipher font that can be used to bypass static analysis for red team/penetration testing engagements. Static analysis scanners will see random ASCII characters but, the text will render as a human-readable string in the client.

### Installation

```console
$ pip install -r requirements.txt
```

### Usage

```console
$ font-cipher.py <filename> [text]
```

You can create a cipher font by specifying a TrueType file, generating `output.ttf` and `output.ttx` files. Optionally, provide a string of text to convert to ciphertext. You can generate ciphertex from a cipher font by specifying a `.ttx` file and providing a string as a command-line argument.

### Examples

```console
$ font-cipher.py Roboto.ttf "Click here to reset your password"
[+] Loading file...
[+] Applying substitutions...
[+] Writing to disk...

KeYsR NMHM vE HMrMv VEwH QGrrXEHU
```

```console
$ font-cipher.py output.ttx "Creating more ciphertext"

KHMGvYIp oEHM sYQNMHvMCv
```


