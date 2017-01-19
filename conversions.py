from zmath.core import floatint

si_units = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
si_values = [1000, 100, 10, 1, 10, 1 / 100, 1 / 1000]
SI = dict(zip(si_units, si_values))

us_units = ["nm", "mi", "fur", "ch", "yd", "ft", "in", "th"]
us_values = [6076.115, 5280, 660, 66, 3, 1, 1 / 12, 1 / 12000]
US = dict(zip(us_units, us_values))

ft = 3.28084


def __convert_si_si(x, fr, to='m'):
    result = floatint(x * SI[fr] / SI[to])
    return result


def __convert_us_us(x, fr, to='ft'):
    result = floatint(x * US[fr] / US[to])
    return result


def __convert_si_us(x, fr, to):
    meters = __convert_si_si(x, fr)
    feets = meters * ft
    result = __convert_us_us(feets, 'ft', to)
    return result


def __convert_us_si(x, fr, to):
    feets = __convert_us_us(x, fr)
    meters = feets / ft
    result = __convert_si_si(meters, 'm', to)
    return result


def length(x, fr, to, rnd=None, return_res=True, print_res=False, swap=False):
    if swap:
        fr, to = to, fr
    error = "invalid conversion from {} to {}".format(fr, to)
    try:
        if fr in SI:
            if to in SI:
                res = __convert_si_si(x, fr, to)
            elif to in US:
                res = __convert_si_us(x, fr, to)
            else:
                raise TypeError
        elif fr in US:
            if to in US:
                res = __convert_us_us(x, fr, to)
            elif to in SI:
                res = __convert_us_si(x, fr, to)
            else:
                raise TypeError
        else:
            raise TypeError
    except TypeError:
        raise TypeError(error)

    res = floatint(res, rnd=rnd)
    if print_res:
        print(str(x) + fr, "= {:,}".format(res) + to)
    if return_res:
        return res


def main():
    args = [10, 'km', 'm']
    kwargs = {'rnd': 3, 'return_res': True,
              'print_res': True, 'swap': False}
    a = length(*args, **kwargs)
    print(a)


if __name__ == '__main__':
    main()
