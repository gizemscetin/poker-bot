from dealer import Dealer
from hand_rank import HandRank
import bisect

#If P1 is winner function returns "0", if P2 is winner function returns "1", in the case of tie function returns None
class ShowHands:
    def Winner(P1, P2, CommunityCards):
        if ((HandRank.RoyalFlush(P1, CommunityCards))[0] != 0 or (HandRank.RoyalFlush(P2, CommunityCards))[0] != 0):
            for n in range (0,5):
                if ((HandRank.RoyalFlush(P1, CommunityCards))[n] > (HandRank.RoyalFlush(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Royal Flush)")
                    return 0
                if ((HandRank.RoyalFlush(P1, CommunityCards))[n] < (HandRank.RoyalFlush(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Royal Flush)")
                    return 1
            print ("It's a Tie (Royal Flush)")
            return None

        # Checking to see if any of the players have Straight Flush
        elif (((HandRank.StraightFlush(P1, CommunityCards))[0] != 0) or ((HandRank.StraightFlush(P2, CommunityCards))[0] != 0)):
            for n in range (0,5):
                if ((HandRank.StraightFlush(P1, CommunityCards))[n] > (HandRank.StraightFlush(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Straight Flush)")
                    return 0
                elif ((HandRank.StraightFlush(P1, CommunityCards))[n] < (HandRank.StraightFlush(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Straight Flush)")
                    return 1
            print ("It's a Tie (Straight Flush)")
            return None

        # Checking to see if any of the players have Four of a Kind
        elif (((HandRank.FourOfAKind(P1, CommunityCards))[0] != 0) or (HandRank.FourOfAKind(P2, CommunityCards))[0] != 0):
            for n in range (0,5):
                if ((HandRank.FourOfAKind(P1, CommunityCards))[n] > (HandRank.FourOfAKind(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Four of a Kind)")
                    return 0
                if ((HandRank.FourOfAKind(P1, CommunityCards))[n] < (HandRank.FourOfAKind(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Four of a Kind)")
                    return 1
            print ("It's a Tie (Four of a Kind)")
            return None

        # Checking to see if any of the players have Full House
        elif (((HandRank.FullHouse(P1, CommunityCards))[0] != 0) or ((HandRank.FullHouse(P2, CommunityCards))[0] != 0)):
            for n in range (0,5):
                if ((HandRank.FullHouse(P1, CommunityCards))[n] > (HandRank.FullHouse(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Full House)")
                    return 0
                elif ((HandRank.FullHouse(P1, CommunityCards))[n] < (HandRank.FullHouse(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Full House)")
                    return 1
            print ("It's a Tie (Full House)")
            return None

        # Checking to see if any of the players have Flush
        elif (((HandRank.Flush(P1, CommunityCards))[0] != 0) or ((HandRank.Flush(P2, CommunityCards))[0] != 0)):
            for n in range (0,5):
                if ((HandRank.Flush(P1, CommunityCards))[n] > (HandRank.Flush(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Flush)")
                    return 0
                if ((HandRank.Flush(P1, CommunityCards))[n] < (HandRank.Flush(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Flush)")
                    return 1
            print ("It's a Tie (Flush)")
            return None

        # Checking to see if any of the players have Straight
        elif (((HandRank.Straight(P1, CommunityCards))[0] != 0) or ((HandRank.Straight(P2, CommunityCards))[0] != 0)):
            for n in range (0,5):
                if ((HandRank.Straight(P1, CommunityCards))[n] > (HandRank.Straight(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Straight)")
                    return 0
                if ((HandRank.Straight(P1, CommunityCards))[n] < (HandRank.Straight(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Straight)")
                    return 1
            print ("It's a Tie (Straight)")
            return None

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
                        return 0
                    if ((HandRank.ThreeOfAKind(P1, CommunityCards))[3+n] < (HandRank.ThreeOfAKind(P2, CommunityCards))[3+n]):
                        print("Player 2 is the Winner (Three of a Kind High Kicker)")
                        return 1
                print ("It's a Tie (Three of a Kind)")
                return None

        # Checking to see if any of the players have Two Pair
        elif ((((HandRank.TwoPair(P1, CommunityCards))[0] != 0) and ((HandRank.TwoPair(P1, CommunityCards))[1] != 0)) or (((HandRank.TwoPair(P2, CommunityCards)[0] != 0)) and (HandRank.TwoPair(P2, CommunityCards)[1] != 0))):
            for n in range (0, 4):
                if ((HandRank.TwoPair(P1, CommunityCards))[n] > (HandRank.TwoPair(P2, CommunityCards))[n]):
                    print ("Player 1 is the Winner (Two Pair)")
                    return 0
                if ((HandRank.TwoPair(P1, CommunityCards))[n] < (HandRank.TwoPair(P2, CommunityCards))[n]):
                    print ("Player 2 is the Winner (Two Pair)")
                    return 1
            if ((HandRank.TwoPair(P1, CommunityCards))[4] > (HandRank.TwoPair(P2, CommunityCards))[4]):
                print ("Player 1 is the Winner (Two Pair High Kicker)")
                return 0
            elif ((HandRank.TwoPair(P1, CommunityCards))[4] < (HandRank.TwoPair(P2, CommunityCards))[4]):
                print ("Player 2 is the Winner (Two Pair High Kicker)")
                return 1
            else:
                print("It's a Tie (Two Pair)")
                return None

        # Checking to see if any of the players have One Pair
        elif (((HandRank.OnePair(P1, CommunityCards))[0] != 0) or ((HandRank.OnePair(P2, CommunityCards))[0] != 0)):
            if ((HandRank.OnePair(P1, CommunityCards))[0] > (HandRank.OnePair(P2, CommunityCards))[0]):
                print ("Player 1 is the Winner (One Pair)")
                return 0
            elif ((HandRank.OnePair(P1, CommunityCards))[0] < (HandRank.OnePair(P2, CommunityCards))[0]):
                print ("Player 2 is the Winner (One Pair)")
                return 1
            else:
                for n in range (0, 5):
                    if ((HandRank.HighCard(P1, CommunityCards))[(n)] > (HandRank.HighCard(P2, CommunityCards))[(n)]):
                        print("Player 1 is the Winner (One Pair High Kicker)")
                        return 0
                    if ((HandRank.HighCard(P1, CommunityCards))[(n)] < (HandRank.HighCard(P2, CommunityCards))[(n)]):
                        print("Player 2 is the Winner (One Pair High Kicker)")
                        return 1
                print ("It's a Tie (One Pair)")
                return None

        # Checking to see which one of the players have the high card for the win
        else:
            for n in range (0, 5):
                if ((HandRank.HighCard(P1, CommunityCards))[(n)] > (HandRank.HighCard(P2, CommunityCards))[(n)]):
                    print("Player 1 is the Winner (High Card)")
                    return 0
                if ((HandRank.HighCard(P1, CommunityCards))[(n)] < (HandRank.HighCard(P2, CommunityCards))[(n)]):
                    print("Player 2 is the Winner (High Card)")
                    return 1
            print ("It's a Tie (High Card)")
            return None

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
print(P1)
P2 = D.deal_pockets()
print(P2)
D.deal_flop()
D.deal_turn()
D.deal_river()
CommunityCards = D.communitycards_

ShowHands.Winner(P1, P2, CommunityCards)

#print ("\n\tPlayer 1\tPlayer 2")
#print (HandRank.RoyalFlush(P1, CommunityCards), "\t", HandRank.RoyalFlush(P2, CommunityCards))
#print (HandRank.FourOfAKind(P1, CommunityCards), "\t", HandRank.FourOfAKind(P2, CommunityCards))
#print (HandRank.FullHouse(P1, CommunityCards), "\t", HandRank.FullHouse(P2, CommunityCards))
#print (HandRank.Flush(P1, CommunityCards), "\t", HandRank.Flush(P2, CommunityCards))
#print (HandRank.Straight(P1, CommunityCards), "\t", HandRank.Straight(P2, CommunityCards))
#print (HandRank.ThreeOfAKind(P1, CommunityCards), "\t", HandRank.ThreeOfAKind(P2, CommunityCards))
#print (HandRank.TwoPair(P1, CommunityCards), "\t", HandRank.TwoPair(P2, CommunityCards))
#print (HandRank.OnePair(P1, CommunityCards), "\t", HandRank.OnePair(P2, CommunityCards))
#print (HandRank.HighCard(P1, CommunityCards), "\t", HandRank.HighCard(P2, CommunityCards))

#print("Only the best combination hand for each player is printed\nCorrectly in terms of including ordered high kickers")

"""
