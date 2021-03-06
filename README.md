# Keyed Vigenére Cipher

Command line tool to encrypt or decrypt a message using a particular type of keyed Vigenére cipher. Works given some alphabet key and passphrase.

usage: vigenere.py [-h] [-c {encrypt,decrypt}] [-v] message alphakey keyword

Encrypt or decrypt a message using a keyed Vignere cipher.

<b>positional arguments</b>

  message:               the message to encrypt or decrypt
  
  alphakey:              the key with which to generate the alphabet
  
  keyword:               the keyword with which to generate tabula recta and
                        the lookup table


<b>optional arguments</b>

  -h, --help            show this help message and exit
  
  -c {encrypt,decrypt}, --cryptmode {encrypt,decrypt}
  
  -v                    verbose mode: prints tabula recta and lookup table
  

#Examples 
By default, "decrypt" mode is enabled, and verbose mode is off. A sample of input/output is:
![Sample](/img/k1.png "Sample")

With verbose mode enabled, the input
![Sample verbose input](/img/k2_input.png "Sample verbose input")
results in:
![Sample verbose output](/img/k2_output.png "Sample verbose output")
