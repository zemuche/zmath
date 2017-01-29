from zmath.fraction import Fraction, floatfrac, subscripts, superscripts


class Polynomial:
    def __init__(self, coefficients):
        self.__coefficients = coefficients
        self.__string = self.__format_expr(foreval=False)
        self.__expression = self.__format_expr()

    def __str__(self):
        return self.__string

    def eval(self, *args):
        results = []
        for x in args:
            answer = eval(self.__expression)
            if len(args) == 1:
                return floatfrac(answer)
            else:
                results.append(floatfrac(answer))
        return results

    def derivative(self):
        expr = []
        length = len(self.__coefficients)
        for i, c in enumerate(self.__coefficients):
            if c == 0:
                continue
            else:
                if i == length - 1:
                    break
                if i > 0:
                    expr.append(' + ' if c > 0 else ' - ')
                    c = abs(c)
                exp = length - i - 1
                expr.append(Fraction(c * exp))
                if exp > 1:
                    expr.append('x')
                    if exp > 2:
                        expr.append(superscript(exp - 1))
        return ''.join(str(x) for x in expr)

    def graph(self):
        pass

    def __format_expr(self, foreval=True):
        expr = []
        length = len(self.__coefficients)
        for i, c in enumerate(self.__coefficients):
            if c == 0:
                continue
            else:
                if i > 0:
                    expr.append('+' if c > 0 else '-')
                    c = abs(c)
                coef = str(c) + ' * ' if foreval else Fraction(c)
                exponent = length - i - 1
                exp = str(exponent)
                term = "{}x{}" if int(exp) > 1 else "{}x"
                exp = " ** {}".format(exp) if foreval else superscript(exp)
                term = term.format(coef, exp) if exponent > 0 else str(c)
                expr.append(term)
        return ' '.join(expr)


def superscript(num):
    return ''.join(superscripts[n] for n in str(num))


def subscript(num):
    return ''.join(subscripts[n] for n in str(num))


def main():
    # print(degrees)
    p = Polynomial([4, 3/2, -2, 1])
    print(p)
    print(p.derivative())

if __name__ == '__main__':
    main()
