class Card (object):
    '''this is a card'''
    values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    suits = ('c', 'd', 'h', 's')

    def __init__(self, value='?', suit='?'):
        if value == 'J':
            self.value = 11
        elif value == 'Q':
            self.value = 12
        elif value == 'K':
            self.value = 13
        elif value == 'A':
            self.value = 14
        elif value == '?':
            self.value = 0
        elif value == '0':
            self.value = 10
        else:
            self.value = int(value)
            pass
        self.suit = suit
        if self.value == 1:
            raise ValueError('value shall not be 1')
        if len(str(value)) > 1:
            raise ValueError('value not good')
        if self.value == 0 and self.suit != '?':
            raise ValueError('value not match')
        if self.value != 0 and self.suit == '?':
            raise ValueError('value not match')
        #if self.value != 2 or self.value != 3 or self.value != 4 or self.value != 5 or self.value != 6 or self.value != 7 or self.value != 8 or self.value != 9 or self.value != 10 or self.value != 11 or self.value != 12 or self.value != 13 or self.value != 14 or self.value != 0:
        #    raise ValueError('value not good')
        if self.suit == 'c' or self.suit == 'd' or self.suit == 'h' or self.suit == 's' or self.suit == '?':
            pass
        else:
            raise ValueError('suit not good')

    def __str__(self):
        if self.value == 14:
            value = 'A'
        elif self.value == 13:
            value = 'K'
        elif self.value == 12:
            value = 'Q'
        elif self.value == 11:
            value = 'J'
        elif self.value == 10:
            value = '0'
        elif self.value == 0:
            value = '?'
        else:
            value = str(self.value)
        return str(value+self.suit)

    def __repr__(self):
        s = ('Card(%s)' % (self.__str__()))
        return s

    def __eq__(self, other):
        if self.value != other.value:
            return False
        if self.value == other.value:
            if self.suit != other.suit:
                return False
            else:
                return True

    def __lt__(self, other):
        c = 1
        d = 2
        h = 3
        s = 4
        if self.value < other.value:
            return True
        elif self.value == other.value and self.suit < other.suit:
            return True
        else:
            return False

    def is_known(self):
        if self.value <= 14 and self.value >= 2:
            if self.suit == 'c':
                return True
            elif self.suit == 'd':
                return True
            elif self.suit == 's':
                return True
            elif self.suit == 'h':
                return True
            else:
                return False
        else:
            return False

def card_from_num(num):
    if num > 51 or num < 0:
        raise ValueError('value shall be [0, 51]!')
    if num >= 0 and num <= 12:
        suit = 'c'
        value = int(num+2)
        pass
    if num > 12 and num <= 25:
        suit = 'd'
        value = int(num-11)
        pass
    if num > 25 and num <= 38:
        suit = 'h'
        value = int(num-24)
        pass
    if num > 38 and num <= 51:
        suit = 's'
        value = int(num-37)
        pass
    if value == 14:
        value = 'A'
    elif value == 13:
        value = 'K'
    elif value == 12:
        value = 'Q'
    elif value == 11:
        value = 'J'
    elif value == 10:
        value = '0'
    elif value == 0:
        value = '?'
    else:
        value = str(value)
    c = Card(value, suit)
    return c
