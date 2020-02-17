import sys
sys.setrecursionlimit(300000000)

def dfs(y, x):
    if memo[y][x]:
        return memo[y][x]
    memo[y][x] = 1

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:continue
        if forest[ny][nx] > forest[y][x]:
            memo[y][x] = max(dfs(ny, nx)+1, memo[y][x])
    return memo[y][x]




N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
memo = [[0]*N for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for y in range(N):
    for x in range(N):
        if memo[y][x] == 0:
            dfs(y, x)

mmax = -987654321
for y in range(N):
    for x in range(N):
        if mmax < memo[y][x]:
            mmax =memo[y][x]

print(mmax)