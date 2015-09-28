import sys
n = 5
a = [4, 2, 3, 1, 5]
# dp[i] the length of longest increasing subsequence which end with a[i]
# dp[i] = max(1, dp[j]+1|j<i And a[j] < a[i])
dp = [0 for x in range(n)]


def solve():
    res = 0
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
    print res
solve()


b = [1, 2, 4, 8, 9, 15, 18, 20, 21]


def binary_search(array, start, length, num):
    assert len(array)-start >= length
    end = start + length - 1
    while start <= end:
        middle = start + (end - start) / 2
        middle_num = array[middle]
        if middle_num < num:
            start = middle + 1
            continue
        elif middle_num > num:
            end = middle - 1
            continue
        else:
            return middle
    return None

print binary_search(b, 0, len(b), 16)


def lower_bound(array, start, length, num):
    assert len(array)-start >= length
    end = start + length - 1
    while start < end:
        middle = start + (end - start) / 2
        middle_num = array[middle]
        if middle_num < num:
            start = middle + 1
            continue
        elif middle_num > num:
            end = middle - 1
            continue
        else:
            return middle - 1
    if array[start] < num:
        return start
    else:
        return start-1

print lower_bound(b, 0, len(b), 2)


def solve_v2():
    dp_v2 = [sys.maxint for x in range(n)]
    for i in range(n):
        position = lower_bound(dp_v2, 0, n, a[i])
        dp_v2[position+1] = a[i]
    print dp_v2

solve_v2()


