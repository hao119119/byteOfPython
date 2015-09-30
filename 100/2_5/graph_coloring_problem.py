num_v = 4
color = [0 for x in range(num_v)]
G = [[0 for x in range(num_v)] for y in range(num_v)]

# example of no
# G[0][1] = G[0][2] = 1
# G[1][0] = G[1][2] = 1
# G[2][0] = G[2][1] = 1

# example of yes
G[0][1] = G[0][3] = 1
G[1][0] = G[1][2] = 1
G[2][1] = G[2][3] = 1
G[3][0] = G[3][2] = 1


def dfs(v, c):
    color[v] = c
    for i in range(num_v):
        if G[v][i] == 1:
            if color[i] == c:
                return False
            if color[i] == 0 and not dfs(i, -c):
                return False
    return True


def solve():
    for i in range(num_v):
        if color[i] == 0:
            if not dfs(i, 1):
                print 'no'
                return
    print 'yes'

solve()
