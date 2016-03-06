# Keyed Vigenére Cipher Solver

Command line tool to encrypt or decrypt a message using a particular type of keyed Vigenére cipher. Works given some alphabet key and passphrase.

usage: vigenere.py [-h] [-c {encrypt,decrypt}] [-v] message alphakey keyword

Encrypt or decrypt a message using a keyed Vignere cipher.

positional arguments:
  message               the message to encrypt or decrypt
  alphakey              the key with which to generate the alphabet
  keyword               the keyword with which to generate tabula recta and
                        the lookup table

optional arguments:
  -h, --help            show this help message and exit
  -c {encrypt,decrypt}, --cryptmode {encrypt,decrypt}
  -v                    verbose mode: prints tabula recta and lookup table
  

#Examples 

![Sample output](/k2_output.png "Sample output")
