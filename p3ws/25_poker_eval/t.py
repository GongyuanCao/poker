from card import Card
from deck import Deck
from evaluate import compare_hands


def main():
    hand1 = Deck()
    hand2 = Deck()
    hand1.add_card(Card('2', 'c'))
    hand1.add_card(Card('2', 'd'))
    hand1.add_card(Card('2', 'h'))
    hand1.add_card(Card('3', 'h'))
    hand1.add_card(Card('5', 'h'))
    hand1.add_card(Card('4', 'd'))
    hand1.add_card(Card('A', 's'))
    hand2.add_card(Card('2', 'c'))
    hand2.add_card(Card('2', 'd'))
    hand2.add_card(Card('2', 'h'))
    hand2.add_card(Card('4', 'h'))
    hand2.add_card(Card('A', 'h'))
    hand2.add_card(Card('0', 'h'))
    hand2.add_card(Card('J', 'h'))
    a = compare_hands(hand1, hand2)
    a
    if a > 0:
        print('hand 1 win')
    elif a < 0:
        print('hand 2 win')
    else:
        print(tie)
    pass


if __name__ == '__main__':
    main()
    pass

"""
2c 5d 9h 8h 7h 3d As; 2c 5d 9h 8h 7h 0h Jh
4s 3s 8h 2s 9d As 5s; 4s 3s 8h 2s 9d 9h 9s
9d 9h 9s 8c 9c 0h Ah; 9d 9h 9s 8c 9c 0c As
9d 9h 8h 9c 7h 6h 5h; 9d 9h 8h 9c 7h 6c 5c
2s 3s 4s 6s 5h 8s 9h; As 2s 3s 4s 5s 8h 9h
2s 3s 4h 5s 6s 4s 0h; 2s 3s 4h 5s 6s 8d Kh
Kc Ac 2c 3c 2s Qc 7c; Kc Ac 2c As 2s 8c 5c 
"""
