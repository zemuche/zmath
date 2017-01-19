import math
from collections import namedtuple
from zmath.core import zsum, prod, floatint

Coordinate = namedtuple("Coordinate", ['x', 'y'])
XIntercept = namedtuple("X_Intercept", ['x', 'y'])
YIntercept = namedtuple("Y_Intercept", ['x', 'y'])


class Circle:
    """An advanced circle analytic toolkit"""

    version = '0.1'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2.0


class Polygon:
    def __init__(self, sides):
        self.n = sides
        self.sides = [0 for _ in range(sides)]
        # self.input_sides()

    def __repr__(self):
        txt = ["Side "+str(i+1) + ': ' + str(s)
               for i, s in enumerate(self.sides)]
        return '\n'.join(str(s) for s in txt)

    def __len__(self):
        return len(self.sides)

    def input_sides(self):
        for i in range(len(self.sides)):
            self.sides[i] = floatint(float(input("Enter side " +
                                                 str(i+1) + ": ")))

    def perimeter(self):
        return floatint(sum(self.sides))


class Triangle(Polygon):
    def __init__(self):
        super().__init__(sides=3)

    def area(self):
        a, b, c = self.sides
        s = sum(self.sides) / 2
        a = floatint((s * (s - a) * (s - b) * (s - c)) ** 0.5)
        return a


class Rectangle(Polygon):
    n = 4

    def __init__(self):
        super().__init__(sides=2)
        self.n = Rectangle.n

    def __len__(self):
        return self.n

    def perimeter(self):
        w, l = self.sides
        return floatint(2 * (w + l))

    def area(self):
        w, l = self.sides
        return floatint(w * l)


class Square(Polygon):
    n = 4

    def __init__(self):
        super().__init__(sides=1)
        self.n = Square.n

    def __len__(self):
        return self.n

    def perimeter(self):
        return floatint(self.sides[0] * self.n)

    def area(self):
        return floatint(self.sides[0] ** 2)


def circum(r):
    """Return the circumference of a circle with radius r."""
    return 2 * math.pi * r


def circlearea(r):
    """Return the area of a circle with radius r."""
    return round(math.pi * r ** 2, 2)


def arclen(r, a):
    """Return the arc length of a circle with radius r and angle a."""
    return round((a / 360) * circum(r), 2)


def sector_area(r, a):
    """Return the sector area of a circle with radius r and arc angle a."""
    return round((a / 360) * circlearea(r), 2)


def segment_area(r, a):
    """Return the segment area of a circle with radius r and arc angle a."""
    return round(sector_area(r, a) - ((r ** 2) * math.sin(a) / 2), 2)


def triarea(*sides):
    """Return the area of a right triangle or a regular triangle."""
    sides = [x for x in sides]
    if len(sides) == 2:
        return prod(sides) * 0.5
    elif len(sides) == 3:
        a, b, c = sides
        s = zsum(sides) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return floatint(area)
    else:
        raise ValueError("area() for triangle needs 3 or 2 "
                         "(for right triangles) sides.")


def rectarea(*sides):
    """Return the area of a square or a rectangle."""
    sides = [x for x in sides]
    if len(sides) == 1:
        s = sides[0]
        return s * s
    elif len(sides) == 2:
        a, b = sides
        return a * b
    else:
        raise ValueError("area() for rectangle needs 1 (for square) or 2 sides.")


def perim(*sides):
    """Return the perimeter of any polygon (at least 3 sides)."""
    sides = [s for s in sides]
    if len(sides) > 2:
        return zsum(sides)
    else:
        raise ValueError("perimeter() needs at least 3 sides.")


def dist(a, b=Coordinate(0, 0)):
    """
    Return the distance of two coordinate points.
    if no value provided for b, distance will be between a and origin.
    """
    if not (isinstance(a, Coordinate) or isinstance(b, Coordinate)):
        raise TypeError("distance() requires Coordinate types")
    x_diff_sq = (a.x - b.x) ** 2
    y_diff_sq = (a.y - b.y) ** 2
    return floatint((x_diff_sq + y_diff_sq) ** 0.5)


def midpoint(a, b=Coordinate(0, 0)):
    """
    Return the midpoint of two coordinate points.
    if no value provided for b, midpoint will be between a and origin.
    """
    x_value = (a.x + b.x) / 2
    y_value = (a.y + b.y) / 2
    mid_point = floatint(x_value), floatint(y_value)
    return mid_point


def slope(a, b=Coordinate(0, 0)):
    """Return the slope of two coordinate points."""
    if not (isinstance(a, Coordinate) or isinstance(b, Coordinate)):
        raise TypeError("slope() requires Coordinate types")
    if a.x != b.x:
        x_diff = a.x - b.x
        y_diff = a.y - b.y
        return floatint(y_diff / x_diff, 4)
    raise ValueError("undefined slope: " + str(a) + ' ' + str(b))


def intercepts(a, b=Coordinate(0, 0)):
    m = float(slope(a, b))
    y_int = floatint((a.y - (m * a.x)))
    x_int = floatint(((0 - y_int) / m))
    y_int = YIntercept(0, y_int)
    x_int = XIntercept(x_int, 0)
    return x_int, y_int


def equation(a, b=Coordinate(0, 0)):
    """Return an equation in the form of mx + b by taking two Coordinates."""
    m = floatint(slope(a, b))
    b = floatint(a.y - (m * a.x))
    equation1 = "y = {0}x + {1}".format(m, b)
    equation2 = "y = {0}x {1}".format(m, b)
    equation3 = "y = {0}x".format(m)
    if b >= 0:
        if b == 0:
            return equation3
        return equation1
    return equation2


def coordinate_tests():
    print("\n\n-------------COORDINATE TESTS")
    pt1, pt2 = Coordinate(4, 2), Coordinate(0, 0)
    xyints = intercepts(pt1, pt2)
    print("Distance:".rjust(12), dist(pt1, pt2))
    print("Midpoint:".rjust(12), midpoint(pt1, pt2))
    print("Slope:".rjust(12), slope(pt1, pt2))
    print("Intercepts:".rjust(12), ', '.join(str(a) for a in xyints))
    print("Equation:".rjust(12), equation(pt1, pt2))


def area_tests():
    print("Perimeter", perim(3, 4, 5, 8))
    print("Triarea", triarea(3, 4, 5))
    print("Sector Area", sector_area(6, 120))
    print("Segment Area", segment_area(6, 120))
    print("Arc Length", arclen(6, 120))


def polygon_tests():
    print("\n\n-------------SQUARE TESTS")
    sq = Square()
    sq.input_sides()
    print(sq)
    print(sq.perimeter())
    print(sq.area())

    print("\n\n-------------TRIANGLE TESTS")
    t = Triangle()
    t.input_sides()
    print(t)
    print(t.perimeter())
    print(t.area())


def circle_test():
    from random import random, seed

    seed(8346345)
    print("\n\n-------------CIRCLE TESTS")
    print("Using Circuitouos version", Circle.version)
    n = 10
    circles = [Circle(random()) for _ in range(n)]
    print("The average area of", n, "random circles:")
    ave = sum([c.area() for c in circles]) / n
    print(ave)


def main():
    coordinate_tests()
    # area_tests()
    # polygon_tests()
    # circle_test()


if __name__ == '__main__':
    main()
