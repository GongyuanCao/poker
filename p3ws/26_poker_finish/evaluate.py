from card import Card, card_from_num
from deck import Deck

A = 14
K = 13
Q = 12
J = 11

# finds flush suit
def find_flush(hand):
    flag = {'c': 0, 's': 0, 'd': 0, 'h': 0}
    for i in range(len(hand.cards)):
        flag[hand.cards[i].suit] += 1
        pass
    ans = None
    for key, value in flag.items():
        if value >= 5:
            ans = key
            pass
        pass
    return ans

# makes dictionary of cards values to count of their occurances
def count_values(hand):
    flag = {14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0}
    for i in range(len(hand.cards)):
        flag[hand.cards[i].value] += 1
        pass
    return flag

# uses counts dict and returns a tuple (value with most n of a kind, n)
def get_max_count(hand, counts):
    names = []
    for key, value in counts.items():
        if(value == max(counts.values())):
            names.append(key)
            n = value
            pass
        pass
#    print(names)
    names.sort(reverse=True)
    ans = (names[0], n)
    return ans

# finds index of second pair or returns -1 for no sec pair
def find_secondary_pair(hand, counts, val):
    ind = -1
    for i in range(len(hand.cards)):
        if counts[hand.cards[i].value] == 2 and hand.cards[i].value != val:
            ind = i
            break
        pass
    return ind

# get first index of value in hand
def get_kind_index(hand, value):
    for i in range(len(hand.cards)):
        if hand.cards[i].value == value:
            ind = i
            break
        pass
    return ind

# build hand with n of a kind starting at ind
def build_of_a_kind(hand, n, ind):
    ans = Deck()
    for i in range(n):
        ans.add_card(hand.cards[ind+i])
        pass
    j = 0
    f = 0
    while f < (5-n):
        if hand.cards[j].value != ans.cards[0].value:
            ans.add_card(hand.cards[j])
            j += 1
            f += 1
        elif hand.cards[j].value == hand.cards[j+1].value or hand.cards[j].value == hand.cards[j-1].value:
            j += 1
        pass
    return ans

# adds secondary pair (for full house or two pair)
def add_pair(hand, pi, ans, ai):
#    print(hand)
#    print(pi)
#    print(ans)
#    print(ai)
    if ai == 3:
        ans.cards.pop(3)
        ans.cards.pop(3)
        for i in range(2):
            ans.add_card(hand.cards[pi+i])
            pass
        pass
    if ai == 2:
        ans.cards.pop(2)
        ans.cards.pop(2)
        ans.cards.pop(2)
        ans.add_card(hand.cards[pi])
        ans.add_card(hand.cards[pi+1])
        i = 0
        while hand.cards[i].value == ans.cards[0].value or hand.cards[i].value == ans.cards[2].value:
            i += 1
            pass
        ans.add_card(hand.cards[i])
        pass
    return ans

# helper for is_straight_at
def is_n_length_straight_at(hand, ind, fs, n):
    pass

# helper for is_straight_at
def is_ace_low_straight_at(hand, ind, fs):
    pass

# if fs = None, look for any straight
# if fs = suit, look for straight in suit
# returns -1 for ace-low, 1 for straight, 0 for no straight
def is_straight_at(hand, ind, fs):
    i = 1
    f = ind
    while hand.cards[f] != hand.cards[-1]:
        if hand.cards[f].value == hand.cards[f+1].value:
            f += 1
            pass
        if hand.cards[f] == hand.cards[-1]:
            break
        if hand.cards[f].value == (hand.cards[f+1].value + 1):
            i += 1
            f += 1
            pass
        if i == 5:
            break
        if hand.cards[f] == hand.cards[-1]:
            break
        if hand.cards[f].value > (hand.cards[f+1].value + 1):
            break
        pass
    flag = {'c': 0, 's': 0, 'd': 0, 'h': 0}
    for l in range(ind, f+1):
        flag[hand.cards[l].suit] += 1
        pass
#    print(i)
#ace low
    if hand.cards[ind].value == 14 and hand.cards[-1].value == 2 and i != 5:
        f5 = None
        for k in range(len(hand.cards)):
            if hand.cards[k].value == 5:
                f = k
                f5 = k
                i = 1
                break
            pass
        while hand.cards[f] != hand.cards[-1]:
            if hand.cards[f].value == hand.cards[f+1].value:
                f += 1
            if hand.cards[f] == hand.cards[-1]:
                break
            if hand.cards[f].value == (hand.cards[f+1].value + 1):
                i += 1
                f += 1
                pass
            if i == 4:
                break
            if hand.cards[f] == hand.cards[-1]:
                break
            if hand.cards[f].value > (hand.cards[f+1].value + 1):
                break
                pass
            pass
        if f5 is not None:
            flag = {'c': 0, 's': 0, 'd': 0, 'h': 0}
            for l in range(f5, f+1):
                flag[hand.cards[l].suit] += 1
                pass
            flag[hand.cards[ind].suit] += 1
#    print(flag)
    if fs is None:
        if i >= 5:
            dex = 1
            pass
        elif i == 4:
            if hand.cards[ind].value == 14 and hand.cards[0].value == 14 and hand.cards[f].value == 2:
                dex = -1
            else:
                dex = 0
        else:
            dex = 0
        pass
    if fs is not None:
        if i < 4:
            dex = 0
        elif i >= 5:
            dex = 1
        elif i == 4:
            if hand.cards[ind].value == 14 and hand.cards[f].value == 2:
                dex = -1
            else:
                dex = 0
#        print(flag[fs])
#        print(ind)
#        print(hand.cards[ind].suit)
        if flag[fs] < 5 or fs != hand.cards[ind].suit or fs != hand.cards[f].suit:
            dex = 0
#        print(dex)
    return dex

# provided
def copy_straight(hand, ind, fs, ace_low=False):
    ans = Deck()
    last_card = None
    target_len = 5
    assert not fs or hand.cards[ind].suit == fs
    if ace_low:
        assert hand.cards[ind].value == 14
        last_card = hand.cards[ind]
        target_len = 4
        to_find = 5
        ind += 1
        pass
    else:
        # regular straight
        to_find = hand.cards[ind].value
        pass
    while len(ans.cards) < target_len:
#        print(ind)
#        print(len(hand.cards))
        assert ind < len(hand.cards)
        assert ind >= 0
        if hand.cards[ind].value == to_find:
            if not fs or hand.cards[ind].suit == fs:
                ans.add_card(hand.cards[ind])
                to_find -= 1
                pass
            pass
#        print(hand)
#        print(ans)
        ind += 1
        pass
    if last_card is not None:
        ans.add_card(last_card)
        pass
    assert len(ans.cards) == 5
    return ans

# provided
# looks for a straight (or straight flush if fs is not None)
# calls the student's is_straight_at for each index
# if found, copy_straight returns cards used for straight
def find_straight(hand, fs):
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == 1:
            # straight
            return copy_straight(hand, i, fs)
        pass
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == -1:
            # ace-low straight
            return copy_straight(hand, i, fs, True)
        pass
    return None

# provided
# builds hand with flush suit fs
def build_flush(hand, fs):
    ans = Deck()
    i = 0
    while len(ans.cards) < 5:
        assert i < len(hand.cards)
        if hand.cards[i].suit == fs:
            ans.add_card(hand.cards[i])
            pass
        i += 1
        pass
    return ans

# provided
def evaluate_hand(hand):
    # straight flush
    fs = find_flush(hand)
    straight = find_straight(hand, fs)
    if fs and straight:
        return straight, 'straight flush'
    # four of a kind
    val_counts = count_values(hand)
    v, n = get_max_count(hand, val_counts)
    assert n <= 4
    ind = get_kind_index(hand, v)
    if n == 4:
        return build_of_a_kind(hand, 4, ind), 'four of a kind'
    # full house
    sec_pair = find_secondary_pair(hand, val_counts, v)
    if n == 3 and sec_pair >= 0:
        ans = build_of_a_kind(hand, 3, ind)
        ans = add_pair(hand, sec_pair, ans, 3)
        return ans, 'full house'
    # flush
    if fs:
        return build_flush(hand, fs), 'flush'
    # straight
    if straight:
        return straight, 'straight'
    # three of a kind
    if n == 3:
        return build_of_a_kind(hand, 3, ind), 'three of a kind'
    # two pair
    if n == 2 and sec_pair >=0:
        ans = build_of_a_kind(hand, 2, ind)
        ans = add_pair(hand, sec_pair, ans, 2)
        return ans, 'two pair'
    # pair
    if n == 2:
        return build_of_a_kind(hand, 2, ind), 'pair'
    # high card
    ans = Deck()
    ans.cards = hand.cards[0:5]
    return ans, 'high card'

def num_from_rank(r):
    ranks = ['high card', 'pair', 'two pair', 'three of a kind', \
                 'straight', 'flush', 'full house', \
                 'four of a kind', 'straight flush']
    return ranks.index(r)

# returns positive if hand1 > hand2, 
# 0 for tie, or 
# negative for hand2 > hand 1
def compare_hands(hand1, hand2):
    hand1.cards.sort(reverse=True)
    hand2.cards.sort(reverse=True)
#    print(hand1)
#    print(hand2)
#    print(evaluate_hand(hand1))
#    print(evaluate_hand(hand2))
    if num_from_rank(evaluate_hand(hand1)[1]) > num_from_rank(evaluate_hand(hand2)[1]):
        ans = 1
        pass
    elif num_from_rank(evaluate_hand(hand1)[1]) < num_from_rank(evaluate_hand(hand2)[1]):
        ans = -1
        pass
    elif num_from_rank(evaluate_hand(hand1)[1]) == num_from_rank(evaluate_hand(hand2)[1]):
        ans = 0
        for i in range(0, 5):
            if evaluate_hand(hand1)[0].cards[i].value > evaluate_hand(hand2)[0].cards[i].value:
                ans = 1
                break
            elif evaluate_hand(hand1)[0].cards[i].value < evaluate_hand(hand2)[0].cards[i].value:
                ans = -1
                break
            elif evaluate_hand(hand1)[0].cards[i].value == evaluate_hand(hand2)[0].cards[i].value:
                pass
        pass
    return ans
