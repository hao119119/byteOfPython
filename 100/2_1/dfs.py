n = 3
a = [1, 2, 4, 7]
k = 3


def dfs(i, summary):
    if i == n:
        return k == summary
    if dfs(i + 1, summary):
        return True
    if dfs(i + 1, summary + a[i]):
        return True
    return False


print dfs(0, 0)

field = [list("W........WW."),
         list(".WWW.....WWW"),
         list("....WW...WW."),
         list(".........WW."),
         list(".........W.."),
         list("..W......W.."),
         list(".W.W.....WW."),
         list("W.W.W.....W."),
         list(".W.W......W."),
         list("..W.......W.")]
N = 10
M = 12


def dfs_find(x, y):
    if field[x][y] == 'W':
        field[x][y] = "."
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 'W':
                dfs_find(nx, ny)


print field
count = 0
for j in range(0, N):
    for k in range(0, M):
        if field[j][k] == 'W':
            dfs_find(j, k)
            print field
            count += 1
print count