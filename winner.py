from dealer import Dealer
from handrank import HandRank
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

class ShowHands:
    def Winner(player1, player2, CommunityCards):
        if ((HandRank.RoyalFlush(P1, CommunityCards))[0] != 0 or (HandRank.RoyalFlush(P2, CommunityCards))[0] != 0):
            for n in range (0,5):
                if ((HandRank.RoyalFlush(P1, CommunityCards))[n] > (HandRank.RoyalFlush(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Royal Flush)")
                    return None
                if ((HandRank.RoyalFlush(P1, CommunityCards))[n] < (HandRank.RoyalFlush(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Royal Flush)")
                    return None
            print ("It's a Tie (Royal Flush)")

        # Checking to see if any of the players have Straight Flush
        elif (((HandRank.StraightFlush(P1, CommunityCards))[0] != 0) or ((HandRank.StraightFlush(P2, CommunityCards))[0] != 0)):
            for n in range (0,5):
                if ((HandRank.StraightFlush(P1, CommunityCards))[n] > (HandRank.StraightFlush(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Straight Flush)")
                    return None
                elif ((HandRank.StraightFlush(P1, CommunityCards))[n] < (HandRank.StraightFlush(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Straight Flush)")
                    return None
            print ("It's a Tie (Straight Flush)")

        # Checking to see if any of the players have Four of a Kind
        elif (((HandRank.FourOfAKind(P1, CommunityCards))[0] != 0) or (HandRank.FourOfAKind(P2, CommunityCards))[0] != 0):
            for n in range (0,5):
                if ((HandRank.FourOfAKind(P1, CommunityCards))[n] > (HandRank.FourOfAKind(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Four of a Kind)")
                    return None
                if ((HandRank.FourOfAKind(P1, CommunityCards))[n] < (HandRank.FourOfAKind(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Four of a Kind)")
                    return None
            print ("It's a Tie (Four of a Kind)")

        # Checking to see if any of the players have Full House
        elif (((HandRank.FullHouse(P1, CommunityCards))[0] != 0) or ((HandRank.FullHouse(P2, CommunityCards))[0] != 0)):
            for n in range (0,5):
                if ((HandRank.FullHouse(P1, CommunityCards))[n] > (HandRank.FullHouse(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Full House)")
                    return None
                elif ((HandRank.FullHouse(P1, CommunityCards))[n] < (HandRank.FullHouse(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Full House)")
                    return None
            print ("It's a Tie (Full House)")

        # Checking to see if any of the players have Flush
        elif (((HandRank.Flush(P1, CommunityCards))[0] != 0) or ((HandRank.Flush(P2, CommunityCards))[0] != 0)):
            for n in range (0,5):
                if ((HandRank.Flush(P1, CommunityCards))[n] > (HandRank.Flush(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Flush)")
                    return None
                if ((HandRank.Flush(P1, CommunityCards))[n] < (HandRank.Flush(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Flush)")
                    return None
            print ("It's a Tie (Flush)")

        # Checking to see if any of the players have Straight
        elif (((HandRank.Straight(P1, CommunityCards))[0] != 0) or ((HandRank.Straight(P2, CommunityCards))[0] != 0)):
            for n in range (0,5):
                if ((HandRank.Straight(P1, CommunityCards))[n] > (HandRank.Straight(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Straight)")
                    return None
                if ((HandRank.Straight(P1, CommunityCards))[n] < (HandRank.Straight(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Straight)")
                    return None
            print ("It's a Tie (Straight)")

        # Checking to see if any of the players have Three of a Kind
        elif (((HandRank.ThreeOfAKind(P1, CommunityCards))[0] != 0) or ((HandRank.ThreeOfAKind(P2, CommunityCards))[0] != 0)):
            if ((HandRank.ThreeOfAKind(P1, CommunityCards))[0] > (HandRank.ThreeOfAKind(P2, CommunityCards))[0]):
                print ("Player 1 is the Winner (Three of a Kind)")
            elif ((HandRank.ThreeOfAKind(P1, CommunityCards))[0] < (HandRank.ThreeOfAKind(P2, CommunityCards))[0]):
                print ("Player 2 is the Winner (Three of a Kind)")
            else:
                for n in range (0, 2):
                    if ((HandRank.ThreeOfAKind(P1, CommunityCards))[3+n] > (HandRank.ThreeOfAKind(P2, CommunityCards))[3+n]):
                        print("Player 1 is the Winner (Three of a Kind High Kicker)")
                        return None
                    if ((HandRank.ThreeOfAKind(P1, CommunityCards))[3+n] < (HandRank.ThreeOfAKind(P2, CommunityCards))[3+n]):
                        print("Player 2 is the Winner (Three of a Kind High Kicker)")
                        return None
                print ("It's a Tie (Three of a Kind)")

        # Checking to see if any of the players have Two Pair
        elif ((((HandRank.TwoPair(P1, CommunityCards))[0] != 0) and ((HandRank.TwoPair(P1, CommunityCards))[1] != 0)) or (((HandRank.TwoPair(P2, CommunityCards)[0] != 0)) and (HandRank.TwoPair(P2, CommunityCards)[1] != 0))):
            for n in range (0, 4):
                if ((HandRank.TwoPair(P1, CommunityCards))[n] > (HandRank.TwoPair(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Two Pair)")
                    return None
                if ((HandRank.TwoPair(P1, CommunityCards))[n] < (HandRank.TwoPair(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Two Pair)")
                    return None
            if ((HandRank.TwoPair(P1, CommunityCards))[4] > (HandRank.TwoPair(P2, CommunityCards))[4]):
                print ("Player 1 is the Winner (Two Pair High Kicker)")
                return None
            elif ((HandRank.TwoPair(P1, CommunityCards))[4] < (HandRank.TwoPair(P2, CommunityCards))[4]):
                print ("Player 2 is the Winner (Two Pair High Kicker)")
                return None
            else:
                print("It's a Tie (Two Pair)")
        # Checking to see if any of the players have One Pair
        elif (((HandRank.OnePair(P1, CommunityCards))[0] != 0) or ((HandRank.OnePair(P2, CommunityCards))[0] != 0)):
            if ((HandRank.OnePair(P1, CommunityCards))[0] > (HandRank.OnePair(P2, CommunityCards))[0]):
                print ("Player 1 is the Winner (One Pair)")
            elif ((HandRank.OnePair(P1, CommunityCards))[0] < (HandRank.OnePair(P2, CommunityCards))[0]):
                print ("Player 2 is the Winner (One Pair)")
            else:
                for n in range (0, 5):
                    if ((HandRank.HighCard(P1, CommunityCards))[(n)] > (HandRank.HighCard(P2, CommunityCards))[(n)]):
                        print("Player 1 is the Winner (One Pair High Kicker)")
                        return None
                    if ((HandRank.HighCard(P1, CommunityCards))[(n)] < (HandRank.HighCard(P2, CommunityCards))[(n)]):
                        print("Player 2 is the Winner (One Pair High Kicker)")
                        return None
                print ("It's a Tie (One Pair)")

        # Checking to see which one of the players have the high card for the win
        else:
            for n in range (0, 5):
                if ((HandRank.HighCard(P1, CommunityCards))[(n)] > (HandRank.HighCard(P2, CommunityCards))[(n)]):
                    print("Player 1 is the Winner (High Card)")
                    return None
                if ((HandRank.HighCard(P1, CommunityCards))[(n)] < (HandRank.HighCard(P2, CommunityCards))[(n)]):
                    print("Player 2 is the Winner (High Card)")
                    return None
            print ("It's a Tie (High Card)")

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
"""

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

ShowHands.Winner(P1, P2, CommunityCards)

print ("\n\tPlayer 1\tPlayer 2")
print (HandRank.RoyalFlush(P1, CommunityCards), "\t", HandRank.RoyalFlush(P2, CommunityCards))
print (HandRank.FourOfAKind(P1, CommunityCards), "\t", HandRank.FourOfAKind(P2, CommunityCards))
print (HandRank.FullHouse(P1, CommunityCards), "\t", HandRank.FullHouse(P2, CommunityCards))
print (HandRank.Flush(P1, CommunityCards), "\t", HandRank.Flush(P2, CommunityCards))
print (HandRank.Straight(P1, CommunityCards), "\t", HandRank.Straight(P2, CommunityCards))
print (HandRank.ThreeOfAKind(P1, CommunityCards), "\t", HandRank.ThreeOfAKind(P2, CommunityCards))
print (HandRank.TwoPair(P1, CommunityCards), "\t", HandRank.TwoPair(P2, CommunityCards))
print (HandRank.OnePair(P1, CommunityCards), "\t", HandRank.OnePair(P2, CommunityCards))
print (HandRank.HighCard(P1, CommunityCards), "\t", HandRank.HighCard(P2, CommunityCards))

print("Only the best combination hand for each player is printed\nCorrectly in terms of including ordered high kickers")
