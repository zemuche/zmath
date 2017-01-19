import math
from zmath.fraction import Fraction


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        distance = round(math.sqrt(x_diff_sq + y_diff_sq), 2)
        return Fraction(distance).__str__(True)

    def midpoint(self, other):
        x_value = (self.x - other.x)/2
        y_value = (self.y - other.y)/2
        midpoint = (Fraction(x_value).__str__(True),
                    Fraction(y_value).__str__(True))
        return midpoint

    def slope(self, other):
        rise = self.y - other.y
        run = self.x - other.x
        slope = rise / run
        return Fraction(slope)

    def intercepts(self, other):
        m = self.slope(other)
        y_intercept = round((self.y - (m * self.x)), 2)
        x_intercept = round(((0 - y_intercept) / m), 2)
        return (str(Fraction(x_intercept)), 0), (0, str(Fraction(y_intercept)))

    def equation(self, other):
        m = self.slope(other)
        b = round((self.y - (m * self.x)), 2)
        equation1 = "y = {0}x + {1}".format(m, b)
        equation2 = "y = {0}x {1}".format(m, b)
        equation3 = "y = {0}x".format(m)
        if b >= 0:
            if b == 0:
                return equation3
            return equation1
        return equation2


def main():
    a = Coordinate(4, 2)
    b = Coordinate(0, 0)
    print("Points: {}, {}".format(a, b))
    print("Slope: {}".format(a.slope(b)))
    print("Midpoint: {}".format(a.midpoint(b)))
    print("Distance: {}".format(a.distance(b)))
    print("Intercepts: {}".format(a.intercepts(b)))
    print("Equation: {}".format(a.equation(b)))


if __name__ == '__main__':
    main()
