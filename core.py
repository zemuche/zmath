import math
from functools import reduce
from zmath.fraction import Fraction

pi = 3.141592653589793
e = 2.718281828

others = ['log', 'log2', 'log10']
ops = ['+', '*', '-', '/', '//', '**', '^', '%', '!', '~', ',']
ops += others


def add(a, b): return a + b


def sub(a, b): return a - b


def mul(a, b): return a * b


def div(a, b): return a / b


def intdiv(a, b): return a // b


def mod(a, b): return a % b


def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


def precedence(c):
    if c in ['(']:
        return 1
    elif c in ['+', '-']:
        return 2
    elif c in ['*', '/', '//', '%']:
        return 3
    elif c in ['**', '^']:
        return 4
    elif c in ['!', '~'] + others:
        return 5


def is_op(c):
    if c != '':
        return c in ops
    else:
        return False


def isnum(c):
    if c != '':
        for i in list(str(c)):
            if i not in "0123456789.":
                return False
        return True
    else:
        return False


def calc(op, num1, num2=None, show_steps=False):
    operators = {'+': add, '*': mul, '-': sub, '/': div, '//': intdiv,
                 '**': pow, '^': pow, '%': mod, '!': fact, '~': sigma,
                 'log10': math.log10, 'log2': math.log2, 'log': math.log}
    if num2 is None:
        answer = floatint(operators[op](float(num1)))
        if show_steps:
            if op in others:
                print(op + '(' + wrap(num1) + ')', '=', answer)
            else:
                print(wrap(num1) + op, '=', answer)
    else:
        answer = floatint(operators[op](float(num1), float(num2)))
        if show_steps:
            print(wrap(num1), op, wrap(num2), '=', answer)
    return answer


def prod(numbers, start=0, end=None, exp=1):
    """Return the product of a list of numbers.
    Optional arguments to restrict product within a range."""
    if end is None:
        end = len(numbers)

    res = 1
    for n in numbers[start:end]:
        res *= n ** exp
    return res


def zsum(numbers, start=0, end=None, exp=1):
    """Return the (power) sum of a list of numbers.
    Optional arguments to restrict sum within a range."""
    if end is None:
        end = len(numbers)
    res = 0
    for n in numbers[start:end]:
        res += n ** exp
    return res


def zsum2(*args):
    res = 0
    for arg in args:
        res += arg
    return res


def ave(*args):
    """Return the average value of a collection."""
    return sum(args) / len(args)


def eachtoint(iterable):
    """Takes an iterable as an argument and returns a
    list of each item converted to an integer"""
    return list(map(int, iterable))


def eachtofloat(iterable):
    """Takes an iterable as an argument and returns a
    list of each item converted to a float"""
    return list(map(float, iterable))


def floatint(num, rnd=None):
    """Return the integer of a number if the number only has
    zeroes after the decimal."""
    if isinstance(num, float) and num.is_integer():
        return int(num)
    else:
        if rnd is None:
            return num
        return round(num, ndigits=rnd)


def eachtofrac(collection):
    """Takes an iterable as an argument and returns a
    list of each item converted to a fraction"""
    return [Fraction(c) for c in collection]


def floatfrac(num):
    """Return the fraction of a floating point number."""
    if isinstance(num, float) or isinstance(num, int):
        return Fraction(num)
    else:
        return num


def primes(limit):
    """Generate all primes up to n using the sieve of Atkin"""
    # result = [2, 3]
    file = open("primes"+str(limit)+".txt", 'w')
    sieve = [False] * (limit + 1)
    for x in range(1, int(limit ** 0.5) + 1):
        for y in range(1, int(limit ** 0.5) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(limit ** 0.5)):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False
    for p in range(5, limit):
        if sieve[p]:
            file.write(str(p) + '\n')
            # result.append(p)
    # return result


def isprime(num):
    """Return True if an integer is a prime, False otherwise."""
    prime = True
    for divisor in range(2, math.ceil(num ** 0.5) + 1):
        if num % divisor == 0:
            prime = False
            break
    return prime


def primefactors(n):
    """Return the two prime factors of n"""
    for factor in range(2, math.ceil(n ** 0.5) + 1):
        if isprime(factor):
            second = floatint(n / factor)
            if isinstance(second, int) and isprime(second):
                return factor, second


def _gcd(a, b):
    """Return the greatest common divisor of a and b, iteratively."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def gcd(*args):
    """Return the greatest common divisor of args using helper function."""
    return reduce(_gcd, args)


def _lcm(a, b):
    """Return the least common multiple of a and b, iteratively."""
    return a * b // gcd(a, b)


def lcm(*args):
    """Return the least common multiple of args."""
    return reduce(_lcm, args)


def fibonacci(n):
    """Generate the first n fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib(n):
    """Return pair of fibonacci numbers F(n) and F(n-1)"""
    if n <= 1:
        return n, 0
    else:
        a, b = fib(n - 1)
        return a + b, a


def fact(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return floatint(res)


def fact2(n):
    """Return the factorial of n (n!)"""
    if n == 1:
        return 1
    else:
        return n * fact2(n - 1)


def factors(n, proper=False):
    """
    Generate factors of n one by one
    :param n:
    :param proper:
    :return: generator object
    """
    for x in range(1, n // 2 + 1):
        if n % x == 0:
            yield x
    if not proper:
        yield n


def filterfactors(sequence, n):
    """Return filtered list of the factors of n from the sequence."""
    return list(filter(lambda x: not n % x, sequence))


def arefactors(sequence, n):
    """Return True if all numbers in the sequence are factors of n."""
    for x in sequence:
        if n % x != 0:
            return False
    return True


def multiples(n, limit):
    """Generate multiples of n up to the limit one by one"""
    for x in range(n, limit + 1):
        if x % n == 0:
            yield x


def filtermultiples(sequence, n):
    """Return filtered list of the multiples of n from the sequence."""
    return list(filter(lambda x: not x % n, sequence))


def aremultiples(sequence, n):
    """Return True if all numbers in the sequence are multiples of n."""
    for x in sequence:
        if x % n != 0:
            return False
    return True


def triples(limit):
    for m in range(1, int(limit ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 and gcd(m, n) == 1:
                c = m ** 2 + n ** 2
                if c <= limit:
                    a = m ** 2 - n ** 2
                    b = 2 * m * n
                    yield a, b, c


def sigma(n):
    """Return the summation of n."""
    if n > 0:
        return floatint(float((n * (n + 1)) / 2))
    else:
        return 0


def sqsigma(n):
    """Return the summation of i^2 for i in range n."""
    return floatint(float((n * (n + 1) * (2 * n + 1)) / 6))


def cusigma(n):
    """Return the summation of i^3 for i in range n."""
    return floatint(float((n ** 2 * (n + 1) ** 2) / 4))


def sqroot(n):
    epsilon = 0.0001
    guess = n / 2.0000
    while abs(guess ** 2 - n) >= epsilon:
        guess -= (((guess ** 2) - n) / (2 * guess))
    return floatint(round(guess, 5))


def nthroot(x, n):
    """
    :param x: radicand
    :param n: root
    :return: n-th root of x
    """
    return floatint(round(float(x ** (1 / n)), 5))


def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


def printpowof(exp, limit):
    """
    Prints a table of logs of 2.
    :param exp: determines the log base
    :param limit: determines when to stop finding logn
    :return:
    """
    print(" N\t\tn^{}".format(exp))
    x = 1
    while x <= limit:
        res = floatint(pow(x, exp))
        print("{0:2}\t\t{1}".format(x, res))
        x += 1


def printbaseof(base, limit):
    """
    Prints a table of logs of 2.
    :param base: determines the log base
    :param limit: determines when to stop finding logn
    :return:
    """
    print(" N\t\t{}^n".format(base))
    n = 1
    while n <= limit:
        res = floatint(pow(base, n))
        print("{0:2}\t\t{1}".format(n, res))
        n += 1


def makelogof(n):
    """
    Make a log function
    :param n: determines the log base
    :return: a log function that has x as parameter and n as the base
    """

    def log_of(x):
        return math.log(x, n)

    return log_of


def printlogsof(base, limit):
    """
    Prints a table of logs of 2.
    :param base: determines the log base
    :param limit: determines when to stop finding logn
    :return:
    """
    logofn = makelogof(base)
    print("Numbers\t\tLog(n)")
    n = 1
    while n <= limit:
        res = floatint(logofn(n))
        print("{0:7}\t\t{1:2}".format(n, res))
        n *= base


def multtable(limit):
    """
    Prints a multiplication table with the limit as the height and width
    """
    for x in range(1, limit + 1):
        for y in range(1, x + 1):
            print(str(x * y).ljust(5), end='')
        print()


def radian(deg):
    """Return the radian of degree deg."""
    from zmath.fraction import Fraction
    deg = str(deg).rstrip('°')
    rad = Fraction(int(deg), 180)
    return str(rad) + chr(960)


def degree(rad):
    """Return the degree of radian rad."""
    from zmath.fraction import Fraction
    if isinstance(rad, str):
        numer, denom = rad.rstrip('π').split('/')
        deg = Fraction(int(numer), int(denom))
    else:
        deg = Fraction(rad)
    return str(deg * 180) + chr(176)


def wrap(x, n=5, length=10):
    if len(str(x)) >= length:
        if isinstance(x, int) or isinstance(x, float):
            return str(round(x, n)) + '..'
        elif isinstance(x, list):
            x = ' '.join(str(a) for a in x)
        return str(x)[:n] + '..'
    return str(x)


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def read_primes(filename):
    with open(filename) as file:
        for line in file:
            yield line


def permutations(iterable, r=None):
    from challenges.infix import evaluate
    n = len(iterable)
    k = len(iterable) if r is None else r
    exp = "n! / (n - k)!"
    return evaluate(exp, variables=locals())


def combinations(iterable, r=None):
    from challenges.infix import evaluate
    n = len(iterable)
    k = len(iterable) if r is None else r
    exp = "n! / (n - k)! / k!"
    return evaluate(exp, variables=locals())


def main():
    from time import time
    import os
    # rad1 = radian(225)
    # print(rad1, end=' ')
    # deg1 = degree(1 / 4)
    # print(deg1, end=' ')
    # rad2 = radian(90)
    # print(rad2, end=' ')
    # deg2 = degree(rad1)
    # print(deg2, end=' ')

    # a = [9, -8, -7]
    # agcd = gcd(*a)
    # print(agcd)
    # print(a, list(map(lambda x: x // agcd, a)))
    # alcm = lcm(*a)
    # print(alcm)
    # print(a, list(map(lambda x: alcm // x, a)))
    # print(sigma(20))
    # print(pow(4, 0.5))

    start = time()

    print(time() - start)
    # mytriples = sorted(triples(50), key=lambda *triple: sum(*triple))
    # for t in mytriples:
    #     print(t)
    # print(permutations(range(8), 3))
    # print(combinations(range(8), 3))


if __name__ == "__main__":
    main()
