# 🦊 Kitsune

Kitsune is a tool for generating randomized substitution cipher fonts that can be used to bypass static analysis for red team/penetration testing engagements. Static analysis scanners will see random ASCII characters, but clients will render human-readable text.

### Installation

```console
$ git clone https://github.com/disasterbyte/kitsune.git && cd kitsune
$ pip install .
```

### Usage

```console
$ kitsune <filename> [text]
```

You can create a cipher font by specifying a TrueType file, generating `output.ttf` and `output.ttx` files. Optionally, provide a string of text to convert to ciphertext.

```console
$ kitsune Roboto.ttf "Click here to reset your password"
[+] Loading source font...
[+] Generating .ttx file...
[+] Generating .ttf file...

KsbEu mfJf LZ JfpfL YZTJ iCpphZJw
```

You can generate ciphertex from an existing cipher font directly from the `.ttx` file, providing a string as a command-line argument.

```console
$ kitsune output.ttx "Creating more ciphertext"

KJfCLbgB RZJf EbimfJLfAL
```

