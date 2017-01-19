import math


class Fraction:
    def __init__(self, numer, denom=1, mixed=False):
        self.mixed = mixed
        if isinstance(numer, float):
            numer, denom = self.__converter(numer)
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
        regular = str(self.numer) + '/' + str(self.denom)
        if self.numer == self.denom or self.denom == 1:
            return str(self.numer)
        if self.mixed:
            if abs(self.numer) > abs(self.denom):
                whole = self.numer // self.denom
                self.numer %= self.denom
                if self.numer / self.denom < 0.0000000001:
                    self.numer = 0
                if self.numer == 0:
                    return str(whole)
                else:
                    return str(whole) + ' ' + str(abs(self.numer)) + \
                           '/' + str(self.denom)
        return regular

    def __int__(self):
        return self.numer // self.denom

    def __float__(self):
        return self.numer / self.denom

    def __round__(self, n=None):
        return round(float(self), n)

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

    def __gt__(self, other):
        other = self.convert_to_fraction(other)
        diff = self.numer * other.denom - self.denom * other.numer
        if diff < 0:
            return str(self) + " < " + str(other)
        if diff > 0:
            return str(self) + " > " + str(other)
        return str(self) + " = " + str(other)

    def sqrt(self):
        numer_new = (self.numer ** 0.5) * (self.denom ** 0.5)
        if numer_new.is_integer():
            return Fraction(int(numer_new), self.denom)
        else:
            return round(numer_new / self.denom, 3)

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
        repeat = repeat_pattern(decimal)
        if repeat:
            return repeat_ratios(decimal, repeat)
        else:
            return convert_any_decimal(decimal)


def repeat_ratios(x, repeat=1):
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


def convert_to_frac(x):
    repeat = repeat_pattern(x)
    if repeat:
        return repeat_ratios(x, repeat)
    else:
        return convert_any_decimal(x)


def main():
    f1 = Fraction(0.5)
    f2 = Fraction(9/2)
    f3 = Fraction(4, 9)
    f4 = Fraction(1/9)
    f3_sqrt = f3.sqrt()
    f4_sqrt = f4.sqrt()
    print(f1, f2, f3, f4, f3_sqrt, f4_sqrt)
    print(f1, int(f1), float(f1))
    print(f2, int(f2), float(f2))
    print(round(f2))


if __name__ == "__main__":
    main()
