from zmath.core import floatint, eachtofloat
from math import acos, degrees


class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(self.coordinates)
        except ValueError:
            raise ValueError("The coordinates must be nonempty")
        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self):
        return "Vector{}".format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self, other):
        if len(self.coordinates) == len(other):
            result = [a + b for a, b in zip(self.coordinates, other.coordinates)]
            return Vector(result)
        else:
            return "Cannot add vectors of unequal length"

    def __sub__(self, other):
        if len(self.coordinates) == len(other):
            result = [a - b for a, b in zip(self.coordinates, other.coordinates)]
            return Vector(result)
        else:
            return "Cannot subtract vectors of unequal length"

    def __mul__(self, other):
        try:
            other = float(other)
            result = [c * other for c in self.coordinates]
            return Vector(eachtofloat(result, 3))
        except TypeError:
            raise TypeError("num has to be int or float")

    def dot(self, other):
        result = [a * b for a, b in zip(self.coordinates, other.coordinates)]
        return floatint(sum(result), 3)

    def magnitude(self):
        return floatint(sum(c ** 2 for c in self.coordinates) ** 0.5, 3)

    def direction(self):
        try:
            return self * (1 / self.magnitude())
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

    def arccos(self, other, deg=False):
        res = (self.dot(other)) / (self.magnitude() * other.magnitude())
        result = acos(res)
        if deg:
            return floatint(degrees(result), 3)
        return floatint(result, 3)


def main():
    a = Vector([3.183, -7.627])
    b = Vector([-2.668, 5.319])
    c = Vector([7.35, 0.221, 5.188])
    d = Vector([2.751, 8.259, 3.985])
    print(a.arccos(b))
    print(c.arccos(d, deg=True))


if __name__ == '__main__':
    main()
