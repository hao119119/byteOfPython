N = 10
M = 10
maze = [list("#S######.#"),
        list("......#..#"),
        list(".#.##.##.#"),
        list(".#........"),
        list("##.##.####"),
        list("....#....#"),
        list(".#######.#"),
        list("....#....."),
        list(".####.###."),
        list("....#...G#")]

queue = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
sx = 0
sy = 1
gx = 9
gy = 8
distance = [["x" for x in range(0, N)] for y in range(0, M)]
print distance
distance[sx][sy] = 0
start = [sx, sy]
queue.append(start)
while len(queue) > 0:
    point = queue.pop(0)
    if point[0] == gx and point[1] == gy:
        break
    for i in range(0, 4):
        nx = point[0]+dx[i]
        ny = point[1]+dy[i]
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != '#' and distance[nx][ny] == "x":
            distance[nx][ny] = distance[point[0]][point[1]]+1
            queue.append([nx, ny])

print distance[gx][gy]
for i in range(0, len(distance)):
    print distance[i]
