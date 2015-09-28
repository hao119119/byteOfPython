from Queue import PriorityQueue
se = 0


def parent(i):
    return i / 2


def left(i):
    return i * 2


def right(i):
    return i * 2 + 1


def push(heap, x):
    heap.append(x)
    i = len(heap) - 1
    while i > 1:
        p = parent(i)
        if heap[p] <= x:
            break
        heap[p], heap[i] = heap[i], heap[p]
        i = p


def pop(heap):
    x = heap[1]
    if len(heap) > 2:
        heap[1] = heap.pop(len(heap) - 1)
    else:
        return heap.pop(len(heap) - 1)
    i = 1
    while left(i) < len(heap):
        l = left(i)
        r = right(i)
        if l < len(heap) and heap[i] > heap[l]:
            minimum = l
        else:
            minimum = i
        if r < len(heap) and heap[r] < heap[minimum]:
            minimum = r
        if minimum == i:
            break
        else:
            heap[minimum], heap[i] = heap[i], heap[minimum]
            i = minimum
    return x


# Expedition (POJ2431)
# num of station
N = 4
# total distance
L = 25
# the gas which the car takes
P = 10
# distance of stations
A = [10, 14, 20, 21]
# gas the stations can offer
B = [10, 5, 2, 4]


def solve():
    # add the end as a gas station which can offer 0 gas. just for convenient
    A.append(L)
    B.append(0)
    global N
    N += 1
    que = PriorityQueue()

    # time of add gas
    ans = 0
    # position of current
    pos = 0
    # gas remains
    tank = P

    for i in range(N):
        d = A[i] - pos
        while tank - d < 0:
            if que.empty():
                return
            tank += que.get()*-1
            ans += 1
        tank -= d
        pos = A[i]
        que.put(B[i]*-1)
    print ans

solve()
