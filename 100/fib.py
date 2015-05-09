N = 8
memo = [0 for x in range(0, N+1)]


def fib(num):
    if num <= 1: return 1
    if memo[num] != 0:
        return memo[num]
    memo[num] = fib(num - 1) + fib(num - 2)
    return memo[num]


print fib(N)

print memo