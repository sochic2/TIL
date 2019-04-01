def bfs():
    global mmax, M, N, H
    for a in range(H):
        for b in range(N):
            for c in range(M):
               if data[a][b][c] == 1:
                    q.append((a, b, c, 0))
    while q:
        z, y, x, time = q.pop(0)
        if time > mmax:
            mmax = time
        for i in range(4):
            if y+ dy[i] < 0 or y+dy[i] >= N or x + dx[i] < 0 or x + dx[i] >= M: continue
            if data[z][y + dy[i]][x + dx[i]] == 0:
                q.append((z, y+ dy[i], x + dx[i], time+1))
                data[z][y + dy[i]][x + dx[i]] = 1
        for j in range(2):
            if z + dz[j] < 0 or z + dz[j] >= H: continue
            if data[z + dz[j]][y][x] == 0:
                q.append((z+dz[j], y, x, time + 1))
                data[z+dz[j]][y][x] = 1



M, N, H = map(int,input().split())   # X, Y, Z
data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# print(data)
mmax = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
dz = [1, -1]
q = []
bfs()
flag = 0
for a in range(H):
    for b in range(N):
        for c in range(M):
            if data[a][b][c] == 0:
                flag = 1

if flag == 1:
    print(-1)
else:
    print(mmax)