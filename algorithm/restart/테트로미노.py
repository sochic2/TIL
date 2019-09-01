import sys
sys.stdin = open('테트로미노.txt')
def dfs(y, x, n, cnt):
    global mmax
    dy = [0, 0, 1]
    dx = [-1, 1, 0]
    if n >= 4:
        if cnt >= mmax:
            mmax = cnt
            # print(visit)
        return


    for i in range(3):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= 0 or nx >= 0 or ny < N or nx < M:
            if visit[ny][nx] == 0:
                visit[ny][nx] = 1
                dfs(ny, nx, n+1, cnt+arr[ny][nx])
                visit[ny][nx] = 0

def fuck(y, x, count):
    global mmax
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    for i in range(4):
        solution = count
        cnt = 0
        for j in range(4):
            if j == i: continue
            ny = y+dy[j]
            nx = x+dx[j]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                break
            solution += arr[ny][nx]
            cnt += 1
        if cnt == 3:
            if solution > mmax:
                mmax = solution



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

mmax = -987654321


for y in range(N):
    for x in range(M):
        visit = [[False] * M for i in range(N)]
        visit[y][x] = 1
        fuck(y, x, arr[y][x])
        dfs(y, x, 1, arr[y][x])



print(mmax)