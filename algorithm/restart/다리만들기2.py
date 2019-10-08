import sys
sys.stdin = open('다리만들기2.txt')

def island(y, x, cnt):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= Y or nx >= X:continue
        if arr[ny][nx] == 1 and narr[ny][nx] == 0:
            narr[ny][nx] = cnt
            island(ny, nx, cnt)

Y, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Y)]
narr = [[0] * X for _ in range(Y)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 1
for y in range(Y):
    for x in range(X):
        if arr[y][x] == 1 and narr[y][x] == 0:
            narr[y][x] = cnt
            island(y, x, cnt)
            cnt += 1


