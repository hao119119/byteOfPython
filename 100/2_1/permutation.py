N = 3
per = [-1 for i in range(N)]
used = [0 for x in range(N)]


def permutation(pos, n):
    if n == pos:
        print per
        return
    for i in range(n):
        if used[i] == 0:
            per[pos] = i
            used[i] = 1
            permutation(pos+1, n)
            used[i] = 0
    return

permutation(0, N)
