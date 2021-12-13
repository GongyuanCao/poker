from card import Card, card_from_num


# write all of your test cases here, then run it as python3 test-card.py
def main():
    # test default constructed card
    t1 = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
    for i in range(13):
        c = Card(t1[i], 's')
        print(c)
        pass
    c1 = Card()
    print(c1)
    # test constructor
    c2 = Card('0', 's')
    # test str and repr
    print(c2)
    print(c2.__str__())
    c2.__repr__()
    # test eq and lt
    c3 = Card('A', 's')
    c3.__repr__()
    c4 = Card('J', 'c')
    c4.__repr__()
    c5 = Card('Q', 'h')
    c5.__repr__()
    if c3.__eq__(c2):
        print('c3 = c2')
        pass
    if c4.__lt__(c5):
        print('c4 < c5')
    c1 = Card('K', 'd')
    c2 = Card('2', 'h')
    if c1.__eq__(c2):
        print('yes')
    if c2.__lt__(c1):
        print('no')
    # test card_from_num (try building a full deck)
    for i in range(51):
        c = card_from_num(i)
        print(c.__str__())
        pass
    # error cases
    # invalid value
    #c = Card(20, 's')
    #print(c)
    # invalid suit
    #c = Card(1, 'as')
    #print(c)
    # invalid inputs to card_from_num
    #c = card_from_num(99)
    return 0


if __name__ == '__main__':
    main()
    pass
