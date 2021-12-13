from point import Point
import numpy as np
import math


class Circle:
    """this is a circle with points"""
    def __init__(self, a_in=None, b_in=1):
        if a_in == None:
            a_in = Point()
            pass
        if b_in < 0:
            b_in = 0
            pass
        self.c = a_in
        self.r = b_in
        pass

    def __str__(self):
        return ('({0}, {1})'.format(Point.__str__(self.c), self.r))

    def __repr__(self):
        return ('Circle({0}, {1})'.format(Point.__str__(self.c), self.r))

    def move(self, dx, dy):
        Point.move(self.c, dx, dy)
        pass

    def intersection_area(self, other_circle):
        d = Point.distance_from(self.c, other_circle.c)
        if d >= self.r + other_circle.r:
            s = 0
            return s
        if self.r == 0 or other_circle.r == 0:
            s = 0
            return s
        if d <= max(self.r, other_circle.r) - min(self.r, other_circle.r):
            s = math.pi * min(self.r, other_circle.r) * min(self.r,
                                                            other_circle.r)
            return s
        else:
            a1 = math.acos((self.r ** 2 + d ** 2 - other_circle.r ** 2) / (2 * self.r * d))
            a2 = math.acos(((other_circle.r ** 2) + (d ** 2) - (self.r ** 2)) / (2 * other_circle.r * d))
            s = a1 * self.r ** 2 + a2 * other_circle.r ** 2 - self.r * d * math.sin(a1)
            return s
        pass

def main():
    c1 = Circle(Point(0, 1), 1)
    c2 = Circle(Point(1, 0), 1)
    s = Circle.__str__(c1)
    r = Circle.__repr__(c1)
    print(s)
    print(Circle.__str__(c2))
    print(Circle.intersection_area(c1, c2))
    pass

if __name__ == '__main__':
    main()
    pass
