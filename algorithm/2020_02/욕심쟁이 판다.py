import sys
sys.setrecursionlimit(300000000)
def dfs(y, x):
    if memo[y][x]:
        return memo[y][x]
    memo[y][x] = 1
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= nx < N and 0 <= ny < N and forest[y][x] < forest[ny][nx]:
            memo[y][x] = max(memo[y][x], dfs(ny, nx)+1)
    return memo[y][x]

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
memo = [[0]*N for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


for y in range(N):
    for x in range(N):
        memo[y][x] = dfs(y, x)

print(max(map(max, memo)))