import random


def parent(i):
    return i >> 1


def left(i):
    return i << 1


def right(i):
    return (i << 1) + 1


def max_heapify(data, i):
    l = left(i)
    r = right(i)
    if l < len(data) and data[i] < data[l]:
        largest = l
    else:
        largest = i
    if r < len(data) and data[largest] < data[r]:
        largest = r
    if i != largest:
        tmp = data[i]
        data[i] = data[largest]
        data[largest] = tmp
        max_heapify(data, largest)


def build_max_heap(data):
    for i in range(len(data)/2-1, -1, -1):
        max_heapify(data, i)


def min_heapify(data, i):
    l = left(i)
    r = right(i)
    if l < len(data) and data[l] < data[i]:
        minimum = l
    else:
        minimum = i
    if r < len(data) and data[r] < data[minimum]:
        minimum = r
    if minimum != i:
        tmp = data[i]
        data[i] = data[minimum]
        data[minimum] = tmp
        min_heapify(data, minimum)


def build_min_heap(data):
    for i in range(len(data)/2-1, -1, -1):
        min_heapify(data, i)


def make_random_data(size):
    data = [random.randint(1, 101) for _ in range(size)]
    return data

if __name__ == '__main__':
    random_data = make_random_data(10)
    print random_data
    build_max_heap(random_data)
    print random_data
    build_min_heap(random_data)
    print random_data
