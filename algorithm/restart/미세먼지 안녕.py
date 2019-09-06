import sys
sys.stdin = open('미세먼지 안녕.txt')

def hwak(arr):
    visit = [[0] * X for _ in range(Y)]
    for i in range(2):
        yy = cleaner[i][0]
        xx = cleaner[i][1]
        visit[yy][xx] = -1
    for y in range(Y):
        for x in range(X):
            if arr[y][x] != -1:
                count = 0
                division = arr[y][x] // 5
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or nx < 0 or ny >= Y or nx >= X:continue
                    if arr[ny][nx] == -1:continue
                    visit[ny][nx] = visit[ny][nx] + division
                    count += 1
                visit[y][x] = visit[y][x] + arr[y][x] - (division*count)
    return clean(visit)

def clean(visit):
    goal_y = cleaner[0][0]
    goal_x = cleaner[0][1]
    y = goal_y - 1
    x = goal_x
    while y != 0:
        visit[y][x] = visit[y-1][x]
        y -= 1
    while x != X-1:
        visit[y][x] = visit[y][x+1]
        x+=1
    while y != goal_y:
        visit[y][x] = visit[y+1][x]
        y += 1
    while x != goal_x:
        if visit[y][x-1] == -1:
            visit[y][x] = 0
        else:
            visit[y][x] = visit[y][x-1]
        x -= 1
    goal_y = cleaner[1][0]
    goal_x = cleaner[1][1]
    y = goal_y+1
    x = goal_x
    while y != Y-1:
        visit[y][x] = visit[y + 1][x]
        y += 1
    while x != X - 1:
        visit[y][x] = visit[y][x + 1]
        x += 1
    while y != goal_y:
        visit[y][x] = visit[y - 1][x]
        y -= 1
    while x != goal_x:
        if visit[y][x - 1] == -1:
            visit[y][x] = 0
        else:
            visit[y][x] = visit[y][x - 1]
        x -= 1

    return visit


Y, X, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Y)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cleaner = []
for y in range(Y):
    for x in range(X):
        if arr[y][x] == -1:
            cleaner.append((y,x))

for _ in range(T):
    arr = hwak(arr)
result = 0
for y in range(Y):
    for x in range(X):
        if arr[y][x] != -1:
            result += arr[y][x]
print(result)