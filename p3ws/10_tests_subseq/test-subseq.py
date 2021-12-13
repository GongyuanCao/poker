from subseq import maxSeq
import sys


def test(list, a):
    if (maxSeq(list) != a):
        sys.exit(1)
        pass
    return 0

def main():
    test([1, 2, 3], 3)
    test([3, 2, 1], 1)
    test([1, 2, 3, 1], 3)
    test([1, 2, 3, 1, 4], 3)
    test([1, 1, 2, 3], 3)
    test([1, 2, 1, 3, 4, 1, 2, 3, 5], 4)
    test([2], 1)
    test([1, 1, 1], 1)
    test([], 0)
    test([-1, 1], 2)
    test([1, -2], 1)
    
if __name__ == '__main__':
    main()
    pass
