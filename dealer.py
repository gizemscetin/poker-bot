from deck import Deck, Card
import bisect

class Dealer:
	def __init__(self):
		self.deck_ = Deck()
		self.deck_.shuffle()
		self.communitycards_ = []
		
	def deal_pockets(self, player_count=1):
		# Pocket cards (later they'll belong to one of the players)
		pockets = []
		pockets.append(self.deck_.pop())
		bisect.insort(pockets, self.deck_.pop())
		return pockets
			
	def deal_flop(self):
		# Flop (three community cards)
		self.communitycards_.append(self.deck_.pop())
		self.communitycards_.append(self.deck_.pop())
		self.communitycards_.append(self.deck_.pop())
		print(self)
		
	def deal_turn(self):
		# Turn (single community card)
		self.communitycards_.append(self.deck_.pop())
		print(self)
		
	def deal_river(self):
		# River (last community card)
		self.communitycards_.append(self.deck_.pop())
		print(self)
		
	def __str__(self):
		return "\t\t" + str(self.communitycards_)
		
# Test Dealer
#D = Dealer()
#D.deal_flop()
#D.deal_turn()
#D.deal_river()