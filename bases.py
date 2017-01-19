from structures.stacks import Stack


def base_converter(decimal, base, formatted=False):
    number = decimal
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    bits = decimal // 256 + 1
    while decimal > 0:
        rem = decimal % base
        rem_stack.push(rem)
        decimal //= base
    new_str = ""
    while not rem_stack.isempty():
        new_str += digits[rem_stack.pop()]

    if not formatted:
        return new_str
    else:
        if base == 2:
            new_str = new_str.zfill(8*bits)
            return "{} in binary: {}".format(str(number), new_str)
        elif base == 8:
            return "{} in octal: {}".format(str(number), new_str)
        elif base == 16:
            return "{} in hexadecimal: {}".format(str(number), new_str)
        else:
            return "{} in base {}: {}".format(str(number), str(base), new_str)


def hex_to_rgb(value):
    leng = len(value)
    colors = tuple(int(value[i:i+leng//3], 16) for i in range(0, leng, leng//3))
    return colors


if __name__ == "__main__":
    from list_functions import product
    print(hex_to_rgb("ffffff"))
    mylist = [1, 2, 3, 4, 5, 6, 7]
    print(product(mylist, 1, 3))
    print(base_converter(128, 16))
    # print(base_converter(255, 16))
    # print(base_converter(255, 16))
