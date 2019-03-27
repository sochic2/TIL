def bfs():
    global zerg_x, zerg_y
    q = []
    solution = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q.append([zerg_y, zerg_x, 3])
    data[zerg_y][zerg_x] =0
    while q:
        a = q.pop(0)
        if a[2] > solution:
            solution = a[2]
        for i in range(4):
            if data[a[0]+dy[i]][a[1]+dx[i]]:
                q.append([a[0]+dy[i], a[1]+dx[i], a[2]+1])
                data[a[0]+dy[i]][a[1]+dx[i]] = 0
    return solution



X, Y = map(int, input().split())
data = [[0] + list(map(int, input())) + [0] for _ in range(Y)]
y_wall = [0] * (X+2)
zerg_x, zerg_y = map(int, input().split())
data.insert(0, y_wall)
data.append(y_wall)
# for i in data:
#     print(*i)
print(bfs())
ssum = 0
for i in data:
    ssum += sum(i)
print(ssum)