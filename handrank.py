from dealer import Dealer
import bisect
import os
import sys

# Defined colors
term_black = ""
term_red = ""
term_def = ""

# if a posix system like mac or linux print with colors
if os.name == 'posix':
	term_black = "\033[107;30m"
	term_red = "\033[1;91m"
	term_def = "\033[0m"

class HandRank:
	def RoyalFlush(player, CommunityCards):
		ordered = []
		best = []
		ordered.append(player[0].rank_)
		bisect.insort(ordered, player[1].rank_)
		for y in range (0, 5):
			bisect.insort(ordered, CommunityCards[y].rank_)
		if (ordered[0] == 1):  #If there is an A in the players hand or community cards
			del ordered[0]
			ordered.append(14) #append rank (14) as 7th card for some hand combinations to be possible
		if (HandRank.StraightFlush(player, CommunityCards) and (ordered[2] == 10) and (ordered[3] == 11) and (ordered[4] == 12) and (ordered[5] == 13) and (ordered[6] == 14)):
			best = ordered[6:2]
			return best
		else:
			for a in range (0,5):    #If there is no 3 of a kind return 5 element list with all zeros
				best.append(0)
			return best

	def StraightFlush(player, CommunityCards):
		best = []
		if (((HandRank.Flush(player, CommunityCards))[0] != 0) and (HandRank.Straight(player, CommunityCards)[0] != 0) and (HandRank.Flush(player, CommunityCards)) == (HandRank.Straight(player, CommunityCards))):
			best = (HandRank.Straight(player, CommunityCards))
			return best
		else:
			for a in range (0,5):    #If there is no 3 of a kind return 5 element list with all zeros
				best.append(0)
			return best

	def FourOfAKind(player, CommunityCards):
		ordered = []
		best = []
		ordered.append(player[0].rank_)
		bisect.insort(ordered, player[1].rank_)
		for y in range (0, 5):
			bisect.insort(ordered, CommunityCards[y].rank_)
		for y in range (0, 4):
			if (ordered[y+3] == ordered[y+2] == ordered[y+1] == ordered[y]):
				if (ordered[y] == 1):
					best.append(14)
					best.append(14)
					best.append(14)
					best.append(14)
					best.append(max(ordered))
					return best
				else:
					best.append(ordered[y])
					best.append(ordered[y])
					best.append(ordered[y])
					best.append(ordered[y])
					ordered[y] = 0
					ordered[y+1] = 0
					ordered[y+2] = 0
					ordered[y+3] = 0
					best.append(max(ordered))
					return best
		for a in range (0,5):    #If there is no 3 of a kind return 5 element list with all zeros
			best.append(0)
		return best

	def FullHouse(player, CommunityCards):
		ordered = []
		best =[]
		ordered.append(player[0].rank_)
		bisect.insort(ordered, player[1].rank_)
		for y in range (0, 5):
			bisect.insort(ordered, CommunityCards[y].rank_)
		for y in range (0, 3):
			for x in range (0, (3-y)):
				if (ordered[y+2] == ordered[y+1] == ordered[y]) and (ordered[6-x] == ordered[5-x]):
					best.append(ordered[6-x])
					best.append(ordered[6-x])
					best.append(ordered[y])
					best.append(ordered[y])
					best.append(ordered[y])
					return best
				elif (ordered[x+1] == ordered[x]) and (ordered[6-y] == ordered[5-y] == ordered[4-y]):
					best.append(ordered[4-y])
					best.append(ordered[4-y])
					best.append(ordered[4-y])
					best.append(ordered[x])
					best.append(ordered[x])
					return best
		for a in range (0,5):    #If there is no 3 of a kind return 5 element list with all zeros
			best.append(0)
		return best

	def Flush(player, CommunityCards):
		club = 0
		diamond = 0
		heart = 0
		spade = 0
		club_cardranks = []
		diamond_cardranks = []
		heart_cardranks = []
		spade_cardranks = []
		nothing = []
		for y in range (0, 2):
			if (player[y].suit_ == 1):
				club += 1
				bisect.insort(club_cardranks,player[y].rank_)
			elif (player[y].suit_ == 2):
				diamond += 1
				bisect.insort(diamond_cardranks,player[y].rank_)
			elif (player[y].suit_ == 3):
				heart += 1
				bisect.insort(heart_cardranks,player[y].rank_)
			else:
				spade += 1
				bisect.insort(spade_cardranks,player[y].rank_)
		for x in range (0, 5):
			if (CommunityCards[x].suit_ == 1):
				club += 1
				bisect.insort(club_cardranks,CommunityCards[x].rank_)
			elif (CommunityCards[x].suit_ == 2):
				diamond += 1
				bisect.insort(diamond_cardranks,CommunityCards[x].rank_)
			elif (CommunityCards[x].suit_ == 3):
				heart += 1
				bisect.insort(heart_cardranks,CommunityCards[x].rank_)
			else:
				spade += 1
				bisect.insort(spade_cardranks,CommunityCards[x].rank_)
		if (club >= 5):
			if (club_cardranks[0] == 1):
				club_cardranks.append(14)
				del club_cardranks[0]
			return list(reversed(club_cardranks))
		elif (diamond >= 5):
			if (diamond_cardranks[0] == 1):
				diamond_cardranks.append(14)
				del diamond_cardranks[0]
			return list(reversed(diamond_cardranks))
		elif (heart >= 5):
			if (heart_cardranks[0] == 1):
				heart_cardranks.append(14)
				del heart_cardranks[0]
			return list(reversed(heart_cardranks))
		elif (spade >= 5):
			if (spade_cardranks[0] == 1):
				spade_cardranks.append(14)
				del spade_cardranks[0]
			return list(reversed(spade_cardranks))
		else:
			for a in range (0,5):    #If there is no 3 of a kind return 5 element list with all zeros
				nothing.append(0)
			return nothing


		"""
		if ((club or diamond or heart or spade) >= 5):
			return True
		else:
			return False
		"""

	def Straight(player, CommunityCards):
		ordered = []
		best =[]
		ordered.append(player[0].rank_)
		bisect.insort(ordered, player[1].rank_)
		for y in range (0, 5):
			bisect.insort(ordered, CommunityCards[y].rank_)
		if (ordered[0] == 1):  #If there is an A in the players hand or community cards
			ordered.append(14) #append rank (14) as 7th card for some hand combinations to be possible
		else:
			ordered.append(0)   # If not append None (Null)
		for y in range (0, 4):
			if (ordered[y+1] == ordered[y] + 1) and (ordered[y+2] == ordered[y] + 2) and (ordered[y+3] == ordered[y] + 3) and (ordered[y+4] == ordered[y] + 4):
				best.append(ordered[y+4])
				best.append(ordered[y+3])
				best.append(ordered[y+2])
				best.append(ordered[y+1])
				best.append(ordered[y])
				return best
		for y in range (0, 3):
			#In case of a Combination like (3, 3, 4, 4, 5, 6, 7) below if statement can still identify the straight HandRank hand from ordered list
			if (ordered[y+2] == ordered[y] + 1) and (ordered[y+3] == ordered[y] + 2) and (ordered[y+4] == ordered[y] + 3) and (ordered[y+5] == ordered[y] + 4):
				best.append(ordered[y+5])
				best.append(ordered[y+4])
				best.append(ordered[y+3])
				best.append(ordered[y+2])
				best.append(ordered[y])
				return best
		for a in range (0,5):    #If there is no 3 of a kind return 5 element list with all zeros
			best.append(0)
		return best

	def ThreeOfAKind(player, CommunityCards):
		ordered = []
		best = []
		ordered.append(player[0].rank_)
		bisect.insort(ordered, player[1].rank_)
		for y in range (0, 5):
			bisect.insort(ordered, CommunityCards[y].rank_)
		for y in range (0, 5):
			if (ordered[y+1] == ordered[y]) and (ordered[y+2] == ordered[y]):
				if (ordered[y] == 1):     #If three of a kind is with Ace use value 14
					best.append(14)
					best.append(14)
					best.append(14)
					best.append(ordered[-1])  #Highest 2 kicker cards
					best.append(ordered[-2])
					return best
				else:
					best.append(ordered[y])
					best.append(ordered[y])
					best.append(ordered[y])
					del ordered[y]
					del ordered[y]
					del ordered[y]
					best.append(ordered[-1]) #Highest 2 kicker cards
					best.append(ordered[-2])
					return best
		for a in range (0,5):    #If there is no 3 of a kind return 5 element list with all zeros
			best.append(0)
		return best

	def TwoPair(player, CommunityCards):
		ordered = []
		best = []
		ordered.append(player[0].rank_)
		bisect.insort(ordered, player[1].rank_)
		for y in range (0, 5):
			bisect.insort(ordered, CommunityCards[y].rank_)
		for y in range (0, 3):
			for x in range (0, 3):
				if (ordered[6-y] == ordered[5-y]) and (ordered[3-x] == ordered[2-x]):
					best.insert(0,ordered[6-y])
					best.insert(0,ordered[6-y])
					if (ordered[3-x] != 1):
						best.insert(2,ordered[3-x])
						best.insert(2,ordered[3-x])
					else:
						best.insert(0, 14)
						best.insert(0, 14)
					ordered[6-y] = 0
					ordered[5-y] = 0
					ordered[3-x] = 0
					ordered[2-x] = 0
					best.append(max(ordered))
					return best
		for a in range (0,5):
			best.append(0)
		return best

	def OnePair(player, CommunityCards):
		ordered = []
		zero = []
		result =[]
		ordered.append(player[0].rank_)
		bisect.insort(ordered, player[1].rank_)
		for x in range (0, 5):
			bisect.insort(ordered, CommunityCards[x].rank_)
		for y in range (0, 6):
			if (ordered[y] == ordered[y+1]):
				if (ordered[y] == 1):
					del ordered[0]
					ordered.append(14) #append rank (14) as 7th card for some hand combinations to be possible
					del ordered[0]
					ordered.append(14) #append rank (14) as 7th card for some hand combinations to be possible
					return list(reversed(ordered[2:7]))
				else:
					result.append(ordered[y])
					result.append(ordered[y+1])
					del ordered[y]
					del ordered[y]
					result.append(ordered[-1])
					result.append(ordered[-2])
					result.append(ordered[-3])
					return result
			zero.append(0)
		return zero

	def HighCard(player, CommunityCards):   #HighCard returns the Rank value of the highest card
		ordered = []
		ordered.append(player[0].rank_)
		bisect.insort(ordered, player[1].rank_)
		for y in range (0, 5):
			bisect.insort(ordered, CommunityCards[y].rank_)
		if (ordered[0] == 1):  #If there is an A in the players hand or community cards
			del ordered[0]
			ordered.append(14) #append rank (14) as 7th card for some hand combinations to be possible
			return list(reversed(ordered[2:7]))
		else:
			return list(reversed(ordered[2:7]))


		"""
		if (ordered[7] == 14):
			return ordered[7]
		else:
			return ordered[6]
		"""

"""
	if (max(HandRank.HighCard(P1, CommunityCards)) > max(HandRank.HighCard(P2, CommunityCards))):
		print ("Player 1 is the Winner (High Card)")
	elif (max(HandRank.HighCard(P1, CommunityCards)) < max(HandRank.HighCard(P2, CommunityCards))):
		print ("Player 2 is the Winner (High Card)")
	elif ((HandRank.HighCard(P1, CommunityCards))[n] > max(HandRank.HighCard(P2, CommunityCards))[n]):
		print ("Player 1 is the Winner (High Card)")
	elif ((HandRank.HighCard(P1, CommunityCards))[n] < (HandRank.HighCard(P2, CommunityCards))[n]):
		print ("Player 2 is the Winner (High Card)")
	print ("It's a Tie (High Card)")


# Test Dealer
CommunityCards = []
P1 = []
P2 = []

D = Dealer()
P1 = D.deal_pockets()
P2 = D.deal_pockets()
D.deal_flop()
D.deal_turn()
CommunityCards = D.deal_river()

HandRank.Winner(P1, P2, CommunityCards)


#print(P1[0].rank_,P1[0].suit_ , "")

if ((HandRank.OnePair(P1, CommunityCards)) > (HandRank.OnePair(P2, CommunityCards))):
	print ("P1")
elif ((HandRank.OnePair(P1, CommunityCards)) < (HandRank.OnePair(P2, CommunityCards))):
	print ("P2")
else:
	print ("P1 and P2 tie")

print("Player 1 RoyalFlush = ", (HandRank.RoyalFlush(P1, CommunityCards)))
print("Player 2 RoyalFlush = ", (HandRank.RoyalFlush(P2, CommunityCards)))
print("Player 1 StraightFlush = ", (HandRank.StraightFlush(P1, CommunityCards)))
print("Player 2 StraightFlush = ", (HandRank.StraightFlush(P2, CommunityCards)))
print("Player 1 FourOfAKind = ", (HandRank.FourOfAKind(P1, CommunityCards)))
print("Player 2 FourOfAKind = ", (HandRank.FourOfAKind(P2, CommunityCards)))
print("Player 1 FullHouse = ", (HandRank.FullHouse(P1, CommunityCards)))
print("Player 2 FullHouse = ", (HandRank.FullHouse(P2, CommunityCards)))
print("Player 1 Flush = ", (HandRank.Flush(P1, CommunityCards)))
print("Player 2 Flush = ", (HandRank.Flush(P2, CommunityCards)))
print("Player 1 Straight = ", (HandRank.Straight(P1, CommunityCards)))
print("Player 2 Straight = ", (HandRank.Straight(P2, CommunityCards)))
print("Player 1 ThreeOfAKind = ", (HandRank.ThreeOfAKind(P1, CommunityCards)))
print("Player 2 ThreeOfAKind = ", (HandRank.ThreeOfAKind(P2, CommunityCards)))
print("Player 1 TwoPair = ", (HandRank.TwoPair(P1, CommunityCards)))
print("Player 2 TwoPair = ", (HandRank.TwoPair(P2, CommunityCards)))
print("Player 1 OnePair = ", (HandRank.OnePair(P1, CommunityCards)))
print("Player 2 OnePair = ", (HandRank.OnePair(P2, CommunityCards)))
print("Player 1 HighCard = ", (HandRank.HighCard(P1, CommunityCards)))
print("Player 2 HighCard = ", (HandRank.HighCard(P2, CommunityCards)))
"""
