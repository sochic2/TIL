def bfs():
    q = []
    solution = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                q.append([i, j, 0])
    while q:
        a = q.pop(0)
        if a[2] > solution:
            solution = a[2]

        for k in range(4):
            if a[0] + dy[k] < 0 or a[0] + dy[k] >= N or a[1] + dx[k] < 0 or a[1] + dx[k] >= M: continue
            else:
                if data[a[0] + dy[k]][a[1]+ dx[k]] == 0:
                    q.append([a[0]+dy[k], a[1]+dx[k], a[2]+1])
                    data[a[0] + dy[k]][a[1] + dx[k]] = 1
    return solution



M, N = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(N)]
result = bfs()
flag =0
for i in data:
    if 0 in i:
        flag = 1

if flag == 1:
    print(-1)
else:
    print(result)


