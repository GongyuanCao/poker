from deck import Deck
import re


class FutureCards(object):
    ''' decks for future cards'''
    def __init__(self, decks=None):
        if decks is None:
            decks = []
            pass
        self.future_cards = decks
        pass

    def __str__(self):
        out = []
        for i in self.future_cards:
            out.append(i.__str__())
            pass
        out = '\n'.join(out)
        return out

    def __repr__(self):
        out = ['FutureCards:']
        j = 0
        for i in self.future_cards:
            out.append('?{0}: {1}'.format(j, i.__str__()))
            j += 1
            pass
        out = '\n'.join(out)
        return out

    def add_future_card(self, ind, c):
        while len(self.future_cards) <= ind:
            d = Deck()
            self.future_cards.append(d)
            pass
        else:
            self.future_cards[ind].add_card(c)
            pass
        pass

    def future_cards_from_deck(self, d):
        for i in range(len(self.future_cards)):
            for j in range(len(self.future_cards[i].cards)):
                self.future_cards[i].cards[j].value = d.cards[i].value
                self.future_cards[i].cards[j].suit = d.cards[i].suit
                pass
            pass
        pass
