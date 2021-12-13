from card import Card, card_from_num

from deck import Deck
from future import FutureCards

# make sure you test all of your functions!

# tip: draw lots of pictures with arrows for pointers to cards.
# use the 'is' operator to see if two arrows point at the same card.
# e.g. if i do
# c1 = Card('K','s')
# c2 = Card('K','s')
# c1 == c2 evaluates to True, but
# c1 is c2 evaluates to False
# because the arrows point to different boxes
# however, if i do
# c1 = Card('K','s')
# d = Deck()
# d.add_card(c1)
# c1 is d.cards[0] evaluates to True
# because the arrows point to the same box
def main():
    hand1 = Deck()
    hand1.add_card(Card('3', 'c'))
    hand1.add_card(Card('4', 'c'))
    hand1.add_card(Card('?', '?'))
    hand1.add_card(Card('?', '?'))
    hand1.add_card(Card('?', '?'))
    hand2 = Deck()
    hand2.add_card(Card('5', 'd'))
    hand2.add_card(Card('9', 'h'))
    hand2.add_card(Card('?', '?'))
    hand2.add_card(Card('?', '?'))
    hand2.add_card(Card('?', '?'))
    hands = FutureCards([hand1, hand2])
    hands.__str__()
    hands.__repr__()
if __name__ == '__main__':
    main()
    pass

