from deck import Deck, Card
from dealer import Dealer

# Starting hand chart:
# https://pnimg.net/w/articles-attachments/0/553/7f42caa3d3.jpg
# There are 3 categories for pocket cards : {pair, suited, non-suited} 
# Distinct hands: 13 pairs, 78 suited, 78 non-suited
# Hand strength : {"weak"	: [127-169],
#				   "medium-": [85-126],
#				   "medium+": [43-84],
#				   "strong" : [1-42]}

hand_chart_rank_for_pairs = [1, 2, 3, 5, 10, 17, 21, 29, 36, 46, 50, 52, 51]

hand_chart_rank_for_suited = [	[0, 4, 6, 8, 12, 19, 24, 30, 34, 28, 32, 33, 39],
								[0, 0, 7, 9, 14, 22, 37, 44, 53, 55, 58, 60, 59],
								[0, 0, 0, 13, 15, 25, 43, 61, 66, 69, 71, 72, 75],
								[0, 0, 0, 0, 16, 26, 41, 64, 79, 82, 86, 87, 89],
								[0, 0, 0, 0, 0, 23, 38, 57, 74, 93, 95, 96, 98],
								[0, 0, 0, 0, 0, 0, 40, 54, 68, 88, 106, 107, 111],
								[0, 0, 0, 0, 0, 0, 0, 48, 62, 78, 94, 116, 118],
								[0, 0, 0, 0, 0, 0, 0, 0, 56, 67, 85, 103, 120],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 63, 70, 90, 110],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65, 77, 92],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 84, 97],
								[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 105]]
								
hand_chart_rank_for_nonsuited = [[0, 11, 18, 27, 42, 76, 91, 102, 113, 101, 104, 109, 117],
								 [0, 0, 20, 31, 45, 81, 112, 122, 125, 128, 132, 133, 135],
								 [0, 0, 0, 35, 49, 83, 115, 131, 137, 141, 143, 144, 146],
								 [0, 0, 0, 0, 47, 80, 108, 129, 147, 149, 152, 152, 155],
								 [0, 0, 0, 0, 0, 73, 100, 124, 140, 157, 158, 160, 162],
								 [0, 0, 0, 0, 0, 0, 99, 119, 134, 150, 164, 165, 166],
								 [0, 0, 0, 0, 0, 0, 0, 114, 126, 139, 156, 167, 168],
								 [0, 0, 0, 0, 0, 0, 0, 0, 121, 130, 145, 161, 169],
								 [0, 0, 0, 0, 0, 0, 0, 0, 0, 123, 136, 148, 163],
								 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 138, 151],
								 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 142, 154],
								 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 159]]
								

class HandStrengthCalculator:
	def __init__(self, cards):
		self.deck_ = Deck()			# Full deck with 52 cards
		self.pocket_cards_ = cards	# Pocket cards of our player
		self.deck_.remove(cards)	# Don't forget to remove each revealed
									# card from the deck
		self.pocket_rank_ = 0		# 169 possible pocket hands and you ain't one. JK
		
		if self.pocket_pair():
			self.pocket_rank_ = hand_chart_rank_for_pairs[14-self.pocket_cards_[0].rank_]
		elif self.pocket_suited():
			self.pocket_rank_ = hand_chart_rank_for_suited[14-self.pocket_cards_[1].rank_]\
														  [14-self.pocket_cards_[0].rank_]
		else:
			self.pocket_rank_ = hand_chart_rank_for_nonsuited[14-self.pocket_cards_[1].rank_]\
															 [14-self.pocket_cards_[0].rank_]
		if self.pocket_rank_ > 126:													 
			self.pocket_strength_ = "weak"
		elif self.pocket_rank_ > 84:													 
			self.pocket_strength_ = "medium-"
		elif self.pocket_rank_ > 42:													 
			self.pocket_strength_ = "medium+"
		elif self.pocket_rank_ > 5:													 
			self.pocket_strength_ = "strong"
		elif self.pocket_rank_ > 1:
			self.pocket_strength_ = "top-notch"
		else:
			self.pocket_strength_ = "$$cashmeousside$$howbowdah$$"

		
	def __str__(self):
		return str(self.pocket_rank_) + " : " + self.pocket_strength_
					
	# Check if pocket is a pair
	def pocket_pair(self):
		if (self.pocket_cards_[0].rank_ == self.pocket_cards_[1].rank_):
			return True
		return False
	
	# Check if pocket is suited
	def pocket_suited(self):
		if (self.pocket_cards_[0].suit_ == self.pocket_cards_[1].suit_):
			return True
		return False

		
# Test
D = Dealer()
pocket = D.deal_pockets()
print(pocket)
H = HandStrengthCalculator(pocket)
print(H)