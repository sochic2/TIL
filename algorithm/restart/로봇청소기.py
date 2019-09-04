import sys
sys.stdin = open('로봇청소기.txt')

def dfs(y, x, d):
    arr[y][x] = 2
    for i in range(4):
        d = (d+3) % 4
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or nx < 0 or ny >= Y or nx >= X: continue
        if arr[ny][nx] == 0:
            dfs(ny, nx, d)
            return
    backy = y + dy[(d+2)%4]
    backx = x + dx[(d+2)%4]
    if backy >= 0 and backx >= 0 and backy < Y and backx < X:
        if arr[backy][backx] != 1:
            dfs(backy, backx, d)
            return
    return


Y, X = map(int, input().split())
y, x, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Y)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dfs(y, x, d)
result = 0
for y in range(Y):
    for x in range(X):
        if arr[y][x] == 2:
            result += 1
print(result)