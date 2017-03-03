import random

# Attributes of a card object:
# Rank : {1, 2, 3, ..., 10, 11(J), 12(Q), 13(K)}
# Suit : Club(1), Diamond(2), Heart(3), Spade(4)
class Card:
	def __init__(self, rank, suit):
		self.rank_ = rank
		self.suit_ = suit
		
	def show(self):
		s = ""
		if self.suit_ == 1:
			s += "\u2663"
		elif self.suit_ == 2:
			s += "\u2666"
		elif self.suit_ == 3:
			s += "♥"	# (:
		else:
			s += "\u2660"
			
		if self.rank_ == 1:
			s += "A"
		elif self.rank_ < 11:
			s += str(self.rank_)
		elif self.rank_ == 11:
			s += "J"
		elif self.rank_ == 12:
			s += "Q"
		else:
			s += "K"
			
		print(s, end = ' ')

class Deck:
	def __init__(self):
		self.cards_ = []
		for suit in range(4):
			for rank in range(1, 14):
				self.cards_.append(Card(rank, suit))
				
	def show(self):
		for card in self.cards_:
			card.show()
			
	def shuffle(self):
		random.shuffle(self.cards_)
	
			
D = Deck()
D.shuffle()
D.show()

