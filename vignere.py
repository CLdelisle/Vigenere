#!/usr/bin/env

'''
A keyed Vignere tool

Python version 2.7

Colby DeLisle
2016
'''

# EVERY LETTER IS UPPERCASE

import argparse
from collections import OrderedDict

def alpha_to_num(char):
	result = ord(char) - 65
	if (result < 0 or result > 25):
		return -1
	else:
		return result

def num_to_alpha(int):
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


def remove_duplicates(list):
	return OrderedDict.fromkeys(''.join(list)).keys()


def generate_alphabet(key): # takes key as a STRING
	alphabet = list(key)
	for i in range(26):
		alphabet.append(num_to_alpha(i))

	return remove_duplicates(alphabet)

def cyclic_shift(alphabet, offset):
	nums = [alpha_to_num(letter) for letter in alphabet]
	nums = [(n + offset)%26 for n in nums]
	return [num_to_alpha(n) for n in nums]

def tile_keyword(keyword):
	key = list(keyword)
	num_tiles = (26/len(key)) + 1
	for i in range(num_tiles):
		key = key + key
	return key[:26]


parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using a keyed Vignere cipher.")
parser.add_argument('-c', '--cryptmode', choices=['encrypt','decrypt'], default='encrypt')
parser.add_argument('message', help="the message to encrypt or decrypt")
parser.add_argument('alphakey', help="the key with which to generate the alphabet")
parser.add_argument('keyword', help="the keyword with which to generate tabula recta")

args = parser.parse_args()

message = str(args.message).upper()
alphakey = str(args.alphakey).upper()
keyword = str(args.keyword).upper()

alphabet = generate_alphabet(alphakey)

regular_alphabet = generate_alphabet("")

print tile_keyword(keyword)
print len(tile_keyword(keyword))
print len(alphabet)

shifted = cyclic_shift(alphabet, 1)



