#!/usr/bin/env python

from User import User
from computer import Computer
from elements import *
import constants
import utility
import random

class Game:
    def __init__(self):
        self.board = Board()
        self.bag = Bag()
        self.dict = utility.get_dictionary()
        self.user = User(self.bag)
        self.computer = Computer(self.bag)
        self.moves_log = []
        
    
    def get_user_letters(self):
        ''' Return the list of user's Letters
        
            @return: the list of user's Letters.
        '''
        return self.user.get_letters()
    
    def get_computer_letters(self):
        ''' Return the list of computer's Letters
        
            @return: the list of computer's Letters.
        '''
        return self.computer.get_letters()
    
    def get_user(self):
        return self.user
    
    def get_computer(self):
        return self.computer
        
    def computer_make_move(self):
        return self.computer.make_move(self.board, 
                                       self.dict, 
                                       self.moves_log)
    
    def get_players_char_letters(self, player):
        '''
            Return the list of letters the given player currently has.
            
            @param player: string indicating the player ('user' or 'computer')
            @return: the list of letters.
        '''
        letters = []
        lts = getattr(self, player).get_letters()
        for l in lts:
            letters.append(l.get_character())
        return letters
    
    def user_swap_letters(self, letters):
        ''' Return the given list of Letters to the bag, and take
            the same amount of letters from the bag.
            
            @param letters: the list of letters to put back.
            @return: True if it is possible, otherwise False.
        '''
        res = self.user.swap_letters(self.bag, letters)
        return res
    
    def computer_swap_letters(self):
        ''' Return the an amount of Letters to the bag, and take
            the same amount of letters from the bag.
            
            @return: True if it is possible, otherwise False.
        '''     
        amount = random.randint(1, 7)
        res = self.computer.swap_letters(self.bag, amount)
        return res
        
         

        

