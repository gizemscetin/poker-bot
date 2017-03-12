from deck import Deck, Card
import bisect

class Dealer:
	def __init__(self):
		self.deck_ = Deck()
		self.communitycards_ = []

	def deal_pockets(self, player_count=1):
		# Pocket cards (later they'll belong to one of the players)
		pockets = []
		pockets.append(self.deck_.pop())
		bisect.insort(pockets, self.deck_.pop())

		# Test Print
		for card in pockets:
			card.show()
		print()
		return pockets

	def deal_flop(self):
		# Flop (three community cards)
		self.communitycards_.append(self.deck_.pop())
		self.communitycards_.append(self.deck_.pop())
		self.communitycards_.append(self.deck_.pop())
		self.show()

	def deal_turn(self):
		# Turn (single community card)
		self.communitycards_.append(self.deck_.pop())
		self.show()

	def deal_river(self):
		# River (last community card)
		self.communitycards_.append(self.deck_.pop())
		self.show()
		return self.communitycards_

	def show(self):
		# Print community cards
		print("\n\t\t", end='')
		for card in self.communitycards_:
			card.show()
		print()
"""
# Test Dealer
D = Dealer()
#D.deal_pockets()
P1 = D.deal_pockets()
P2 = D.deal_pockets()
D.deal_flop()
D.deal_turn()
D.deal_river()
"""