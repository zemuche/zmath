from zmath.core import floatint, floatfrac, eachtofloat,\
    sigma, zsum, fibonacci, fib
from zmath.fraction import Fraction


class Sequence:
    """
    A template for other sequences
    """

    def __init__(self, a1, d, n):
        self.a = a1
        self.d = d
        self.n = n
        self.seq = [None]

    def __repr__(self):
        return ', '.join(str(n) for n in self.seq)

    def __len__(self):
        return len(self.seq)

    def __iter__(self):
        return iter(self.seq)

    def find(self, num):
        return self.seq.index(num)

    def nthterm(self, n):
        if n > self.n:
            raise ValueError("nth out of range")
        return self.seq[n - 1]

    @staticmethod
    def wrap(seqlist, wraptype=str):
        wrap_at = 4 if len(seqlist) > 4 else len(seqlist) + 1
        return ', '.join(wraptype(s) for s in seqlist)


class Arithmetic(Sequence):
    """
    Description:
        An advanced arithmetic sequence toolkit.
    Attributes:
        a - first term of sequence
        d - difference of sequence
        n - number of terms in sequence
        seq - list of arithmetic sequence
        an - last term of sequence
    Methods:
        _sequence - a private generator function to construct the sequence
        nthterm - returns the nth term of the sequence
        series - returns the sum of the sequence
        diff - returns the difference of the sequence
    """

    def __init__(self, a1, d, n):
        super().__init__(a1, d, n)
        self.seq = self._sequence()
        self.an = self.seq[-1]

    def _sequence(self):
        seq = []
        a = self.a - self.d
        for _ in range(self.n):
            a += self.d
            seq.append(Fraction(a))
        return seq

    def series(self):
        return Fraction(self.n * float(self.a + self.an) / 2)


class Harmonic(Sequence):
    """
    Description:
        An advanced harmonic sequence toolkit.
    Attributes:
        a - first term of sequence
        d - difference of sequence
        n - number of terms in sequence
        seq - list of harmonic sequence
        an - last term of sequence
    Methods:
        _sequence - a private generator function to construct the sequence
        nthterm - returns the nth term of the sequence
        series - returns the sum of the sequence
        diff - returns the difference of the sequence
    """

    def __init__(self, a1, d, n):
        super().__init__(a1, d, n)
        self.seq = self._sequence()
        self.an = self.seq[-1]

    def _sequence(self):
        seq = []
        for n in range(self.a, self. a + self.n):
            seq.append(Fraction(1 / (self.d * n)))
        return seq

    def series(self):
        return Fraction(zsum(eachtofloat(self.seq)))


class Geometric(Sequence):
    """
    Description:
        An advanced geometric sequence toolkit.
    Attributes:
        a - first term of sequence
        r - ratio of sequence
        n - number of terms in sequence
        seq - list of geometric sequence
        an - last term of sequence
    Methods:
        _sequence - a private generator function to construct the sequence
        nthterm - returns the nth term of the sequence
        series - returns the sum of the sequence
        ratio - returns the ratio of the sequence
    """

    def __init__(self, a1, r, n):
        super().__init__(a1, r, n)
        self.seq = list(self._sequence())
        self.an = self.seq[-1]

    def _sequence(self):
        seq = []
        a = self.a / self.d
        for _ in range(self.n):
            a *= self.d
            seq.append(Fraction(a))
        return seq

    def series(self):
        return Fraction((self.a * (1 - self.d ** self.n)) / (1 - self.d))


class Power(Sequence):
    """
    Description:
        An advanced power sequence toolkit.
    Attributes:
        p - the power exponent of sequence
        n - number of terms in sequence
        seq - list of square sequence
        an - last term of sequence
    Methods:
        _sequence - a private generator function to construct the sequence
        nthterm - returns the nth term of the sequence
        series - returns the sum of the sequence
    """

    def __init__(self, a1, p, n):
        super().__init__(a1, p, n)
        self.seq = self._sequence()
        self.an = self.seq[-1]

    def _sequence(self):
        seq = []
        for i in range(self.a, self.a + self.n):
            seq.append(Fraction(pow(i, self.d)))
        return seq

    def series(self):
        return Fraction(zsum(self.seq))


class Triangular:
    """
    Description:
        An advanced triangular sequence toolkit.
    Attributes:
        a - first term of sequence
        n - number of terms in sequence
        seq - list of triangular sequence
        an - last term of sequence
    Methods:
        _sequence - a private generator function to construct the sequence
        nthterm - returns the nth term of the sequence
        series - returns the sum of the sequence
    """

    def __init__(self, a1, n):
        self.a = a1
        self.n = n
        self.seq = self._sequence()
        self.an = self.seq[-1]

    def __repr__(self):
        return ', '.join(str(n) for n in self.seq)

    def __iter__(self):
        return iter(self.seq)

    def _sequence(self):
        seq = []
        for n in range(1, self.n + 1):
            seq.append(sigma(n))
        return seq

    def nthterm(self, n):
        if n > self.n:
            raise ValueError("nth out of range")
        return self.seq[n - 1]

    def series(self):
        return floatint((self.n * (self.n + 1) * (self.n + 2)) / 6)


class Fibonacci:
    """
    Description:
        An advanced fibonacci sequence toolkit.
    Attributes:
        n - number of terms in sequence
        seq - list of square sequence
        an - last term of sequence
    Methods:
        _sequence - a private generator function to construct the sequence
        nthterm - returns the nth term of the sequence
        series - returns the sum of the sequence
    """

    def __init__(self, n):
        self.n = n
        self.seq = list(fibonacci(n))
        self.an = self.seq[-1]

    def __repr__(self):
        return ', '.join(str(n) for n in self.seq)

    def __iter__(self):
        return iter(self.seq)

    def nthterm(self, n):
        if n > self.n:
            raise ValueError("nth out of range")
        return self.seq[n - 1]

    def series(self):
        return fib(self.n + 2)[1] - 1


def nth_arithmetic(a, d, n):
    """Return the nth term of the arithmetic sequence A
    with initial value a and difference d."""
    return floatint(a + (n - 1) * d)


def diff(seq):
    """Return the common difference of an arithmetic sequence, or False if not."""
    d = seq[1] - seq[0]
    for i in range(1, len(seq)):
        if not seq[i - 1] + d == seq[i]:
            return False
    return floatfrac(d)


def hdiff(seq):
    """Return the common difference of a harmonic sequence, or False if not."""
    seq = eachtofloat(seq)
    d = 1 / seq[1] - 1 / seq[0]
    for i in range(2, len(seq)):
        cur = 1 / seq[i] - 1 / seq[i - 1]
        if cur != d:
            return False
    return floatfrac(d)


def nth_geometric(a, r, n):
    """Return the nth term of the geometric sequence A with initial value a."""
    return floatint(a * r ** (n - 1))


def ratio(seq):
    """Return the common ration of a geometric sequence, or False if not."""
    if seq[0] == 0:
        return seq[1]
    r = seq[1] / seq[0]
    for i in range(1, len(seq)):
        if not seq[i] / r == seq[i - 1]:
            return False
    return floatfrac(r)


def pratio(seq):
    roots = [None] * len(seq)
    for j, n in enumerate(seq):
        for i in range(10):
            if isinstance(floatint(n ** i), int):
                roots[j] = i


def nth_triangular(n):
    return sigma(n)


def sequence(seq):
    results = {"Arithmetic": diff(seq),
               "Harmonic": hdiff(seq),
               "Geometric": ratio(seq)}
    for k, v in results.items():
        if v:
            print(k + ': ' + str(v))


def allsame(iterable):
    for i in range(len(iterable) - 1):
        if iterable[i] != iterable[i+1]:
            return False
    return True


def main():
    a1 = Arithmetic(1, 1/2, 7)
    h1 = Harmonic(2, 1, 7)
    g1 = Geometric(2, 1/2, 7)
    t1 = Triangular(1, 7)
    p1 = Power(1, 2, 7)
    f1 = Fibonacci(7)
    print(a1, a1.series(), sep='--> ')
    print(h1, h1.series(), sep='--> ')
    print(g1, g1.series(), sep='--> ')
    print(t1, t1.series(), sep='--> ')
    print(p1, p1.series(), sep='--> ')
    print(f1, f1.series(), sep='--> ')


if __name__ == '__main__':
    main()
