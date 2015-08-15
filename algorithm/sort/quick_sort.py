import random

data = [random.randint(1, 101) for _ in range(10)]
print data


def partition(_data, p, r):
    i = p - 1
    x = _data[r]
    for j in range(p, r):
        if _data[j] <= x:
            tmp = _data[j]
            _data[j] = _data[i + 1]
            _data[i + 1] = tmp
            i += 1
    tmp = _data[i + 1]
    _data[i + 1] = _data[r]
    _data[r] = tmp
    return i + 1


def quick_sort(_data, start, end):
    if start < end:
        position = partition(_data, start, end)
        quick_sort(_data, start, position - 1)
        quick_sort(_data, position + 1, end)


if __name__ == '__main__':
    quick_sort(data, 0, len(data) - 1)
    print data



