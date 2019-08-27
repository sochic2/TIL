import sys
sys.stdin = open('등산로조성.txt')
def dfs(y, x, n, cnt):
    global K, result
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
        if maparr[y][x] > maparr[ny][nx] and visit[ny][nx] == 0:
            visit[ny][nx] = 1
            dfs(ny, nx, n, cnt+1)
            visit[ny][nx] = 0
        else:
            if n == 1:
                if maparr[ny][nx] - maparr[y][x] < K and visit[ny][nx] == 0:
                    basket = maparr[ny][nx]
                    maparr[ny][nx] = maparr[y][x] - 1
                    visit[ny][nx] = 1
                    dfs(ny, nx, 0, cnt+1)
                    visit[ny][nx] = 0
                    maparr[ny][nx] = basket
    if result < cnt:
        result = cnt

    return


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    maparr = [list(map(int, input().split())) for _ in range(N)]
    peak = 0
    for y in range(N):
        for x in range(N):
            if maparr[y][x] > peak:
                peak = maparr[y][x]
    candidate = []
    visit = [[0] * N for _ in range(N)]
    result = 0
    for y in range(N):
        for x in range(N):
            if maparr[y][x] == peak:
                candidate.append((y, x))

    for i in range(len(candidate)):
        y, x = candidate[i][0], candidate[i][1]
        visit[y][x] = 1
        dfs(y, x, 1, 1)
        visit[y][x] = 0
    print('#{} {}'.format(tc, result))