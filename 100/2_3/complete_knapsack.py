n = 3
p = [(3, 4), (4, 5), (2, 3)]  # (w, v)
W = 7
# complete knapsack can pick any num of one entry
# dp[i+1][j] means has picked from front i item and weight less than j, the most value
# dp[0][j] = 0
# dp[i+1][j] = max(dp[i][j-k*w[i]]+k*v[i]|0<=k)
dp = [[0 for x in range(W+1)] for y in range(n+1)]


def solve():
    for i in range(n):
        for j in range(W+1):
            # for k=0; k*w[i] <= j; k++
            k = 0
            while k*p[i][0] <= j:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-k*p[i][0]]+k*p[i][1])
                k += 1
    print dp[n][W]
solve()

# dp[i+1][j] = max(dp[i][j-k*w[i]]+k*v[i]|0<=k)
#    = max(dp[i][j], max(dp[i][j-k*w[i]]+k*v[i]|1<=k)
#    = max(dp[i][j], max(dp[i][j-w[i]-k*w[i]]+v[i]|0<=k)
#    = max(dp[i][j], dp[i][j-w[i]]+v[i])
dp = [[0 for x in range(W+1)] for y in range(n+1)]


def solve_v2():
    for i in range(n):
        for j in range(W+1):
            if j < p[i][0]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-p[i][0]]+p[i][1])
    print dp[n][W]
solve_v2()

# reuse the array for solve 0-1 knaspack problem
# dp means has pick from front i, the weight is less than j, the most value
dp = [0 for x in range(W+1)]


def solve_v3():
    for i in range(n):
        for j in range(W, p[i][0], -1):
            dp[j] = max(dp[j], dp[j-p[i][0]]+p[i][1])
    print dp[W]
solve_v3()

# reuse the array for solve complete knaspack problem
# dp means has pick from front i, the weight is j, the most value
dp = [0 for x in range(W+1)]


def solve_v4():
    for i in range(n):
        for j in range(p[i][0], W+1):
            dp[j] = max(dp[j], dp[j-p[i][0]]+p[i][1])
    print dp[W]
solve_v4()


# if the limit changed, need trans the problem in other format
# 1 <= n <= 100
# 1 <= w[i] <= 10**7
# 1 <= v[i] <= 100
# 1 <= W <= 10**9
MAX_N = 100
MAX_V = 100
# dp means has picked from front i the total value is j the least weight
# dp[0][0] = 0
# dp[0][j] = INF
# dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i]
import sys
dp = [[0 for x in range(MAX_N*MAX_V+1)] for y in range(MAX_N)]
for x in range(MAX_N*MAX_V+2):
    dp[0][x] = sys.maxint


def solve_v5():
    for i in range(n):
        for j in range(MAX_N*MAX_V+1):
            if j < p[i][1]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j], dp[i][j-p[i][1]]+p[i][0])
    res = 0
    for i in range(MAX_N*MAX_V+1):
        if dp[n][i] <= W:
            res = i
    print res
