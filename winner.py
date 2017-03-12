from dealer import Dealer
from hand_rank import Poker
import bisect
import os
import sys

class ShowHands:
    def Winner(player1, player2, CommunityCards):
        if ((Poker.RoyalFlush(P1, CommunityCards)) or (Poker.RoyalFlush(P2, CommunityCards))):
            if ((Poker.RoyalFlush(P1, CommunityCards)) > (Poker.RoyalFlush(P2, CommunityCards))):
                print ("Player 1 is the Winner (Royal Flush)")
            elif ((Poker.RoyalFlush(P1, CommunityCards)) < (Poker.RoyalFlush(P2, CommunityCards))):
                print ("Player 2 is the Winner (Royal Flush)")
            else:
                print ("It's a Tie (Royal Flush)")

        # Checking to see if any of the players have Straight Flush
        elif ((Poker.StraightFlush(P1, CommunityCards)) or (Poker.StraightFlush(P2, CommunityCards))):
            if ((Poker.StraightFlush(P1, CommunityCards)) > (Poker.StraightFlush(P2, CommunityCards))):
                print ("Player 1 is the Winner (Straight Flush)")
            elif ((Poker.StraightFlush(P1, CommunityCards)) < (Poker.StraightFlush(P2, CommunityCards))):
                print ("Player 2 is the Winner (Straight Flush)")
            else:
                print ("It's a Tie (Straight Flush)")

        # Checking to see if any of the players have Four of a Kind
        elif (((Poker.FourOfAKind(P1, CommunityCards)) != 0) or ((Poker.FourOfAKind(P2, CommunityCards)) != 0)):
            if ((Poker.FourOfAKind(P1, CommunityCards)) > (Poker.FourOfAKind(P2, CommunityCards))):
                print ("Player 1 is the Winner (Four of a Kind)")
            elif ((Poker.FourOfAKind(P1, CommunityCards)) < (Poker.FourOfAKind(P2, CommunityCards))):
                print ("Player 2 is the Winner (Four of a Kind)")
            else:
                print ("It's a Tie (Four of a Kind)")

        # Checking to see if any of the players have Full House
        elif ((Poker.FullHouse(P1, CommunityCards)) or (Poker.FullHouse(P2, CommunityCards))):
            if ((Poker.FullHouse(P1, CommunityCards)) > (Poker.FullHouse(P2, CommunityCards))):
                print ("Player 1 is the Winner (Full House)")
            elif ((Poker.FullHouse(P1, CommunityCards)) < (Poker.FullHouse(P2, CommunityCards))):
                print ("Player 2 is the Winner (Full House)")
            else:
                print ("It's a Tie (Full House)")

        # Checking to see if any of the players have Flush
        elif (((Poker.Flush(P1, CommunityCards))[-1] != 0) or ((Poker.Flush(P2, CommunityCards))[-1] != 0)):
            if ((Poker.Flush(P1, CommunityCards))[-1] > (Poker.Flush(P2, CommunityCards))[-1]):
                print ("Player 1 is the Winner (Flush)")
            elif ((Poker.Flush(P1, CommunityCards))[-1] < (Poker.Flush(P2, CommunityCards))[-1]):
                print ("Player 2 is the Winner (Flush)")
            else:
                print ("It's a Tie (Flush)")

        # Checking to see if any of the players have Straight
        elif (((Poker.Straight(P1, CommunityCards)) != 0) or ((Poker.Straight(P2, CommunityCards)) != 0)):
            if ((Poker.Straight(P1, CommunityCards)) > (Poker.Straight(P2, CommunityCards))):
                print ("Player 1 is the Winner (Straight)")
            elif ((Poker.Straight(P1, CommunityCards)) < (Poker.Straight(P2, CommunityCards))):
                print ("Player 2 is the Winner (Straight)")
            else:
                print ("It's a Tie (Straight)")

        # Checking to see if any of the players have Three of a Kind
        elif ((Poker.ThreeOfAKind(P1, CommunityCards)) or (Poker.ThreeOfAKind(P2, CommunityCards))):
            if ((Poker.ThreeOfAKind(P1, CommunityCards)) > (Poker.ThreeOfAKind(P2, CommunityCards))):
                print ("Player 1 is the Winner (Three of a Kind)")
            elif ((Poker.ThreeOfAKind(P1, CommunityCards)) < (Poker.ThreeOfAKind(P2, CommunityCards))):
                print ("Player 2 is the Winner (Three of a Kind)")
            else:
                for n in range (0, 6):
                    if ((Poker.HighCard(P1, CommunityCards))[(7-n)] > (Poker.HighCard(P2, CommunityCards))[(7-n)]):
                        print("Player 1 is the Winner (Three of a Kind High Kicker)")
                        return None
                    if ((Poker.HighCard(P1, CommunityCards))[(7-n)] < (Poker.HighCard(P2, CommunityCards))[(7-n)]):
                        print("Player 2 is the Winner (Three of a Kind High Kicker)")
                        return None
                print ("It's a Tie (Three of a Kind)")

        # Checking to see if any of the players have Two Pair
        elif ((((Poker.TwoPair(P1, CommunityCards))[0] != 0) and ((Poker.TwoPair(P1, CommunityCards))[1] != 0)) or (((Poker.TwoPair(P2, CommunityCards)[0] != 0)) and (Poker.TwoPair(P2, CommunityCards)[1] != 0))):
            for n in range (0, 2):
                if ((Poker.TwoPair(P1, CommunityCards))[n] > (Poker.TwoPair(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Two Pair)")
                    return None
                if ((Poker.TwoPair(P1, CommunityCards))[n] < (Poker.TwoPair(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Two Pair)")
                    return None
            if ((Poker.TwoPair(P1, CommunityCards))[2] > (Poker.TwoPair(P2, CommunityCards))[2]):
                print ("Player 1 is the Winner (Two Pair High Kicker)")
                return None
            elif ((Poker.TwoPair(P1, CommunityCards))[2] < (Poker.TwoPair(P2, CommunityCards))[2]):
                print ("Player 2 is the Winner (Two Pair High Kicker)")
                return None
            else:
                print("It's a Tie (Two Pair)")
        # Checking to see if any of the players have One Pair
        elif ((Poker.OnePair(P1, CommunityCards)) or (Poker.OnePair(P2, CommunityCards))):
            if ((Poker.OnePair(P1, CommunityCards)) > (Poker.OnePair(P2, CommunityCards))):
                print ("Player 1 is the Winner (One Pair)")
            elif ((Poker.OnePair(P1, CommunityCards)) < (Poker.OnePair(P2, CommunityCards))):
                print ("Player 2 is the Winner (One Pair)")
            else:
                for n in range (0, 6):
                    if ((Poker.HighCard(P1, CommunityCards))[(7-n)] > (Poker.HighCard(P2, CommunityCards))[(7-n)]):
                        print("Player 1 is the Winner (One Pair High Kicker)")
                        return None
                    if ((Poker.HighCard(P1, CommunityCards))[(7-n)] < (Poker.HighCard(P2, CommunityCards))[(7-n)]):
                        print("Player 2 is the Winner (One Pair High Kicker)")
                        return None
                print ("It's a Tie (One Pair)")

        # Checking to see which one of the players have the high card for the win
        else:
            for n in range (0, 6):
                if ((Poker.HighCard(P1, CommunityCards))[(7-n)] > (Poker.HighCard(P2, CommunityCards))[(7-n)]):
                    print("Player 1 is the Winner (High Card)")
                    return None
                if ((Poker.HighCard(P1, CommunityCards))[(7-n)] < (Poker.HighCard(P2, CommunityCards))[(7-n)]):
                    print("Player 2 is the Winner (High Card)")
                    return None
            print ("It's a Tie (High Card)")

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
"""

# Test Dealer
CommunityCards = []
P1 = []
P2 = []

D = Dealer()
P1 = D.deal_pockets()
print(P1)
P2 = D.deal_pockets()
print(P2)
D.deal_flop()
D.deal_turn()
CommunityCards = D.deal_river()

ShowHands.Winner(P1, P2, CommunityCards)