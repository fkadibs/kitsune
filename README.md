# Font-Cipher
This is a PoC that generates a randomized substitution cipher font that can be used to bypass static analysis for red team/penetration testing engagements. Static analysis scanners will see random ASCII characters, but clients will render human-readable text.

### Installation

```console
$ pip install -r requirements.txt
```

### Usage

```console
$ font-cipher.py <filename> [text]
```

You can create a cipher font by specifying a TrueType file, generating `output.ttf` and `output.ttx` files. Optionally, provide a string of text to convert to ciphertext.

```console
$ font-cipher.py Roboto.ttf "Click here to reset your password"
[+] Loading source font...
[+] Generating .ttx file...
[+] Generating .ttf file...

KsbEu mfJf LZ JfpfL YZTJ iCpphZJw
```

You can generate ciphertex from an existing cipher font directly from the `.ttx` file, providing a string as a command-line argument.

```console
$ font-cipher.py output.ttx "Creating more ciphertext"

KJfCLbgB RZJf EbimfJLfAL
```

