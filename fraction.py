import math
superscripts = {"0": chr(186), "1": chr(185), "2": chr(178), "3": chr(179),
                "4": chr(8308), "5": chr(8309), "6": chr(8310),
                "7": chr(8311), "8": chr(8312), "9": chr(8313)}
subscripts = {"0": chr(8320), "1": chr(8321), "2": chr(8322), "3": chr(8323),
              "4": chr(8324), "5": chr(8325), "6": chr(8326), "7": chr(8327),
              "8": chr(8328), "9": chr(8329)}


class Fraction:
    def __init__(self, numer, denom=1, mixed=False):
        self.mixed = mixed
        if isinstance(numer, float):
            numer, denom = self.__converter(numer)
        if numer < 0 and denom < 0:
            numer *= -1
            denom *= -1
        g = math.gcd(numer, denom)
        self._numer = numer // g
        self._denom = denom // g
        if self._denom == 0:
            print("0 can't be in the denominator")

    @property
    def numer(self):
        return self._numer

    @numer.setter
    def numer(self, new_numer):
        self._numer = new_numer

    @property
    def denom(self):
        return self._denom

    @denom.setter
    def denom(self, new_denom):
        self._denom = new_denom

    def __str__(self):
        regular = superscript(self.numer) + chr(8260) + \
                  subscript(self.denom)
        if self.numer == self.denom or self.denom == 1:
            return str(self.numer)
        elif self.mixed:
            if abs(self.numer) > abs(self.denom):
                whole = self.numer // self.denom
                self.numer %= self.denom
                if self.numer / self.denom < 0.0000000001:
                    self.numer = 0
                if self.numer == 0:
                    return str(whole)
                else:
                    return str(whole) + superscript(abs(self.numer)) + \
                           '/' + subscript(self.denom)
        else:
            return regular

    def __int__(self):
        return self.numer // self.denom

    def __float__(self):
        return self.numer / self.denom

    def __round__(self, n=None):
        return round(float(self), n)

    def __abs__(self):
        return Fraction(abs(self.numer), abs(self.denom))

    def __add__(self, other):
        other = self.convert_to_fraction(other)
        numer_new = other.denom * self.numer + other.numer * self.denom
        denom_new = other.denom * self.denom
        return Fraction(numer_new, denom_new)
    __radd__ = __add__

    def __sub__(self, other):
        other = self.convert_to_fraction(other)
        numer_new = self.numer * other.denom - other.numer * self.denom
        denom_new = self.denom * other.denom
        return Fraction(numer_new, denom_new)

    def __rsub__(self, other):
        other = self.convert_to_fraction(other)
        numer_new = -(self.numer * other.denom - other.numer * self.denom)
        denom_new = self.denom * other.denom
        return Fraction(numer_new, denom_new)

    def __mul__(self, other):
        other = self.convert_to_fraction(other)
        numer_new = self.numer * other.numer
        denom_new = self.denom * other.denom
        return Fraction(numer_new, denom_new)
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.convert_to_fraction(other)
        numer_new = self.numer * other.denom
        denom_new = self.denom * other.numer
        return Fraction(numer_new, denom_new)
    __floordiv__ = __truediv__

    def __rtruediv__(self, other):
        other = self.convert_to_fraction(other)
        numer_new = other.numer * self.denom
        denom_new = other.denom * self.numer
        return Fraction(numer_new, denom_new)
    __rfloordiv__ = __rtruediv__

    def __pow__(self, power, modulo=None):
        return Fraction(self.numer ** float(power) / self.denom ** float(power))

    def __gt__(self, other):
        other = self.convert_to_fraction(other)
        diff = self.numer * other.denom - self.denom * other.numer
        if diff < 0:
            return str(self) + " < " + str(other)
        if diff > 0:
            return str(self) + " > " + str(other)
        return str(self) + " = " + str(other)

    def convert_to_fraction(self, other):
        if isinstance(other, int):
            return Fraction(other)
        elif isinstance(other, float):
            numer, denom = self.__converter(other)
            return Fraction(numer, denom)
        elif isinstance(other, Fraction):
            return other
        else:
            message = "expected type \'Fraction\', got " + str(type(other))
            raise TypeError(message)

    @staticmethod
    def __converter(decimal):
        return decimal_ratios(decimal)

    def superscript(self):
        return superscript(self.numer)

    def subscript(self):
        return subscript(self.denom)


def superscript(num):
    return ''.join(superscripts[n] for n in str(num))


def subscript(num):
    return ''.join(subscripts[n] for n in str(num))


def floatfrac(num):
    """Return the fraction of a floating point number."""
    if isinstance(num, float) or isinstance(num, int):
        return Fraction(num)
    else:
        return num


def decimal_ratios(x, repeat=None):
    from zmath.core import floatint
    for n in range(1, 10000):
        numer = floatint(x * n)
        if isinstance(numer, int):
            return numer, n
    if repeat is None:
        repeat = 5
    mult = 10 ** repeat
    numer = round(mult * x - x)
    return numer, mult - 1


def repeat_pattern(x):
    if len(str(x)) > 10:
        dec = str(x - int(x))
        dec = dec[3:14]
        for i in range(1, 4):
            pattern = True
            for j in range(i, len(dec), i):
                if dec[j - i] != dec[j]:
                    pattern = False
                    break
            if pattern:
                return i
    return False


def convert_any_decimal(decimal):
    length = len(str(decimal)) - 1
    multiplier = pow(10, length - 1)
    numer = int(decimal * multiplier)
    denom = multiplier
    return numer, denom


def main():
    f1 = Fraction(0.5)
    f2 = Fraction(2/3)
    f3 = Fraction(-4, -9)
    f4 = Fraction(1, 27)
    f1_sqrd = f1 ** 2
    f2_cubed = f2 ** 3
    f3_sqrt = f3 ** f1
    f4_cbrt = f4 ** f3_sqrt
    print(f1, f2, f3, f4)
    print(f1_sqrd, f2_cubed, f3_sqrt, f4_cbrt)

    f1 *= 5
    f1.mixed = True
    print(f1)


if __name__ == "__main__":
    main()
