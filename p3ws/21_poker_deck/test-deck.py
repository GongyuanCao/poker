from card import Card, card_from_num
from deck import Deck, build_remaining_deck


# write many test cases here!
def main():
    d1 = Deck()
    print(d1.__repr__())
    d1.add_card(Card('0', 's'))
    d1.add_card(Card('A', 'h'))
    d1.sort()
    print(d1.__repr__())
    if d1.contains(Card('A', 'h')):
        print('yes')
        pass
    d2 = Deck()
    d2.add_card(Card('2', 'c'))
    d2.add_card(Card('3', 's'))
    d2.add_card(Card('4', 'h'))
    print(d2.__repr__())
    print(d2.draw())
    print(d2.__repr__())
    d3 = Deck()
    for i in range(52):
        d3.add_card(card_from_num(i))
    print(d3.__repr__())
    ds = [d1, d2, d3]
    big = build_remaining_deck(ds)
    print(big.__repr__())
    return 0


if __name__ == '__main__':
    main()
    pass
