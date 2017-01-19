def factors(n, proper=False):
    """
    Generate factors of n one by one
    :param n:
    :param proper:
    :return: generator object
    """
    limit = n + 1 if not proper else n
    for x in range(1, limit):
        if n % x == 0:
            yield x


def two_sum(nums, target, return_nums=False):
    """
    :type nums: List[int]
    :type target: int
    :type return_nums: bool
    :rtype: tup(int)
    """
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            if return_nums:
                return target - num, num
            else:
                return lookup[target - num], i
        lookup[num] = i
    return None


def armstrong_nums(start, stop=None):
    if start < 1:
        start = 1
    if stop is None:
        start, stop = 1, start
    for num in range(start, stop + 1):
        order = len(str(num))
        res = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            res += digit ** order
            temp //= 10
        if res == num:
            yield num


def happy_nums(start, stop=None):
    if start < 1:
        start = 1
    if stop is None:
        start, stop = 1, start
    for num in range(start, stop + 1):
        temp = num
        tries = 0
        total = 0
        while total != 1 and tries < 1000:
            digits = list(str(temp))
            total = 0
            for digit in digits:
                total += int(digit) ** 2
                temp = total
            if temp == 1:
                yield num
            tries += 1


def isprime(num):
    """Return True if an integer is a prime, False otherwise."""
    prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            prime = False
            break
    return prime


def primes(start, stop=None):
    """Generate primes between a range"""
    if start < 2:
        start = 2
    if stop is None:
        start, stop = 2, start
    for n in range(start, stop + 1):
        prime = True
        for divisor in range(2, n):
            if n % divisor == 0:
                prime = False
                break
        if prime:
            yield n


def prime_sums(n):
    primes = list(primes(n))
    yes = True
    for i in range(4, n + 1, 2):
        if not two_sum(primes, i):
            yes = False
    return yes


def isperfect(n):
    """Return True if an integer is a perfect number; False otherwise."""
    return sum(factors(n, proper=True)) == n


def issuperperfect(n):
    """Return True if an integer is a super perfect number; False otherwise."""
    return sum(factors(sum(factors(n)))) == 2 * n


def perfect_nums(start, stop=None):
    """Generate perfect numbers between a range"""
    if start < 2:
        start = 2
    if stop is None:
        start, stop = 2, start
    for n in range(start, stop + 1):
        if isperfect(n):
            yield n


def superperfect_nums(start, stop=None):
    """Generate super perfect numbers between a range"""
    if start < 2:
        start = 2
    if stop is None:
        start, stop = 2, start
    for n in range(start, stop + 1):
        if issuperperfect(n):
            yield n


def isabundant(n):
    """
    :param n:
    :return: True if n is abundant; False otherwise
    """
    return sum(factors(n, proper=True)) > n


def abundance(n):
    """
    :param n: int
    :return: the abundance of n
    """
    result = sum(factors(n, proper=True)) - n
    if result:
        return result


def abundant_nums(start, stop=None):
    """Generate abundant numbers between a range"""
    if start < 2:
        start = 2
    if stop is None:
        start, stop = 2, start
    for n in range(start, stop + 1):
        if isabundant(n):
            yield n


def main():
    pn = 100
    perfects = list(perfect_nums(pn))
    print(perfects)
    sperfects = list(superperfect_nums(pn))
    print(sperfects)
    abundants = list(abundant_nums(pn))
    print(abundants)


if __name__ == '__main__':
    main()
