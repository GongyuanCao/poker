from point import Point

def closestPoint(s, p):
    if s == {}:
        return 0
    j = 0
    d = []
    n = []
    for i in s:
        d.append(Point.distance_from(i, p))
        n.append(i)
        j += 1
        pass
    min = d[0]
    ans = n[0]
    for i in range(1, j):
        cur = d[i]
        if cur <= min:
            min = cur
            ans = n[i]
            pass
        pass
    return ans

def main():
    s = [Point(10, 8), Point(12, 5), Point(-20, -30), Point(8, -7), Point(0, 4)]
    p = Point(0, 0)
    print(closestPoint(s, p))
    pass

if __name__ == '__main__':
    main()
    pass
