n = 4
m = 4
s = 'abcd'
t = 'becd'

# dp[i][j] means the length of LCS between s[1]-s[i] and t[1][j]
dp = [[0 for x in range(m+1)] for y in range(n+1)]


# if s[i+1] = t[j+1]:
#       dp[i+1][j+1] = max(dp[i][j]+1, dp[i][j+1], dp[i+1][j])
# else:
#       max(dp[i][j+1], dp[i+1][j])
def solve():
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    print dp[n][m]
