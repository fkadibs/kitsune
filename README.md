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

Specify a TrueType file to generate an `output.ttf` file. Optionally, provide a string of text to convert to ciphertext.

### Example

```console
$ font-cipher.py Roboto.ttf "Click here to reset your password"
[+] Loading file...
[+] Applying substitutions...
[+] Writing to disk...
[+] Ciphertext:
sVSQI KEBE WX BENEW dXrB tvNNbXBe
```
