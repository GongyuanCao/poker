# import statements here
from card import Card
from deck import Deck
from future import FutureCards

def hand_from_string(s, fc):
    pass

def read_input(file, fc):
    f = open(file)
    hands = []
    decks = []
    for line in f.readlines():
#        print(line)
        hand = []
        deck = Deck()
        words = line.split()
#        print(words)
        for i in words:
            if len(i) == 2:
                hand.append(list(i))
                pass
            if len(i) > 2:
                hand.append(['?', i[1:]])
            pass
#        print(hand)
        for j in range(len(hand)):
            if hand[j][0] != '?':
                c = Card(hand[j][0], hand[j][1])
                deck.add_card(c)
                pass
            if hand[j][0] == '?':
                deck.add_placeholder_card()
                fc.add_future_card(int(hand[j][1]), Card())
                deck.cards[-1] = fc.future_cards[int(hand[j][1])].cards[-1]
                pass
            pass
        decks.append(deck)
        hands.append(deck.__str__())
#        print(hands)
        pass
    return decks
