def maxSeq(list):
    flag = [0 for n in range(len(list) + 1)]
    big = -9999
    if list == None:
        return flag[0]
    if list == []:
        return flag[0]
    for i in range(1, len(list) + 1):
        cur = list[i-1]
        if cur > big:
            flag[i] = flag[i-1] + 1
            big = cur
            pass
        else:
            flag[i] = 1
            big = cur
            pass
        pass
    ans = max(flag)
    return ans

def test(list, a):
    if (maxSeq(list) != a):
        print('wrong {0:2d}'.format(a))
        m = maxSeq(list)
        print(m)
    return 0

def main():
    test([1, 2, 3], 3)
    test([3, 2, 1], 1)
    test([1, 2, 3, 4, 1], 4)
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
