import sys
sys.stdin = open('연구소.txt')

def check():
    global mmax
    mapp = [[0 for _ in range(X)] for _ in range(Y)]
    q = []
    for y in range(Y):
        for x in range(X):
            if arr[y][x] == 2:
                q.append((y, x))
            mapp[y][x] = arr[y][x]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        y, x = q.pop(0)
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if nx < 0 or ny < 0 or nx >= X or ny >= Y: continue
            if mapp[ny][nx] == 0:
                mapp[ny][nx] = 2
                q.append((ny, nx))
    result = 0
    for y in range(Y):
        for x in range(X):
            if mapp[y][x] == 0:
                result += 1
    if result > mmax:
        mmax = result


def dfs(n):
    if n ==  3:
        check()

    else:
        for y in range(Y):
            for x in range(X):
                if arr[y][x] == 0:
                    arr[y][x] =1
                    dfs(n+1)
                    arr[y][x] = 0


Y, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Y)]
mmax = -987654321
dfs(0)

print(mmax)



