
class User:
		def __init__(self, bag):
			''' Initialize the Computer class.   
			@param bag: the bag with letters.
			'''
			self.__letters = bag.remove_letters()
			
		def get_letters(self):
			''' Return the list of Letters.
			@return: the list of elements.
			'''
			return self.__letters

		def letters_length(self):
			''' Return the length of the list of Letters.
						
						@return: the number of elements.
			'''
			return len(self.__letters)

		def get_letter_at(self, index):
			''' Get the letter at the specified index of the list.
						
				@param index: the index
				@return: the Letter
			'''
			return self.__letter[index]

		def add_letter(self, letter):
			''' Add a new Letter to the list of Letters.
						
			@param letter: the new Letter.
			'''
			self.__letters.append(letter)
