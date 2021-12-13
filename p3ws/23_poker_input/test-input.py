from card import Card, card_from_num
from deck import Deck
from future import FutureCards
from pinput import read_input

def main():
    fc = FutureCards()
    hands = read_input('test.txt', fc)
    print(hands)
    d = Deck()
    for i in range(51):
        d.add_card(card_from_num(i))
        pass
    d.shuffle()
    fc.future_cards_from_deck(d)
    print(fc.future_cards)
    print(hands)
    pass

if __name__ == '__main__':
    main()
    pass
