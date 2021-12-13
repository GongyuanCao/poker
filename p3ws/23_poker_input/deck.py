from card import Card, card_from_num
import random


class Deck(object):
    ''' this is a deck of cards'''
    def __init__(self, cards=None):
        if cards == None:
            cards = []
        self.cards = cards

    def __str__(self):
        lis = []
        for i in self.cards:
            lis.append(i.__str__())
            pass
        s = ' '.join(lis)
        return s

    def __repr__(self):
        return 'Deck(%s)' % (self.__str__())

    def add_card(self, c):
        self.cards.append(c)
        pass

    def add_placeholder_card(self):
        self.cards.append(Card('?', '?'))
        return self.cards[-1]

    def contains(self, c):
        for i in self.cards:
            if i.__eq__(c):
                return True
        return False

    def shuffle(self):
        random.shuffle(self.cards)
        pass

    def assert_full(self):
        stdeck = Deck()
        for i in range(52):
            stdeck.cards.append(card_from_num(i))
            pass
        for i in stdeck.cards:
            assert self.contains(i)
            pass
        assert len(self.cards) == 52
        pass

    # takes card from from deck, appends it to end, and returns it
    def draw(self):
        drawcard = self.cards.pop(0)
        self.cards.append(drawcard)
        return drawcard

    # sorts high to low
    def sort(self):
        self.cards.sort(reverse=True)
        pass
    pass

# builds and returns complete deck except for cards in hands
def build_remaining_deck(hands):
    stdeck = Deck()
    for i in range(52):
        stdeck.cards.append(card_from_num(i))
        pass
    ans = stdeck
    for hand in hands:
        for i in hand.cards:
            if ans.contains(i):
                ans.cards.remove(i)
#                hand.cards.remove(i)
                pass
            pass
        pass
    return ans
