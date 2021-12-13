#!/usr/local/bin/python3

import sys
from future import FutureCards
from pinput import read_input
from deck import build_remaining_deck, Deck
from evaluate import compare_hands
from card import Card

# provided
def print_results(wins, n):
    for i in range(0, len(wins) - 1):
        print('Hand {} won {} / {} times'.format(i, wins[i], n))
        pass
    print('and there were {} ties'.format(wins[len(wins) - 1]))
    pass

def montecarlo(hands, rdeck, fc, time):
    win = []
    for i in range(len(hands)+1):
        win.append(0)
        pass
    for i in range(time):
#        for k in range(len(fc.future_cards)):
        rdeck.shuffle()
        fc.future_cards_from_deck(rdeck)
#        print(hands)
        max = []
        max.append(hands[0])
        mn = 0
        for j in range(1, len(hands)):
            if compare_hands(hands[j], max[-1]) > 0:
                max = []
                max.append(hands[j])
                mn = j
                pass
            elif compare_hands(hands[j], max[-1]) == 0:
                max.append(hands[j])
                pass
            pass
        if len(max) > 1:
            win[-1] += 1
        else:
            win[mn] += 1
            pass
#        print(mn)
#        print(win)
        pass
    return win

def main():
    # get count of command line arguments
    argc = len(sys.argv)
    # check user input
    if argc == 2:
        time = 10000
        pass
    elif argc == 3:
        time = int(sys.argv[2])
        pass
    elif argc != 3 and argc != 2:
        raise ValueError('incorrect parameters')
    # read from file
    fname = sys.argv[1]
    fc = FutureCards()
    hands = read_input(fname, fc)
    rdeck = build_remaining_deck(hands)
    # do monte carlos
    win = montecarlo(hands, rdeck, fc, time)
    # print results
    print_results(win, time)
    pass

if __name__ == '__main__':
    main()
