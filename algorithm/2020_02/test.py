import sys
sys.setrecursionlimit(300000)
def dfs(i, j):
    if memo[i][j]:
        return memo[i][j]
    memo[i][j] = 1
    for a in range(4):
        ni, nj = i+di[a], j+dy[a]
        if 0 <= ni < N and 0 <= nj < N and forest[i][j] < forest[ni][nj]:
            memo[i][j] = max(memo[i][j], dfs(ni, nj)+1)
    return memo[i][j]

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
memo = [[0] * N for _ in range(N)]
di = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        memo[i][j] = dfs(i, j)
print(max(map(max, memo)))