# 🦊 Kitsune

Kitsune is a tool for generating randomized substitution cipher fonts, useful for bypassing static analysis for red team/penetration testing engagements. Scanners will see random ASCII characters, but clients will render human-readable text.

### Installation

```console
$ git clone https://github.com/disasterbyte/kitsune.git && cd kitsune
$ pip install .
```

### Usage

```console
$ kitsune <filename> [text]
```

You can generate a cipher font from an existing TrueType file, which will create `output.ttf` and `output.ttx` files. Optionally, provide a string of text to convert to ciphertext.

```console
$ kitsune Roboto.ttf -c "Click here to reset your password"
[+] Loading source font...
[+] Generating .ttx file...
[+] Generating .ttf file...

KsbEu mfJf LZ JfpfL YZTJ iCpphZJw
```

You can generate ciphertex from an existing Kitsune `.ttx` file, providing a string as a command-line argument.

```console
$ kitsune output.ttx -c "Creating more ciphertext"

KJfCLbgB RZJf EbimfJLfAL
```

