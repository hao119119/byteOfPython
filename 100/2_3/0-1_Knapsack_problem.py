p = [(2, 3), (1, 2), (3, 7), (2, 4)]
W = 5
N = len(p)
max_value = 0


def find_stuff(i, weight, value):
    global max_value
    if i == N:
        if max_value < value and weight <= W:
            max_value = value
        return
    find_stuff(i+1, weight + p[i][0], value + p[i][1])
    find_stuff(i+1, weight, value)

find_stuff(0, 0, 0)
print max_value


# i for index, j for left weight
def rec(i, j):
    res = 0
    if i == N:
        pass
    elif j < p[i][0]:
        res = rec(i+1, j)
    else:
        res = max(rec(i+1, j), rec(i+1, j - p[i][0])+p[i][1])
    return res

v = rec(0, 5)
print v


dp = [[-1 for x in range(0, W+1)] for y in range(0, N+1)]


def rec_v2(i, j):
    res = 0
    if dp[i][j] >= 0:
        return dp[i][j]
    if i == N:
        pass
    elif j < p[i][0]:
        res = rec_v2(i+1, j)
    else:
        res = max(rec_v2(i+1, j), rec_v2(i+1, j-p[i][0])+p[i][1])
    dp[i][j] = res
    return res
v = rec_v2(0, W)
print v


# dp[i][j] means has pick from front i and the total weight not more than j, the most value
dp_v2 = [[0 for x in range(0, W+1)] for y in range(0, N+1)]


# left down to right up
def dp_solve():
    for i in range(N-1, -1, -1):
        for j in range(W+1):
            if j < p[i][0]:
                dp_v2[i][j] = dp_v2[i+1][j]
            else:
                dp_v2[i][j] = max(dp_v2[i+1][j], dp_v2[i+1][j-p[i][0]]+p[i][1])
    print dp_v2[0][W]
dp_solve()


# dp[i][j] means has pick from front i and the total weight not more than j, the most value
# reset value
dp_v2 = [[0 for x in range(0, W+1)] for y in range(0, N+1)]


# left up to right down
def dp_solve_v2():
    for i in range(N):
        for j in range(W+1):
            if j < p[i][0]:
                dp_v2[i+1][j] = dp_v2[i][j]
            else:
                dp_v2[i+1][j] = max(dp_v2[i][j], dp_v2[i][j-p[i][0]]+p[i][1])
    print dp_v2[N][W]
dp_solve_v2()



# dp[i][j] means has picked from front i and the value is j, the least weight
dp_v3 = [[0 for x in range(0, W+1)] for y in range(0, N+1)]
# to be continued


#

