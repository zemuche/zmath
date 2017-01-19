# from pprint import pprint
from zmath.core import prod, zsum, floatint
from dictionary import count_items
from operator import itemgetter


def hmean(numbers):
    """Return the harmonic mean of numbers."""
    return floatint(pmean(numbers, exp=-1))


def gmean(numbers):
    """Return the geometric mean of numbers."""
    return floatint(prod(numbers) ** (1 / len(numbers)), rnd=2)


def amean(numbers):
    """Return the arithmetic mean of numbers."""
    # return round(sum(numbers) / len(numbers), 2)
    return pmean(numbers, exp=1)


def qmean(numbers):
    """Return the quadratic mean of numbers."""
    return pmean(numbers, exp=2)


def cmean(numbers):
    """Return the quadratic mean of numbers."""
    return pmean(numbers, exp=3)


def pmean(numbers, exp=1):
    """Return the power (generalized) mean of numbers"""
    return floatint((zsum(numbers, exp=exp) /
                     len(numbers)) ** (1 / exp), rnd=3)


def wmean(numbers):
    """Return the weighted mean of numbers."""
    pass


def mode(numbers):
    return max(numbers, key=numbers.count)


def mode2(numbers):
    """Return the most occurring number from numbers."""
    return max(count_items(numbers).items(), key=itemgetter(1, 0))[0]


def median(numbers):
    """Return the middle number after sorting numbers."""
    numbers = sorted(numbers)
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return amean([numbers[mid], numbers[mid - 1]])
    else:
        return numbers[len(numbers) // 2]


if __name__ == '__main__':
    nums = [10, 10, 8, 1, 8, 3, 7, 5, 3, 7, 9, 11, 11, 17, 6, 6, 9]
    print(sorted(nums))
    print("min".ljust(10), min(nums))
    print("hmean".ljust(10), hmean(nums))
    print("gmean".ljust(10), gmean(nums))
    print("amean".ljust(10), amean(nums))
    print("qmean".ljust(10), qmean(nums))
    print("cmean".ljust(10), cmean(nums))
    print("median".ljust(10), median(nums))
    print("mode".ljust(10), mode(nums))
    print("mode".ljust(10), mode2(nums))
    print("max".ljust(10), max(nums))
