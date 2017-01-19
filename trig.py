import math

from zmath.core import floatint
from zmath.fraction import Fraction


def unitcircle():
    print(''.join(label.ljust(10) for label in ["Theta", "Sin", "Cos", "Tan"]))
    print("-"*40)
    print(''.join(str(zeroes).ljust(10) for zeroes in [0, 0, -1, 0]))

    for n in (6, 4, 3, 2, 1, 2/3, 1/2):
        sin = floatint(round(math.sin(math.pi / n), 2))
        cos = floatint(round(math.cos(math.pi / n), 2))
        tan = "Undefined" if cos == 0 else float(round(sin / cos, 2))
        tan = floatint(tan) if isinstance(tan, float) else tan
        fraction = Fraction(1 / n).__str__(True)
        theta = "π/{0}".format(n) if n > 1 else "{}π".format(fraction)
        results = [theta, sin, cos, tan]
        print(''.join(str(r).ljust(10) for r in results))


if __name__ == '__main__':
    unitcircle()
