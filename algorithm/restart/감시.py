import sys
sys.stdin = open('감시.txt')

def check():
    global mmin
    office = [[0 for _ in range(X)] for _ in range(Y)]
    for y in range(Y):
        for x in range(X):
            if arr[y][x] == 6:
                office[y][x] = arr[y][x]
    for i in range(len(cctv)):
        y, x, tv, d = cctv[i][0], cctv[i][1], cctv[i][2], direction[i]
        office[y][x] = 9
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        if tv == 1:
            while True:
                y = y + dy[d]
                x = x + dx[d]
                if y < 0 or x < 0 or y >= Y or x >= X: break
                if office[y][x] == 6: break
                office[y][x] = 9

        if tv == 2:
            for i in range(0, 3, 2):
                ny = y
                nx = x
                while True:
                    ny = ny + dy[d-i]
                    nx = nx + dx[d-i]
                    if ny < 0 or nx < 0 or ny >= Y or nx >= X:break
                    if office[ny][nx] == 6:break
                    office[ny][nx] = 9


        if tv == 3:
            for i in range(2):
                ny = y
                nx = x
                while True:
                    ny = ny + dy[d-i]
                    nx = nx + dx[d-i]
                    if ny < 0 or nx < 0 or ny >= Y or nx >= X:break
                    if office[ny][nx] == 6:break
                    office[ny][nx] = 9
        if tv == 4:
            for i in range(3):
                ny = y
                nx = x
                while True:
                    ny = ny + dy[d-i]
                    nx = nx + dx[d-i]
                    if ny < 0 or nx < 0 or ny >= Y or nx >= X:break
                    if office[ny][nx] == 6:break
                    office[ny][nx] = 9

        if tv == 5:
            for i in range(4):
                ny = y
                nx = x
                while True:
                    ny = ny + dy[d-i]
                    nx = nx + dx[d-i]
                    if ny < 0 or nx < 0 or ny >= Y or nx >= X:break
                    if office[ny][nx] == 6:break
                    office[ny][nx] = 9

    result = 0
    for y in range(Y):
        for x in range(X):
            if office[y][x] == 0:
                result += 1
    if result < mmin:
        mmin = result


def dfs(n):
    if n >= len(cctv):
        check()
        return
    else:
        for i in range(4):
            direction[n] = i
            dfs(n+1)
            direction[n] = 0


Y, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Y)]
mmin = 987654321
cctv = []
for y in range(Y):
    for x in range(X):
        if 0 < arr[y][x] < 6:
            cctv.append((y, x, arr[y][x]))
direction = [0] * len(cctv)
dfs(0)
print(mmin)
