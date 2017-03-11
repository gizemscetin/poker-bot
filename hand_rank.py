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

class Poker:
    #def __init__(self):

    def RoyalFlush(player, CommunityCards):
        ordered = []
        ordered.append(player[0].rank_)
        bisect.insort(ordered, player[1].rank_)
        for y in range (0, 5):
            bisect.insort(ordered, CommunityCards[y].rank_)
        if (ordered[0] == 1):  #If there is an A in the players hand or community cards
            ordered.append(14) #append rank (14) as 7th card for some hand combinations to be possible
        else:
            ordered.append(None)   # If not append None (Null)
        if (Poker.StraightFlush(player, CommunityCards) and (ordered[3] == 10) and (ordered[4] == 11) and (ordered[5] == 12) and (ordered[6] == 13) and (ordered[7] == 14)):
            return True
        else:
            return False

    def StraightFlush(player, CommunityCards):
        if ((Poker.Flush(player, CommunityCards))[-1] != 0) and (Poker.Straight(player, CommunityCards) != 0) and (Poker.Flush(player, CommunityCards)[-1] == (Poker.Straight(player, CommunityCards))):
            return True
        else:
            return False

    def FourOfAKind(player, CommunityCards):
        ordered = []
        ordered.append(player[0].rank_)
        bisect.insort(ordered, player[1].rank_)
        for y in range (0, 5):
            bisect.insort(ordered, CommunityCards[y].rank_)
        for y in range (0, 4):
            if (ordered[y+3] == ordered[y+2] == ordered[y+1] == ordered[y]):
                if (ordered[y] == 1):
                    return max(ordered)
                else:
                    ordered[y] = 0
                    ordered[y+1] = 0
                    ordered[y+2] = 0
                    ordered[y+3] = 0
                    return max(ordered)
        return 0

    def FullHouse(player, CommunityCards):
        ordered = []
        ordered.append(player[0].rank_)
        bisect.insort(ordered, player[1].rank_)
        for y in range (0, 5):
            bisect.insort(ordered, CommunityCards[y].rank_)
        for y in range (0, 3):
            for x in range (0, (2-y)):
                if (ordered[y+2] == ordered[y+1] == ordered[y]) and (ordered[6-x] == ordered[5-x]):
                    return True
                elif (ordered[x+1] == ordered[x]) and (ordered[6-y] == ordered[5-y] == ordered[4-y]):
                    return True
        return False

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
                bisect.insort(club_cardranks,player[y].rank_)
            elif (CommunityCards[x].suit_ == 2):
                diamond += 1
                bisect.insort(diamond_cardranks,player[y].rank_)
            elif (CommunityCards[x].suit_ == 3):
                heart += 1
                bisect.insort(heart_cardranks,player[y].rank_)
            else:
                spade += 1
                bisect.insort(spade_cardranks,player[y].rank_)
        if (club >= 5):
            return club_cardranks
        elif (diamond >= 5):
            return diamond_cardranks
        elif (heart >= 5):
            return heart_cardranks
        elif (spade >= 5):
            return spade_cardranks
        else:
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
                return ordered[y+4]
        for y in range (0, 3):
            #In case of a Combination like (3, 3, 4, 4, 5, 6, 7) below if statement can still identify the straight poker hand from ordered list
            if (ordered[y+2] == ordered[y] + 1) and (ordered[y+3] == ordered[y] + 2) and (ordered[y+4] == ordered[y] + 3) and (ordered[y+5] == ordered[y] + 4):
                return ordered[y+5]
        return 0

    def ThreeOfAKind(player, CommunityCards):
        ordered = []
        ordered.append(player[0].rank_)
        bisect.insort(ordered, player[1].rank_)
        for y in range (0, 5):
            bisect.insort(ordered, CommunityCards[y].rank_)
        for y in range (0, 5):
            if (ordered[y+1] == ordered[y]) and (ordered[y+2] == ordered[y]):
                if (ordered[y] == 1):
                    return 14
                else:
                    return ordered[y]
        return 0

    def TwoPair(player, CommunityCards):
        ordered = []
        pairs = []
        ordered.append(player[0].rank_)
        bisect.insort(ordered, player[1].rank_)
        for y in range (0, 5):
            bisect.insort(ordered, CommunityCards[y].rank_)
        #Incase one of the Pairs is a pair of Ace adjust the Rank of that pair to High (14)
        if (ordered[0] == 1) and (ordered[1] == 1):
            pairs.append(14)
        else:
            for y in range (0, 3):
                for x in range (0, 3):
                    if (ordered[6-y] == ordered[5-y]) and (ordered[3-x] == ordered[2-x]):
                        pairs.append(ordered[y])
                        if (ordered[3-x] != 1):
                            bisect.insort(pairs, ordered[5-x])
                        ordered[6-y] = 0
                        ordered[5-y] = 0
                        ordered[5-x] = 0
                        ordered[6-x] = 0
                        pairs.append(max(ordered))
                        return pairs
        pairs.append(0)
        pairs.append(0)
        return pairs

    def OnePair(player, CommunityCards):
        ordered = []
        ordered.append(player[0].rank_)
        bisect.insort(ordered, player[1].rank_)
        for x in range (0, 5):
            bisect.insort(ordered, CommunityCards[x].rank_)
        for y in range (0, 6):
            if (ordered[y] == ordered[y+1]):
                if (ordered[y] == 1):
                    return 14
                else:
                    return ordered[y]
        return 0

    def HighCard(player, CommunityCards):   #HighCard returns the Rank value of the highest card
        ordered = []
        ordered.append(player[0].rank_)
        bisect.insort(ordered, player[1].rank_)
        for y in range (0, 5):
            bisect.insort(ordered, CommunityCards[y].rank_)
        if (ordered[0] == 1):  #If there is an A in the players hand or community cards
            ordered.append(14) #append rank (14) as 7th card for some hand combinations to be possible
        else:
            ordered.append(0)   # If not append None (Null)
        return ordered

        """
        if (ordered[7] == 14):
            return ordered[7]
        else:
            return ordered[6]
        """

"""
    if (max(Poker.HighCard(P1, CommunityCards)) > max(Poker.HighCard(P2, CommunityCards))):
        print ("Player 1 is the Winner (High Card)")
    elif (max(Poker.HighCard(P1, CommunityCards)) < max(Poker.HighCard(P2, CommunityCards))):
        print ("Player 2 is the Winner (High Card)")
    elif ((Poker.HighCard(P1, CommunityCards))[n] > max(Poker.HighCard(P2, CommunityCards))[n]):
        print ("Player 1 is the Winner (High Card)")
    elif ((Poker.HighCard(P1, CommunityCards))[n] < (Poker.HighCard(P2, CommunityCards))[n]):
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

Poker.Winner(P1, P2, CommunityCards)


#print(P1[0].rank_,P1[0].suit_ , "")

if ((Poker.OnePair(P1, CommunityCards)) > (Poker.OnePair(P2, CommunityCards))):
    print ("P1")
elif ((Poker.OnePair(P1, CommunityCards)) < (Poker.OnePair(P2, CommunityCards))):
    print ("P2")
else:
    print ("P1 and P2 tie")

print("Player 1 RoyalFlush = ", (Poker.RoyalFlush(P1, CommunityCards)))
print("Player 2 RoyalFlush = ", (Poker.RoyalFlush(P2, CommunityCards)))
print("Player 1 StraightFlush = ", (Poker.StraightFlush(P1, CommunityCards)))
print("Player 2 StraightFlush = ", (Poker.StraightFlush(P2, CommunityCards)))
print("Player 1 FourOfAKind = ", (Poker.FourOfAKind(P1, CommunityCards)))
print("Player 2 FourOfAKind = ", (Poker.FourOfAKind(P2, CommunityCards)))
print("Player 1 FullHouse = ", (Poker.FullHouse(P1, CommunityCards)))
print("Player 2 FullHouse = ", (Poker.FullHouse(P2, CommunityCards)))
print("Player 1 Flush = ", (Poker.Flush(P1, CommunityCards)))
print("Player 2 Flush = ", (Poker.Flush(P2, CommunityCards)))
print("Player 1 Straight = ", (Poker.Straight(P1, CommunityCards)))
print("Player 2 Straight = ", (Poker.Straight(P2, CommunityCards)))
print("Player 1 ThreeOfAKind = ", (Poker.ThreeOfAKind(P1, CommunityCards)))
print("Player 2 ThreeOfAKind = ", (Poker.ThreeOfAKind(P2, CommunityCards)))
print("Player 1 TwoPair = ", (Poker.TwoPair(P1, CommunityCards)))
print("Player 2 TwoPair = ", (Poker.TwoPair(P2, CommunityCards)))
print("Player 1 OnePair = ", (Poker.OnePair(P1, CommunityCards)))
print("Player 2 OnePair = ", (Poker.OnePair(P2, CommunityCards)))
print("Player 1 HighCard = ", (Poker.HighCard(P1, CommunityCards)))
print("Player 2 HighCard = ", (Poker.HighCard(P2, CommunityCards)))
"""