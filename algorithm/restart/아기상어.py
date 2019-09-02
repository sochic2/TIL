import sys
sys.stdin = open('아기상어.txt')

def check(possible):
    global mmax
    if len(possible):
        possible.sort()
        time, y, x, size, feed = possible.pop(0)
        if mmax < time:
            mmax = time
        if feed == 0:
            q = [(time, y, x, size+1, size+1)]
            arr[y][x] = 0
            bfs(q)
        else:
            q = [(time, y, x, size, feed)]
            arr[y][x] = 0
            bfs(q)

    else:
        return

def bfs(q):
    global mmax
    visit = [[0 for _ in range(N)] for _ in range(N)]
    possible = []

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        time, y, x, size, feed = q.pop(0)
        visit[y][x] = 1
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny < 0 or nx < 0 or nx >= N or ny >= N:
                continue


            if visit[ny][nx] == 0:
                # 먹기 가능
                if arr[ny][nx] < size and arr[ny][nx] != 0:
                    possible.append((time+1, ny, nx, size, feed-1))
                    visit[ny][nx] = 1

                if arr[ny][nx] == size or arr[ny][nx] == 0:
                    q.append((time+1, ny, nx, size, feed ))
                    visit[ny][nx] = 1

    check(possible)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 9:
            q.append((0, y, x, 2, 2))
            arr[y][x] = 0



mmax = 0
bfs(q)

print(mmax)