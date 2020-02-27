# 🦊 Kitsune

Kitsune generates randomized substitution cipher fonts, useful for bypassing static analysis for red team/penetration testing engagements. Scanners will see random ASCII characters, but clients will render human-readable text.

### Installation

```console
$ git clone https://github.com/disasterbyte/kitsune.git && cd kitsune
$ pip install .
```

### Usage

```console
$ kitsune -h
usage: kitsune [-h] [-c TEXT] [-o FILE] [-w] filename

positional arguments:
  filename    input filename

optional arguments:
  -h, --help  show this help message and exit
  -c TEXT     generate ciphertext
  -o FILE     output file name
  -w          generate woff2 webfont
```

Generate a cipher font from an existing TrueType file, which will create `output.ttf` and `output.ttx` files. Optionally, you can specify an output filename or provide a string of text to convert to ciphertext.

```console
$ kitsune Roboto.ttf -o example -c "Click here to reset your password"
[+] Loading source font...
[+] Generating example.ttx file...
[+] Generating example.ttf file...

KsbEu mfJf LZ JfpfL YZTJ iCpphZJw
```

Generate ciphertex from an existing Kitsune `.ttx` file, providing a string as a command-line argument.

```console
$ kitsune example.ttx -c "Creating more ciphertext"

KJfCLbgB RZJf EbimfJLfAL
```

