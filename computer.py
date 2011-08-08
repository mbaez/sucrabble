#!/usr/bin/env python

from elements import *
import random


class Computer:
    ''' The Computer module represents the computer scrabble player 
        in the User vs Computer mode.
    '''
    def __init__(self, letters):
        ''' Initialize the Computer class.
            
            @param letters: List of the Letters to use.
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
    
        
    def swap_letters(self, bag, amount=0):
        ''' Return the given amount of Letters to the bag, and take
            the same amount from the bag.
            
            @param bag: the bag
            @param amount: the amount.
            @return: True if it is possible otherwise False.
        '''
        from_bag = bag.remove_letters(amount)
        if from_bag == -1:
            return False
        
        to_bag = [] 
        i = 0
        amount = len(from_bag) 
        while i < amount:
            for j in range(0, self.letters_length()):
                if random.randint(0, 1) and i < amount:
                    l = self.get_letter_at(j)
                    to_bag.append(l)
                    self.get_letters().remove(l)
                    i += 1
        
        bag.add_letters(to_bag)
        for l in from_bag:
            self.add_letter(l)
        return True         
            
            
                                
    def make_move(self, board, dict, moves):
        ''' Function which calculates the move that the computer
            will make.
            
            @param board: the current gameboard
            @param dict: the dictionary
            @param moves: the list of Moves that were made along the game.
            @return: the Move made.
        '''
        move = Move()
        for i in range(0, board.get_size()):
            for j in range(0, board.get_size()):
                if not board.is_tile_empty(i, j):
                    letter = board.get_value_at(i, j)
                    criterion, type = utility.can_form_a_word(board, 
                                                              self.get_letters(),
                                                              letter, i, j)
                    words = utility.search_words_that_match(criterion, 
                                                            dict)
                    for w in words:
                        possible = move.try_move(board, w, type, i, j)
                        if possible:
                            move.calculate_score()
                            return move
        # probar intercambiar letras.
        # else pasar turno.
        # to be continued..
         

        
        
        
