#!/usr/bin/env python

import utility
import constants

class Letter:
    ''' Letter class. Represents a letter on the gameboard.
    '''
    def __init__(self, character = "", score = 0):
        ''' Initialize the letter
            @param character: The string representing the letter.
        '''
        self.__score = score
        self.__is_blank = False
        self.set_character(character)
    
    
    
    def set_character(self, character):
        ''' Set the letter string
           
            @param character: the new letter string value   
        '''
        if(character == " "):
            self.__is_blank = True
        self.__character = character
    
    def set_is_blank(self, is_blank):
        ''' Set is_blank property of the letter
        
            @param is_blank: True or False.
        '''
        self.__is_blank = is_blank
    
    def set_score(self, score):
        ''' Set the score of the letter.
        
            @param score: the new score value of the letter.
        '''
        self.__score = score
    
    def get_character(self):
        ''' Get the letter string
        
            @return: the string representation of this letter.
        '''
        return self.__character
    
    def get_score(self):
        ''' Get the letter score.
        
            @return: the score of this letter.
        '''
        if(self.is_blank()):
            return 0
        return self.__score
    
    def is_blank(self):
        ''' Check if the letter is blank
        
            @return: True if the letter is a blank letter.
        '''
        return self.__is_blank
        
    def __eq__(self, other):
        ''' Check if this Letter equals another Letter
        
            @param other: Other letter
            @return: True if the Letter strings are the same
        '''
        if(isinstance(other, Letter)):
            a = utility.get_unicode(self.get_character())
            b = utility.get_unicode(other.get_character())
            if a == b:
                return True
            elif ((a != b) and (self.is_blank() == True and other.is_blank() == True)):
                return True
        return false
    
    def __neq__(self, other):
        ''' Check if this Letter does not equal another Letter
        
            @param other: Other letter
            @return: True if the Letter strings are not the same
        '''
        if(isinstance(other, Letter)):
            if(self == other):
                return False
        return True
    
    def __repr__(self):
        ''' Return a string formatted as follow:
            Letter_String: Score
            
            @return: string representation of this Letter.
        '''
        return self.get_character() + ": "+str(self.get_score()) 


class Board:
    ''' Board class. Represents the gameboard.
    '''
    def __init__(self, size = constants.DEFAULT_BOARD_SIZE):
        ''' Initialized the board
            
            @param size: the size of this board. For example 15x15
        '''
        
        self.__size = size
        self.__board = utility.create_board(size)
    
    def get_size(self):
        ''' get the size of this board
        
            @return: the size.
        '''
        return self.__size
    
    def set_size(self, size):
        ''' set the size value of this board
        
            @param: the new size value.
        '''     
        self.__size = size
        
        
    def get_value_at(self, row, column):
        ''' Get the value at the specified position [row][column] on the
            board.
            
            @param row: row on the board
            @param column: column on the board          
            @return: The value at the specificied position.
        '''
        return self.__board[row][column]
    
    def set_value_at(self, value, row, column):
        ''' Set the value at the specified position [row][column] on the
            board.
            
            @param value: new value
            @param row: row on the board
            @param column: column on the board
        '''     
        self.__board[row][column] = value
        
    def get_tile_style(self, row, column):
        ''' Get the style of the tile  at the specified position 
            [row][column] on the board.
            
            @param row: row on the board
            @param column: column on the board          
            @return: The style of the tile at the specificied position.
        '''
        # implementar....
    
    def get_tile_score(self, row, column):
        ''' Get the score of the tile  at the specified position 
            [row][column] on the board.
            
            @param row: row on the board
            @param column: column on the board          
            @return: The score of the tile at the specificied position.
        '''
        # implementar....
    
    def is_tile_empty(self, row, column):
        ''' Check if the tile is empty  at the specified position 
            [row][column] on the board.
            
            @param row: row on the board
            @param column: column on the board          
            @return: True or False
        '''
        return  (self.get_value_at(row, column) == "")
    
        
        


class Move:
    ''' Move class represents a move made by a player.
        The Move is a list of tuples containing 
        (letter, x-position, y-position) for all Letters in the Move.   
    ''' 
    def __init__(self, move = None):
        self.__score = 0
        self.__move = []
        self.__has_blank = False
        if move != None:
            for l, x, y in move:
                self.add_move(l, x ,y)
    
    def has_blank(self):
        '''
        Check whether this Move contains a blank letter
        
        @return: True if this Move contains a blank Letter
        ''' 
        return self.__has_blank
        
    def add_move(self, letter, x, y):
        ''' Add a new move
            
            @param letter: the Letter
            @param x: x-position on the board
            @param y: y-position on the board
        '''
        if not self.has_blank():
            self.__has_blank = letter.is_blank()
        move.append((letter, x , y))
    
    def remove_move(self, letter, x, y):
        ''' Remove move
            
            @param letter: the Letter
            @param x: x-position on the board
            @param y: y-position on the board
        '''
        self.move.remove((letter,x,y))

    def get_score(self):
        ''' Get the score for the move
            
            @return: the score for the move
        '''
        return self.__score
    
    def set_score(self, score):
        ''' Set the score 
            
            @param score: the score 
        '''     
        self.__score = score
    
    def length(self):
        '''
        Get number of tuples in the Move.
        
        @return: Number of tuples in the move.
        '''
        return len(self.move)
    
    def clear(self):
        ''' Clear the move '''
        move = []
    
    def get_move(self, index):
        ''' Get the Move at the specified index
        
            @param index: index
            @return: the Move at the specified index
        '''
        return move[index]
        
    def get_moves(self):
        ''' Get the list of moves
        
            @return: the list of  moves
        '''
        return self.__move  
    
    def get_first_move(self):
        ''' Get the first move'''
        return get_move(0)
        
    def is_valid(self, dictionary):
        ''' Check whether this move is valid, that is
            form the word and look if it exists in the dictionary
            
            @param dictionary: the dictionary
            @return: True if the move is valid, otherwise False
        '''
        word = self.word_to_play()
        if self.is_horizontal() or self.is_vertical():
            if utility.search_word(word, dictionary):
                if self.has_common_tile(len(word), board):
                    if verify_words(board):
                        return True
                    else
                        return False
                else
                    return True
            else
                return False
        else
            return False

    
    def is_horizontal(self):
        ''' Check whether the Move is horizontal.
        
            @return: True if all Letters in the move are arranged horizontally.
        '''     
        if self.is_empty():
            return False
            
        l, x, y = get_first_move()
        if not is_empty():
            for _l, _x, _y in self.get_moves():
                if _x != x:
                    return False
            return True
        
    
    def is_vertical(self):
        ''' Check whether the Move is vertical.
        
            @return: True if all Letters in the move are arranged vertically.
        '''     
        if self.is_empty():
            return False
        
        l, x, y = get_first_move()
        if not is_empty():
            for _l, _x, _y in self.get_moves():
                if _y != y:
                    return False
            return True
    
    def calculate_score(self):
        ''' Calculates the score for the move
            
            @return : the score for the move.
        '''
        # implementar....
        
    def isEmpty(self):
        ''' Check whether the Move is empty
        
            @return: True if the Move has no Letters in it.
        '''
        
        return self.length() == 0
    
    def try_move(self, board, word, type, row, column):
        ''' Try to insert the given word into the board.
        
            @param board: the gameboard
            @param word: the word to insert
            @param type: the type of the letter, see the 
            utility.can_form_a_word function.
            @param row: the row in the gameboard.
            @param column: the column in the gameboard.
            @return: True if it is possible and also valid to insert 
            the given word into the gameboard, otherwise False.
        '''
        # implementar....

    
    def word_to_play(self):
        ''' To form the word from the move object 
        
            @return: Word that this Move spells
        '''

        word = ""
        for letter in self.get_moves():
                word += letter.get_character()
        return word
    

    def has_common_tile(self, l, board):
        '''
        Check to see if this move has a common tile with another word in the board
        
        @param board: the board that contains the words
        @param l: the length of the word
        @return: True if this Move has a letter,x,y tile in common
        '''
        LETTER = 0
        ROW = 1
        COL = 2
        row_in = self.get_move(0)[ROW]
        col_in = self.get_move(0)[COL]

        row_fi = self.get_move(l - 1)[ROW]
        col_fi = self.get_move(l - 1)[COL]

        if self.is_horizontal():
            flag = True
            j = col_in
            while j >= col_in and j <= col_fi and flag = True:
                if board.get_value_at(row_in, j) == " ":
                    flag = False
                j += 1

            #if flag == True:
            #the word has a tile in common, so the move is ok
            #    return True
            #else:
            #the word hasn't a tile in common, so try another move
            #    return False
            return flag
    
        if self.is_vertical():
            flag = True
            i = row_in
            while i >= row_in and i <= row_fi and flag = True:
                if board.get_value_at(i, col_in) == " ":
                    flag = False
                i += 1

            #if flag == True:
            #the word has a tile in common, so the move is ok
            #    return True
            #else:
            #the word hasn't a tile in common, so try another move
            #    return False
            return flag

    def verify_words(self, board):
        ''' 
            Check if the gameboard has corret words

            @param board: the gameboard with the words 
        '''

        words = " "

    #verify if the rows have correct words
        for i in range(0,board.get_size()):
            for j in range(0, board.get_size()):
                word += str(board.get_value_at(i, j))
             
            list_words = words.split()
            for word in list_words:
                if not utility.search_word(word, dictionary):
                    return False
            words = " "

    #verify if the cols have correct words
        for j in range(0, board.get_size()):
            for i in range(0, board.get_size()):
                words += str(board.get_value_at(i, j))
            list_words = words.split()
            for word in list_word:
                if not utility.search_word(word, dictionary):
                    return False
            words = " "

        return True

    def first_move(self, board):
        middle = (board.get_size() + 1) / 2
        if board.get_value_at(middle, middle) != " ":
                    return True
        return False                
        
        
        
class Bag:
    ''' Bag represents a "Bag" of Letters. It contains a dictionary
        named __bag_letters, formatted as follow
        {"Letter" : (count, score)}
    ''' 
    def __init__(self, lenguage= constants.DEFAULT_LENGUAGE):
        self.__bag_letters = {}
        self.__bag_letters = utility.get_letters_from_file(lenguage)
        
        
    
    def remove_letters(self, amount = constants.DEFAULT_AMOUNT_LETTERS):
        ''' Removes Letters from the bag
            
            @param size: the amount of Letters that are going to be removed
            @return: the letters removed.
        '''
        # format "letter": (count, score)
        
        n = self.amount_letters_in_bag()
        
        # if amount > n just remove the n letters in the bag.
        if n > 0 and amount > n:
                amount = n
        elif n == 0
            return -1
                
        removed = []
        i = 0
        while i < amount:
            for key, data in self.get_bag_letters().items():
                if random.randint(0 , 1) and i < amount:
                    if data[0] > 0:
                        removed.append(Letter(key, data[1]))
                        self.get_bag_letters()[key] = (data[0] - 1, data[1])
                        i += 1
        return removed
        

    def add_letters(self, letters):
        ''' Add letters to the bag
            
            @param letters: the list of Letters that are going to be added
        '''     
        for l in letters:
            count , score = self.get_bag_letters()[l.get_character()]
            self.get_bag_letters()[l.get_character()] = (count + 1, score)
             
    

    def get_bag_letters(self):
        ''' Get the bag of letters '''
        return self.__bag_letters
    
    
    def amount_letters_in_bag(self):
        ''' Return the number of letters that are avalable in the bag.
        '''
        count = 0
        for key, data in self.get_bag_letters().items():
            count += data[0]
        return count
