def bubble_sort(iterable):
    passes = len(iterable) - 1
    exchange = True
    while passes > 0 and exchange:
        exchange = False
        for i in range(passes):
            if iterable[i] > iterable[i+1]:
                exchange = True
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
        passes -= 1
    return iterable


def selection_sort(sequence):
    length = len(sequence)
    for i in range(length-1):
        mini = i
        exchange = False
        for j in range(i+1, length):
            if sequence[j] < sequence[mini]:
                mini = j
                exchange = True
        if exchange:
            sequence[i], sequence[mini] = sequence[mini], sequence[i]
    return sequence


def insertion_sort(sequence):
    length = len(sequence)
    for i in range(1, length):
        key = sequence[i]
        j = i
        while j > 0 and sequence[j-1] > key:
            sequence[j] = sequence[j-1]
            j -= 1
        sequence[j] = key
    return sequence


def merge_sort(alist):
    def _merge_sort(iterable, first, last):
        mid = (first + last) // 2
        if first < last:
            _merge_sort(iterable, first, mid)
            _merge_sort(iterable, mid + 1, last)

            a, z, k = first, mid + 1, 0
            temp = [None] * (last - first + 1)
            while a <= mid and z <= last:
                if iterable[a] < iterable[z]:
                    temp[k] = iterable[a]
                    a += 1
                else:
                    temp[k] = iterable[z]
                    z += 1
                k += 1

            if a <= mid:
                temp[k:] = iterable[a:mid + 1]
            if z <= last:
                temp[k:] = iterable[z:last + 1]

            k = 0
            while first <= last:
                iterable[first] = temp[k]
                first += 1
                k += 1
    _merge_sort(alist, 0, len(alist) - 1)
    return alist


def quick_sort(iterable):
    import statistics as stat
    less = []
    equal = []
    greater = []

    if len(iterable) > 1:
        three = [iterable[0], iterable[len(iterable) // 2], iterable[-1]]
        pivot = stat.median(three)
        for i in iterable:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
        return quick_sort(less) + equal + quick_sort(greater)

    else:
        return iterable


def heap_sort(iterable):
    # Convert list to heap
    length = len(iterable) - 1
    least_parent = int(length / 2)
    for i in range(least_parent, -1, -1):
        move_down(iterable, i, length)

    # Flatten heap into sorted array
    for i in range(length, 0, -1):
        if iterable[0] > iterable[i]:
            swap(iterable, 0, i)
            move_down(iterable, 0, i-1)

    return iterable


def move_down(iterable, first, last):
    largest = (2 * first) + 1
    while largest <= last:
        # Right child exists and is larger than left child
        if (largest < last) and (iterable[largest] < iterable[largest+1]):
            largest += 1

        # Right child is larger than parent
        if iterable[largest] > iterable[first]:
            swap(iterable, largest, first)
            # Move down to largest child
            first = largest
            largest = (2 * first) + 1
        else:
            return                      # Force exit


def swap(a, x, y):
    a[x], a[y] = a[y], a[x]


def main():
    original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = original[:]

    print("Original list: {}".format(original))
    print("{}: {}".format(bubble_sort.__name__, bubble_sort(a)))
    print("{}: {}".format(selection_sort.__name__, selection_sort(a)))
    print("{}: {}".format(insertion_sort.__name__, insertion_sort(a)))
    print("{}: {}".format(merge_sort.__name__, merge_sort(a)))
    print("{}: {}".format(quick_sort.__name__, quick_sort(a)))
    print("{}: {}".format(heap_sort.__name__, heap_sort(a)))


if __name__ == '__main__':
    main()
