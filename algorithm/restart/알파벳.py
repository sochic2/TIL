import sys
sys.stdin = open('알파벳.txt')

def dfs(y, x, alpha, cnt):
    global mmax
    if cnt > mmax:
        mmax = cnt
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or ny < 0 or ny >= Y or nx >= X:continue
        if arr[ny][nx] not in alpha:
            dfs(ny, nx, alpha+arr[ny][nx], cnt+1)


Y, X = map(int, input().split())
arr = [input() for _ in range(Y)]
mmax = -987654321
dfs(0, 0, arr[0][0], 1)
print(mmax)