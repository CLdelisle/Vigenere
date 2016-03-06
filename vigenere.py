#!/usr/bin/env

'''
A keyed Vigenere tool

Python version 2.7

Colby DeLisle
2016
'''

version = '0.1'
# first iteration - decrypt functionality enabled

import argparse
from collections import OrderedDict, deque

#--------------------------------------------------------------------------------

def alpha_to_num(char):
	""" Get integer value of a letter """
	result = ord(char) - 65
	if (result < 0 or result > 25):
		return -1
	else:
		return result

def num_to_alpha(int):
	""" Get character corresponding to an int """
	if   int == 0:
		return 'A'
	elif int == 1:
		return 'B'
	elif int == 2:
		return 'C'
	elif int == 3:
		return 'D'
	elif int == 4:
		return 'E'
	elif int == 5:
		return 'F'
	elif int == 6:
		return 'G'
	elif int == 7:
		return 'H'
	elif int == 8:
		return 'I'
	elif int == 9:
		return 'J'
	elif int == 10:
		return 'K'
	elif int == 11:
		return 'L'
	elif int == 12:
		return 'M'
	elif int == 13:
		return 'N'
	elif int == 14:
		return 'O'
	elif int == 15:
		return 'P'
	elif int == 16:
		return 'Q'
	elif int == 17:
		return 'R'
	elif int == 18:
		return 'S'
	elif int == 19:
		return 'T'
	elif int == 20:
		return 'U'
	elif int == 21:
		return 'V'
	elif int == 22:
		return 'W'
	elif int == 23:
		return 'X'
	elif int == 24:
		return 'Y'
	elif int == 25:
		return 'Z'
	else:
		return ''

#--------------------------------------------------------------------------------

def remove_duplicates(list):
	""" Remove all but first occurences of letters in a list """
	return OrderedDict.fromkeys(''.join(list)).keys()

def first_occurrence(alphabet, char):
	""" Get index of first occurence of char in alphabet (list) """
	return alphabet.index(char)

def rotate_right(alphabet, offset):
	""" Rotate a list right by offset (int) """
	d = deque(alphabet)
	d.rotate(offset)
	return list(d)

def rotate_left(alphabet, offset):
	""" Rotate a list left by offset (int) """
	d = deque(alphabet)
	d.rotate(-offset)
	return list(d)

#--------------------------------------------------------------------------------

def generate_alphabet(key):
	""" Generate modified alphabet from a given alphakey """
	alphabet = list(key) # takes key as a STRING
	for i in range(26):
		alphabet.append(num_to_alpha(i))

	return remove_duplicates(alphabet)

def generate_lookup_table(alphabet, keyword):
	""" Generates dictionary used to translate between plaintext & ciphertext """
	key = list(keyword)
	lookup = {}
	for i in range(len(key)):
		lookup[i] = rotate_left(alphabet, alphabet.index(key[i]))

	return lookup

def print_tabula_recta(alphabet):
	""" Prints tabula recta generated by alphabet """
	for i in range(26):
		print rotate_left(alphabet,i)

def print_lookup_table(alphabet, keyword):
	""" Prints the lookup table generated from a modified alphabet and a keyword """
	print alphabet
	for i in range(len(keyword)):
		index = first_occurrence(alphabet,keyword[i])
		print(rotate_left(alphabet,index))

#--------------------------------------------------------------------------------

def decrypt_letter(alphabet, lookup_table, char, index):
	""" Decrypt a single letter
	alphabet - the global alphabet set by the alphakey
	lookup_table - the table generated by the alphakey and keyword
	char - the ciphertext character to decrypt
	index - current state of iteration through the keyword
	"""
	if(0 <= alpha_to_num(char) < 26):
		shifted_alphabet = lookup_table[index]
		n = shifted_alphabet.index(char)
		return alphabet[n]
	else:
		return char

def decrypt(message, alphakey, keyword, verbose):
	""" Decrypt logic 
	Returns plaintext characters as list
	"""
	alphabet = generate_alphabet(alphakey) # Create alphabet generated by alphakey
	lookup = generate_lookup_table(alphabet,keyword)
	message_chars = list(message)
	ciphertext_chars = []
	key_length = len(list(keyword))

	i = 0
	for m in message_chars:
		ciphertext_chars.append(decrypt_letter(alphabet, lookup, m, i))
		if(0 <= alpha_to_num(m) < 26):
			i = (i + 1) % key_length

	if verbose:
		print ''
		print "Tableau:"
		print_tabula_recta(alphabet)
		print ''
		print "Lookup table:"
		print_lookup_table(alphabet, list(keyword))

	return ciphertext_chars

def encrypt():
	""" Encrypt logic """
	pass
	# To be implemented

#================================================================================

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using a keyed Vignere cipher.")
	parser.add_argument('message', help="the message to encrypt or decrypt")
	parser.add_argument('alphakey', help="the key with which to generate the alphabet")
	parser.add_argument('keyword', help="the keyword with which to generate tabula recta and the lookup table")
	parser.add_argument('-c', '--cryptmode', choices=['encrypt','decrypt'], default='decrypt')
	parser.add_argument('-v', action='store_true', default=False, help="verbose mode: prints tabula recta and lookup table")

	args = parser.parse_args()

	message = str(args.message).upper()
	alphakey = str(args.alphakey).upper()
	keyword = str(args.keyword).upper()
	mode = args.cryptmode
	verbose = args.v

	if(mode == 'encrypt'):
		pass
		# To be implemented

	else: #decrypt
		plaintext_chars = decrypt(message, alphakey, keyword, verbose)
		print ''
		print "Decrypted plaintext:"
		print ''.join(plaintext_chars)
		print ''

#=============================================================================END

