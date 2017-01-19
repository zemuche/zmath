def binsearchrecur(sequence, item, start=0, stop=None):
    if len(sequence) == 0:
        return False
    if stop is None:
        stop = len(sequence)
    if start == stop and item == sequence[start]:
            return start
    mid = (stop + start) // 2
    if item == sequence[mid]:
        return mid
    elif item < sequence[mid]:
        return binsearchrecur(sequence, item, start, mid)
    else:
        return binsearchrecur(sequence, item, mid + 1, stop)


def binsearchiter(sequence, item, return_index=True):
    if len(sequence) == 0:
        return False
    found = False
    start = 0
    end = len(sequence) - 1
    while not found and start < end:
        mid = (start + end) // 2
        if item == sequence[mid]:
            found = True
            if return_index is True:
                return mid
        elif item > sequence[mid]:
            start = mid + 1
        else:
            end = mid
    return found


def linsearch(sequence, target, start=0, end=None):
    """Search linearly for target in sequence between
    start and end, inclusive."""
    if end is None:
        end = len(sequence) - 1
    for i, value in enumerate(sequence[start:end+1], start):
        if value == target:
            break
    else:
        return False
    return i

