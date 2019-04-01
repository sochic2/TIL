def dfs(i, j, a):
    y = i
    x = j
    alpha = a
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N: continue
        if paint[new_y][new_x] == alpha and visit[new_y][new_x] == 0:
            visit[new_y][new_x] = 1
            dfs(new_y, new_x, alpha)


def dfs_2(i, j, a):
    y = i
    x = j
    alpha = a
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N: continue
        if paint[new_y][new_x] == alpha and visit_2[new_y][new_x] == 0:
            visit_2[new_y][new_x] = 1
            dfs_2(new_y, new_x, alpha)




N = int(input())
paint = [list(input()) for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

visit = [[0] * N for _ in range(N)]
formal = 0
for i in range(N):
    for j in range(N):
        if paint[i][j] and visit[i][j] == 0:
            formal += 1
            visit[i][j] = 1
            dfs(i, j, paint[i][j])


for i in range(N):
    for j in range(N):
        if paint[i][j] == 'R':
            paint[i][j] = 'G'

rg = 0
visit_2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if paint[i][j] and visit_2[i][j] == 0:
            rg += 1
            visit[i][j] = 1
            dfs_2(i, j, paint[i][j])



print(formal, end=' ')
print(rg)