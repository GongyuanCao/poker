import numpy as np
import math


class Point:
    """a point in a Cartesian plane"""
    def __init__(self, a_in=0, b_in=0):
        self.x = a_in
        self.y = b_in
        pass

    def __str__(self):
        return ('({0}, {1})'.format(self.x, self.y))

    def __repr__(self):
        return ('Point({0}, {1})'.format(self.x, self.y))

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        pass

    def distance_from(self, pt):
        p1 = np.array([self.x, self.y])
        p2 = np.array([pt.x, pt.y])
        p3 = p2-p1
        p4 = math.hypot(p3[0], p3[1])
        return p4
    pass

def main():
    p = Point()
    pt = Point(2, 3)
    print(Point.__str__(p))
    print(Point.__repr__(p))
    print(Point.move(p, 3, -5))
    print(Point.distance_from(p, pt))
    pass

if __name__ == '__main__':
    main()
    pass
