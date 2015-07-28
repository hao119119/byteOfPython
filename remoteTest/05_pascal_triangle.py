import pydevd
pydevd.settrace('10.12.11.118', port=51234, stdoutToServer=True, stderrToServer=True)

N = 15
matrix = [[0 for x in range(0, N)] for y in range(0, N)]
for x in range(0, N):
    matrix[x][0] = 1
    matrix[x][x] = 1
    print matrix[x]

print
print
print

for x in range(0, N):
    if x > 1:
        for y in range(1, x):
            matrix[x][y] = matrix[x-1][y-1] + matrix[x-1][y]
    print matrix[x]
