import random
import os

# Defined colors
term_black = ""
term_red = ""
term_def = ""

# if a posix system like mac or linux print with colors
if os.name == 'posix':
	term_black = "\033[107;30m"
	term_red = "\033[107;91m"
	term_def = "\033[0m"

# Attributes of a card object:
# Rank : {2, 3, ..., 10, 11(J), 12(Q), 13(K), 14(A)}
# Suit : Club(1), Diamond(2), Heart(3), Spade(4)
class Card:
	def __init__(self, rank, suit):
		self.rank_ = rank
		self.suit_ = suit
		
	def __str__(self):
		s = ""
		if self.suit_ == 1:
			s += term_black + "\u2663" + term_def # Prints black on white symbol
		elif self.suit_ == 2:
			s += term_red + "\u2666" + term_def # Prints red on white symbol
		elif self.suit_ == 3:
			s += term_red + "♥" + term_def 	# (: Prints red on white symbol
		else:
			s += term_black + "\u2660" + term_def # Prints black on white symbol
			
		if self.rank_ < 11:
			s += str(self.rank_)
		elif self.rank_ == 11:
			s += "J"
		elif self.rank_ == 12:
			s += "Q"
		elif self.rank_ == 13:
			s += "K"
		else:
			s += "A"
			
		return s
		
	__repr__ = __str__
		
	def __eq__(self, other):
	# Override the default Equals behavior
		if isinstance(other, self.__class__):
			return (self.rank_ == other.rank_) and (self.suit_ == other.suit_)
		return False

	def __ne__(self, other):
		# Define a non-equality test
		return not self.__eq__(other)

	def __lt__(self, other):
		# Define comparison w.r.t their ranks
		if isinstance(other, self.__class__):
			return self.rank_ < other.rank_
		return False

class Deck:
	def __init__(self):
		self.cards_ = []
		for suit in range(4):
			for rank in range(2, 15):
				self.cards_.append(Card(rank, suit))
				
	def __len__(self):
		return len(self.cards_)
			
	def __str__(self):
		return str(self.cards_)
			
	def shuffle(self):
		random.shuffle(self.cards_)
		
	def pop(self):
		return self.cards_.pop(0)
		
	def remove(self, cards):
		# Find the given cards and remove them from the deck.
		for card in cards:
			self.cards_.remove(card)
				

# Test
#D = Deck()
#print(D)
#D.shuffle()
#print(D)

