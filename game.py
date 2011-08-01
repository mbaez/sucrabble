from User import User
from computer import *
from elements import *
class Game:
	def __init__(self):
		self.board = Board()
		self.bag = Bag()
		self.user = User(self.bag)
		self.computer =Computer(self.bag)
		
	def get_user_letters(self):
		return self.user.get_letters()
	
	def get_computer_letters(self):
		return self.computer.get_letters()
	
	def get_user(self):
		return self.user
	
	def get_computer(self):
		return self.computer
		

