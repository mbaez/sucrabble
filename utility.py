#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Utility functions module.
'''
import constants
import re
import os

def get_unicode(data):
	if not isinstance(data, unicode):
		return unicode(data, "utf-8")
	return data
	

def create_board(size):
	board = []
	for i in range(0, size):
		row = []
		for j in range(0, size):
			row.append("")
		board.append(row)
	
	return board
	

def get_letters_from_file(lenguage = constants.DEFAULT_LENGUAGE):
	letters = {}
	letters_path = os.path.join(constants.LENGUAGES_PATH, lenguage, 
								"letters.txt")
	letters_path =  os.sep + letters_path
	file = open(letters_path, "r")
	list = file.readlines()
	# format "Letter": (count, score)
	pattern = re.compile(r".(?P<letter>[\w\s]+).: .(?P<count>\d+),(?P<score>\d+).")
	
	for i in list:
		m = pattern.match(i)
		if m:
			info = (m.group('count') , m.group('score'))
			letters[m.group('letter')] = (int(info[0]) , int(info[1]))	
	
	return letters
	
	
def get_dictionary(lenguage = constants.DEFAULT_LENGUAGE):
	''' Get the dictionary used in the Game
	
		@param lenguage: the lenguage.
		@return: a list containing the dictionary.
	'''
	file_name = "dict-" + lenguage + ".txt" 
	dict_path = os.path.join(constants.DICTIONARIES_PATH, file_name)
	dict_path = os.sep + dict_path 
	file = open(dict_path, "r")
	dict = file.readlines()
	return dict

def search_word(word, dict,lenguage = constants.DEFAULT_LENGUAGE):
	''' Look for the specified word in the dictionary 
	
		@param lenguage: the lenguage.
		@param word: word to look for
		@param dict: the dictionary.
		@return: True or False
	'''
	l2 = filter(lambda n: re.match(word, capitalize_word(n)), dict)
	if not l2:
		return False
	return True

def can_form_a_word(board, letters,letter, posx, posy):
	''' Check if the given letter can be used to form a new word
		on the board.
		
		@param board: the gameboard
		@param letters: the list of letters to use.
		@param letter: the letter at [row][column] on the board
		@param posx: x-possition [row]
		@param posy: y-possition [column]
		@return: A tuple containing a regular expresion to use as a 
				pattern to search in the dictionary and the type of 
				the given letter. The possible types are:
					- First letter of the word
					- Middle letter.
					- Last letter.
	'''
	# implementar...

def search_words_that_match(criterion, dict):
	''' Look for words in the dictionary that match with the given
		pattern
		
		@param criterion: the pattern
		@param dict: the dictionary
		@return: the list of words that matched				
	'''
	pattern = re.compile(criterion)
	l = filter(lambda n: pattern.match(capitalize_word(n)), dict)
	return l
	
	
def capitalize_word(word):
	''' capitalize all the letters in the given word.
		
		@param word: the word
		@return: the word capitalized.
	'''	
	x = word
	x = x.replace('á', 'a')
	x = x.replace('é', 'e')
	x = x.replace('í', 'i')
	x = x.replace('ó', 'o')
	x = x.replace('ú', 'u')
	x = x.swapcase()
	return x
	
	
